import math
import os.path
from time import strftime, localtime

from PySide6 import QtSvg, QtXml
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QByteArray, QSize, QPoint, Qt, QRect, QPropertyAnimation
from PySide6.QtGui import QMouseEvent, QEnterEvent, QPainter, QColor, QPen, QPainterPath, QBrush
from PySide6.QtWidgets import QWidget, QMainWindow, QStyle, QGraphicsDropShadowEffect

from widgets.main.mainWindow.mainWindow import MainWindow
from widgets.main.mainWindow.ui.main_window_frame import Ui_MainWindowFrame


class MainWindowFrame(QMainWindow):

    def __init__(self):
        super(MainWindowFrame, self).__init__()
        self.ui = Ui_MainWindowFrame()
        self.ui.setupUi(self)

        self.mainwindow = MainWindow()
        self.mainwindow.setFrame(self)
        self.ui.verticalLayout_3.addWidget(self.mainwindow)

        self.readSettings()
        self.mainwindow.ui.configWin.hide()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.writeSettings()
        print("保存配置文件")

    def writeSettings(self):
        settings = QtCore.QSettings("settings/settings.ini", QtCore.QSettings.IniFormat)

        settings.beginGroup("MainWindow")
        settings.setValue('geometry', self.saveGeometry())
        # In[] 保存最近打开信息:
        # step 1: 获取当前widget清单
        widget_count = self.mainwindow.ui.verticalLayout_7.count()
        recent_10_item_path = list()
        recent_10_item_time = list()
        for i in range(widget_count):
            btn = self.mainwindow.ui.verticalLayout_7.itemAt(i).widget()
            recent_10_item_path.append(btn.text())
            recent_10_item_time.append(btn.getOpenTime())
        # step 2: 保存widget清单到settings文件中
        settings.setValue('recent_10_item_path', recent_10_item_path)
        settings.setValue('recent_10_item_time', recent_10_item_time)
        # In[] 保存固定的项目信息:
        # step 1: 获取当前widget清单
        widget_count = self.mainwindow.ui.verticalLayout_9.count()
        recent_10_item_path_pin = list()
        recent_10_item_time_pin = list()
        for i in range(widget_count):
            btn = self.mainwindow.ui.verticalLayout_9.itemAt(i).widget()
            recent_10_item_path_pin.append(btn.text())
            recent_10_item_time_pin.append(btn.getOpenTime())
        # step 2: 保存widget清单到settings文件中
        settings.setValue('recent_10_item_path_pin', recent_10_item_path_pin)
        settings.setValue('recent_10_item_time_pin', recent_10_item_time_pin)
        settings.endGroup()

        self.lodDockWidgetSetting(settings, "Dock_project", self.mainwindow.ui.projWin)
        self.lodDockWidgetSetting(settings, "Dock_ouput", self.mainwindow.ui.dockWidget)
        self.lodDockWidgetSetting(settings, "Dock_afc_config", self.mainwindow.ui.configWin)

    def readSettings(self):
        settings = QtCore.QSettings("settings/settings.ini", QtCore.QSettings.IniFormat)

        settings.beginGroup("MainWindow")
        self.restoreGeometry(settings.value('geometry'))
        recent_10_item_path = settings.value('recent_10_item_path', ["c:/app/blank.afc", "c:/app/blank.afc"])
        current_time = strftime('%Y-%m-%d %H:%M', localtime())
        recent_10_item_time = settings.value('recent_10_item_time', [current_time, current_time])
        n = 0
        for file_path in recent_10_item_path:
            btn = self.mainwindow.createRecntFilePathBtn(file_path, recent_10_item_time[n])
            self.mainwindow.ui.verticalLayout_7.addWidget(btn)
            if btn.text() == "c:/app/blank.afc":
                btn.hide()
            n = n + 1
        # In[] 读取固定的项目信息:
        # step 1: 获取当前setting中的最近固定项目
        recent_10_item_path_pin = settings.value('recent_10_item_path_pin', ["c:/app/blank.afc", "c:/app/blank.afc"])
        recent_10_item_time_pin = settings.value('recent_10_item_time_pin', ["2021-08-04", "2021-08-04"])
        n = 0
        for file_path in recent_10_item_path_pin:
            btn = self.mainwindow.createRecntFilePathBtn(file_path, recent_10_item_time_pin[n])
            self.mainwindow.ui.verticalLayout_9.addWidget(btn)
            btn.setPinStatus(True)
            if btn.text() == "c:/app/blank.afc":
                btn.hide()
            n = n + 1
        settings.endGroup()

        self.readDockWidgetSetting(settings, "Dock_project", self.mainwindow.ui.projWin)
        self.readDockWidgetSetting(settings, "Dock_ouput", self.mainwindow.ui.dockWidget)
        self.readDockWidgetSetting(settings, "Dock_afc_config", self.mainwindow.ui.configWin)

    def readDockWidgetSetting(self, settings, title, dock):
        settings.beginGroup(title)
        dock.setHidden(settings.value('hidden', 'false') == "true")

        if settings.value('area') is not None:
            self.mainwindow.addDockWidget(Qt.DockWidgetArea(int(settings.value('area'))), dock)
        self.mainwindow.resizeDocks([dock], [int(settings.value('width', 200))], Qt.Horizontal)
        self.mainwindow.resizeDocks([dock], [int(settings.value('height', 200))], Qt.Vertical)
        settings.endGroup()

    def lodDockWidgetSetting(self, settings, title, dock):
        settings.beginGroup(title)
        settings.setValue('hidden', dock.isHidden())
        settings.setValue('area', self.mainwindow.dockWidgetArea(dock))
        settings.setValue('width', dock.width())
        settings.setValue('height', dock.height())
        settings.endGroup()
