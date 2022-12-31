"""
qt lappy main view
"""


from PyQt5 import QtWidgets, QtCore, QtGui


from src.models.lapmodel import LapModel
from src.utils.helpers import dir_helper
from src.services import project_remover_service


from gui import prog
from gui.views.uis.ui_qtlapview import UIQtLapView
from gui.services import lapproject_service
from gui.services.project_contextmenu_maker import ProjectContextMenuMaker
from gui.models.loglevelenum import LogLevelEnum
from gui.utils.helpers import question_box, qtreewidgetitem_helper
from gui.models.project_treeview_item_type import ProjectTreeViewItemType
from gui.views.mapplotview import MapPlotView


class QtLapView(QtWidgets.QMainWindow, UIQtLapView):
    """
    view
    """

    create_empty_project = QtCore.pyqtSignal(str, str)
    log_message = QtCore.pyqtSignal(str, LogLevelEnum)
    delete_model = QtCore.pyqtSignal(LapModel)

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setup_ui(self)
        self.__connect()
        self.__readSettings()

    def add_project_to_projects_view(self, model: LapModel):
        item = lapproject_service.to_tree_widget_item(model)
        if item is not None:
            self.proj_explorer_tree.addTopLevelItem(item)

    def __add_tab(self, widget: QtWidgets.QWidget, name: str):
        """
        add tab to pages
        """
        self.central_widget.addTab(widget, name)

    def __connect(self):
        self.new_project_action.triggered.connect(self.__on_new_project_create)
        self.proj_explorer_tree.customContextMenuRequested.connect(
            self.__prepareProjectItemContextMenu)
        self.proj_explorer_tree.itemClicked.connect(self.__on_item_clicked)

    @QtCore.pyqtSlot(QtWidgets.QTreeWidgetItem, int)
    def __on_item_clicked(self, item, column):
        if not item:
            return

        plot = MapPlotView()
        self.__add_tab(plot, item.text(column))

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
                project_remover_service.remove_projects_in_dir(project_folder)

        self.settings.setValue('new_project_last_dir', project_folder)

        input = QtWidgets.QInputDialog()
        input.setWhatsThis('test')

        project_name, status = input.getText(
            self, 'Project name', 'Please, insert project name')

        if not status:
            return

        self.create_empty_project.emit(project_folder, project_name)

    def __delete_model(self, item):
        model = self.__close_model(item)
        project_remover_service.remove_project_files(model.project.main_file)

    def __close_model(self, item):
        model = item.data(0, QtCore.Qt.UserRole)

        if not model:
            return

        self.delete_model.emit(model)

        self.proj_explorer_tree.takeTopLevelItem(
            self.proj_explorer_tree.indexOfTopLevelItem(item))

        return model

    def __prepareProjectItemContextMenu(self, point):
        # Infos about the node selected.
        selected_item = self.proj_explorer_tree.itemAt(point)

        if not selected_item:
            return

        if selected_item.Type == ProjectTreeViewItemType.PROJECT:
            maker = ProjectContextMenuMaker(selected_item)
            maker.on_delete_model.connect(self.__delete_model)
            maker.on_close_model.connect(self.__close_model)
            menu = maker.get_menu()
            point.setY(point.y() + 60)
            menu.exec_(self.mapToGlobal(point))

        # if not project_item.Type == ProjectTreeViewItemType

        # item = self.proj_explorer_tree.itemAt(point)
        # name = item.text(0)  # The text of the node.
        # tp = item.Type  # type(item.Type) //.__name__

        # if tp == ProjectItemType.BOUND:
        #     self.__boundContextMenu()

        # self.log_message(f'context menu for {name} with type = {tp}',
        #                  LogLevelEnum.info)

    # def __boundContextMenu(self):
    #     menu = QtWidgets.QMenu(self)
    #     createAction = menu.addAction('Create')
    #     createAction.triggered.connect(self.__createBound)
    #     menu.popup(QtGui.QCursor.pos())

    def __readSettings(self):
        self.settings = QtCore.QSettings(prog.ORGANIZATION, prog.PRODUCT_NAME)
