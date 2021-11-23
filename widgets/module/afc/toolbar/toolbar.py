import os

from PySide6.QtGui import Qt, QIcon, QAction
from PySide6.QtWidgets import QWidget, QHBoxLayout, QToolButton, QMenu

# from widgets.main.mainWindow.mainWindow import MainWindow
from widgets.qss import Qss


class AFCToolBar(QWidget):
    def __init__(self, parent = None):
    # def __init__(self, parent:MainWindow=None):
        super(AFCToolBar, self).__init__()

        self.mainwindow = parent

        self.setObjectName('toolbar_afc')
        self.setContentsMargins(0, 0, 0, 0)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.toolbutton_run = QToolButton()
        self.toolbutton_run.setStyleSheet(Qss().button)
        self.toolbutton_run.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolbutton_run.setText("运行")
        self.toolbutton_run.setIcon(QIcon(':/resource/Run_16x.svg'))
        self.layout.addWidget(self.toolbutton_run)

        self.toolbutton_run.clicked.connect(self.mainwindow.runCal)

