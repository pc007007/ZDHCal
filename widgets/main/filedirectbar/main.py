import os

from PySide6 import QtCore
from PySide6.QtCore import Slot, Signal, QSortFilterProxyModel
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton, QToolButton, QMenu, QWidgetAction, \
    QFileSystemModel, QTreeView, QListView, QSizePolicy, QVBoxLayout

from widgets.qss import Qss

qss = Qss(style='default')


class FileDirectoryBar(QWidget):
    pathChanged = Signal(str)

    def __init__(self, filepath, parent=None):
        super(FileDirectoryBar, self).__init__()

        self.mainwindow = parent
        self.setContentsMargins(10, 0, 0, 0)
        self._filepath = filepath
        self._whole_list = {}

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setup_button_list()

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, path):
        self._filepath = path
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().deleteLater()
        self.setup_button_list()
        self.pathChanged.emit(path)

    def setup_button_list(self):
        icon_button = QPushButton()
        icon_button.setIcon(QIcon(':/resource/FolderClosed_16x.svg'))
        icon_button.setStyleSheet(qss.button)
        self.layout.addWidget(icon_button)
        path_list = self._filepath.split('/')
        current_path = ''
        for i, folder_name in enumerate(path_list):
            path_button = QPushButton()
            path_button.setText(folder_name)
            # path_button.setIcon(QIcon(':/resource/FolderClosed_16x.svg'))
            path_button.setStyleSheet(qss.button)

            path_button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
            self.layout.addWidget(path_button)

            current_path = f'{current_path}/{folder_name}'
            self._whole_list[folder_name] = current_path[1:]
            path_button.clicked.connect(self.update_path)

            expand_button = QToolButton()
            expand_button.setIcon(QIcon(':/resource/ExpandRight_16x.svg'))
            expand_button.setStyleSheet(qss.toolButton_fileDirectory)
            menu = QMenu()
            menu.setStyleSheet(qss.menu)

            expand_button.clicked.connect(
                lambda *args, btn=expand_button, menux=menu, x=current_path[1:]: self.show_menu(btn, menux, x))
            self.layout.addWidget(expand_button)

    @Slot()
    def update_path(self):
        path_button = self.sender()
        path = self._whole_list[path_button.text()]
        self.filepath = path

    @Slot()
    def show_menu(self, button, menu, path):
        menu.clear()
        action = QWidgetAction(self)
        model = QFileSystemModel()
        model.setRootPath(path)
        model.setFilter(QtCore.QDir.Dirs | QtCore.QDir.NoDotAndDotDot)

        content = QListView()
        content.setContentsMargins(0, 0, 0, 0)
        content.setStyleSheet(qss.listView_fileDirectory)
        content.setModel(model)
        content.setRootIndex(model.index(path))
        content.clicked.connect(lambda index: update(self, index, menu))

        def update(self, index, menu):
            self.filepath = f"{path}/{index.data()}"
            menu.close()

        action.setDefaultWidget(content)
        menu.addAction(action)
        menu.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        button.setMenu(menu)
        button.showMenu()
