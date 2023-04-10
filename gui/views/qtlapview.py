"""
qt lappy main view
"""


from PyQt5 import QtWidgets, QtCore


from src.models.lapmodel import LapModel
from src.utils.helpers import dir_helper
from src.services import project_remover, project_cloner


from gui import prog
from gui.views.uis.ui_qtlapview import UIQtLapView
from gui.services import lapproject_service
from gui.services.project_contextmenu_maker import ProjectContextMenuMaker
from gui.models.loglevelenum import LogLevelEnum
from gui.utils.helpers import question_box, qtreewidgetitem_helper
from gui.models.project_treeview_item_type import ProjectTreeViewItemType
from gui.views.geomview import GeomView
from gui.views.dialogs.project_clone_input_dialog import ProjectCloneInputDialog


class QtLapView(QtWidgets.QMainWindow, UIQtLapView):
    """
    view
    """

    create_empty_project = QtCore.pyqtSignal(str, str)
    log_message = QtCore.pyqtSignal(str, LogLevelEnum)
    close_model = QtCore.pyqtSignal(LapModel)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        UIQtLapView.__init__(self)
        self.setup_ui(self)
        self.__connect()
        self.__read_settings()

    def add_project_to_projects_view(self, model: LapModel):
        item = lapproject_service.to_tree_widget_item(model)
        if item is not None:
            self.proj_explorer_tree.addTopLevelItem(item)

    def __add_tab(self, widget: QtWidgets.QWidget, name: str):
        """
        add tab to pages
        """
        self.main_tab_widget.addTab(widget, name)

    def __connect(self):
        self.new_project_action.triggered.connect(self.__on_new_project_create)
        self.proj_explorer_tree.customContextMenuRequested.connect(
            self.__prepare_project_item_context_menu)
        self.proj_explorer_tree.itemClicked.connect(self.__on_item_clicked)

        self.main_tab_widget.tabCloseRequested.connect(
            lambda index: self.main_tab_widget.removeTab(index))

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def __on_item_clicked(self, item, column):
        if not item:
            return

        if item.Type == ProjectTreeViewItemType.INIT_DATA_GEOM:
            self.__on_geom_open(item, column)

    def __on_geom_open(self, item, column):
        project_item = qtreewidgetitem_helper.get_item_king(item)

        if not project_item:
            self.log_message.emit(
                "Can not define project item", LogLevelEnum.WARNING)
            return

        model = project_item.data(0, QtCore.Qt.UserRole)

        if not model:
            return

        plot = GeomView(self.main_tab_widget)
        plot.set_geom(model.geom)
        self.__add_tab(plot, item.text(column))

        plot.map.scene.fig.tight_layout()

    def __on_new_project_create(self):
        last_dir = self.settings.value('new_project_last_dir')
        last_dir = '' if last_dir is None else last_dir

        project_folder = QtWidgets.QFileDialog.getExistingDirectory(
            self, 'Select Folder', last_dir, options=QtWidgets.QFileDialog.DontUseNativeDialog)

        if not project_folder:
            return

        if dir_helper.dir_contains_files_pattern(project_folder, '.lap'):
            # ask for delete files
            ask_result = question_box.positive_answer(self,
                                                      'Preparing project directory',
                                                      'Chosen directory contains project(s) files. ' +
                                                      'Do you want to delete previous project(s)?')

            if ask_result:
                project_remover.remove_projects_in_dir(project_folder)

        self.settings.setValue('new_project_last_dir', project_folder)

        input_diag = QtWidgets.QInputDialog()

        project_name, status = input_diag.getText(
            self, 'Project name', 'Please, insert the project name' + 20 * ' ')

        if not status:
            return

        self.create_empty_project.emit(project_folder, project_name)

    def __delete_model(self, item):
        model = item.data(0, QtCore.Qt.UserRole)
        ask_res = question_box.positive_answer(self,
                                               'Delete the project',
                                               f'Do you want to permanently delete the project {model.name}?')
        if not ask_res:
            return

        model = self.__close_model(item)
        project_remover.remove_project_files(model.project.main_file)

    def __close_model(self, item):
        model = item.data(0, QtCore.Qt.UserRole)

        if not model:
            return None

        ask_res = question_box.positive_answer(self,
                                               'Closing the project',
                                               f'Do you want to close the project {model.name}?')
        if not ask_res:
            return None

        self.close_model.emit(model)

        self.proj_explorer_tree.takeTopLevelItem(
            self.proj_explorer_tree.indexOfTopLevelItem(item))

        return model

    def __prepare_project_item_context_menu(self, point):
        # Infos about the node selected.
        selected_item = self.proj_explorer_tree.itemAt(point)

        if not selected_item:
            return

        if selected_item.Type == ProjectTreeViewItemType.PROJECT:
            maker = ProjectContextMenuMaker(selected_item)
            maker.on_delete_model.connect(self.__delete_model)
            maker.on_close_model.connect(self.__close_model)
            maker.on_edit_model.connect(self.__edit_model)
            maker.on_clone_model.connect(self.__clone_model)
            menu = maker.get_menu()
            point.setY(point.y() + 60)
            menu.exec_(self.mapToGlobal(point))

    def __read_settings(self):
        self.settings = QtCore.QSettings(prog.ORGANIZATION, prog.PRODUCT_NAME)

    def __edit_model(self, item: QtWidgets.QTreeWidgetItem):
        model = item.data(0, QtCore.Qt.UserRole)

        if not model:
            return

        input_diag = QtWidgets.QInputDialog()

        project_name, status = input_diag.getText(
            self, 'Project name', 'Please, insert project name' + 20 * ' ')

        if not status:
            return

        model.name = project_name
        item.setText(0, project_name)

    def __clone_model(self, item: QtWidgets.QTreeWidgetItem):
        """
        Clone model

        Args:
            item (QtWidgets.QTreeWidgetItem): _description_
        """
        model = item.data(0, QtCore.Qt.UserRole)

        if not model:
            return

        # ask to clone
        ask_result = question_box.positive_answer(self,
                                                  'Cloning the project',                                                  
                                                  f'Do you want to clone the project {model.name}?')
        if not ask_result:
            return

        dialog = ProjectCloneInputDialog(self)
        if dialog.exec():
            new_path, new_name = dialog.get_inputs()
        
        # project_cloner.remove_project_files(model.project.main_file)
