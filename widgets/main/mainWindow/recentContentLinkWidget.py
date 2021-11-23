import os

from PySide6 import QtCore
from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QCursor, QAction, QIcon, Qt
from PySide6.QtWidgets import QPushButton, QWidget, QMenu, QApplication

from widgets.main.mainWindow.ui.RecentContent import Ui_RecentContentLink


class RecentContentLink(QPushButton):
    # clickedbtn = Signal()

    def __init__(self, file_path, time):
        super(RecentContentLink, self).__init__()
        self.ui = Ui_RecentContentLink()
        self.ui.setupUi(self)

        self._file_path = file_path
        self._title_with_extension = os.path.split(file_path)[-1]
        self._title = os.path.split(file_path)[-1].split('.')[0]
        self._path_folder = os.path.dirname(file_path)
        self._open_time = time

        self.ui.pushButton_rcl.setText(self._title_with_extension)
        self.ui.label_rcl.setText(self._path_folder)
        self.ui.time_label.setText(self._open_time)

        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.create_rightmenu)
        self.ui.pushButton_rcl_2.toggled.connect(self.slot_pin_state_changed)
        self.ui.pushButton_rcl.clicked.connect(self.clicked)

        self.ui.toolButton_rcl.setDisabled(False)

    def getFileName(self):
        return self._title_with_extension

    def getFileNameWithExtension(self):
        return self._title

    def getOpenTime(self):
        return self._open_time

    def getPinStatus(self) -> bool:
        return self.ui.pushButton_rcl_2.isChecked()

    def getFilePath(self):
        return self._file_path

    def setPinStatus(self, checked: bool):
        self.ui.pushButton_rcl_2.setChecked(checked)

    def text(self) -> str:
        return self._file_path

    def create_rightmenu(self):
        # 菜单对象
        groupBox_menu = QMenu(self)
        action_delete = QAction(QIcon(':/resource/DeTableRow_16x.svg'), u'从列表中删除', self)
        action_pin = QAction(QIcon(':/resource/PushpinUnpin_16x.svg'), u'将此项目固定到列表', self)
        action_copy = QAction(QIcon(':/resource/Copy_16x.svg'), u'复制路径', self)
        groupBox_menu.addAction(action_delete)
        groupBox_menu.addAction(action_pin)
        groupBox_menu.addAction(action_copy)

        action_delete.triggered.connect(self.slot_delete_item)
        action_pin.triggered.connect(self.slot_pin_item)
        action_copy.triggered.connect(self.slot_copy_path)

        # 声明当鼠标在groupBox控件上右击时，在鼠标位置显示右键菜单   ,exec_,popup两个都可以
        groupBox_menu.popup(QCursor.pos())

    @Slot()
    def slot_delete_item(self):
        self.deleteLater()

    @Slot()
    def slot_pin_item(self):
        self.setPinStatus(True)

    @Slot()
    def slot_copy_path(self):
        mainWindow = self.parent().parent().parent().parent().parent().parent().parent().parent().parent().parent()
        clip = QApplication.clipboard()
        clip.setText(self._file_path)
        mainWindow.ui.statusbar.showMessage("已复制", 2000)

    @Slot()
    def slot_pin_state_changed(self, checked):
        mainWindow = self.parent().parent().parent().parent().parent().parent().parent().parent().parent().parent()
        if checked:
            mainWindow.ui.verticalLayout_9.insertWidget(0, self)
        else:
            mainWindow.ui.verticalLayout_7.insertWidget(0, self)


