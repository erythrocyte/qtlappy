import pyqt5ac

pyqt5ac.main(uicOptions='--from-imports', force=False, initPackage=True,
             ioPaths=[
                 ['gui/resources/*.qrc', 'gui/resources/__init__.py']
                 ])
