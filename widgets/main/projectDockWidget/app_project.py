import os

from PySide6.QtCore import QPoint
from PySide6.QtGui import Qt, QAction, QCursor
from PySide6.QtWidgets import QWidget, QFileSystemModel, QMenu, QMessageBox
from PySide6 import QtCore

# from widgets.mainWindow.mainWindow import MainWindow
from widgets.main.newProjectWidget.NewProjectDlg import NewProjectDlg
from widgets.main.projectDockWidget.ui.project_content import Ui_Project


class Project(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Project()
        self.ui.setupUi(self)

        # 设定Model展示的内容
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        # 过滤工作
        self.model.setFilter(QtCore.QDir.Dirs|QtCore.QDir.Files|QtCore.QDir.NoDotAndDotDot)
        # self.model.setNameFilters(["*.afc"])
        self.model.setNameFilterDisables(True)

        self.ui.treeView.setModel(self.model)

        # treeView的基本设置
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(20)
        self.ui.treeView.setSortingEnabled(False)
        self.ui.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView.customContextMenuRequested[QPoint].connect(self.the_widget_menu)

        # 隐藏表头 1=隐藏 0=显示
        self.ui.treeView.setHeaderHidden(1)
        # 隐藏文件大小、类型、日期列
        self.ui.treeView.setColumnHidden(1, True)
        self.ui.treeView.setColumnHidden(2, True)
        self.ui.treeView.setColumnHidden(3, True)

    def the_widget_menu(self, point):
        popMenu = QMenu()
        popMenu.addAction(QAction(u'新建', self, triggered=self.add))
        popMenu.addAction(QAction(u'删除', self, triggered=self.remove))
        popMenu.exec_(QCursor.pos())

    def add(self):
        index = self.ui.treeView.currentIndex()
        filepath = self.showPath(index)
        file_dir = os.path.dirname(filepath)
        mainWindow = self.parentWidget().parentWidget()
        dlg = NewProjectDlg(mainWindow)
        dlg.folder_path = file_dir
        dlg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dlg.created.connect(mainWindow.create_new_project)
        dlg.exec()

    def remove(self):
        index = self.ui.treeView.currentIndex()
        filepath = self.showPath(index)
        filename = self.showFileName(index)
        result = self.confirmBox(f"删除 <{filename}> ")
        mainWindow = self.parentWidget().parentWidget()
        tab_numb = mainWindow.ui.mainContent.count()
        if result:
            for i in range(0, tab_numb):
                if mainWindow.ui.mainContent.widget(i).property("full_path") == filepath:
                    mainWindow.close_tab(i)
            os.remove(filepath)

    # 读取设置路径-也就是项目所在文件夹
    def setPath(self, path):
        self.ui.treeView.setRootIndex(self.model.index(path))

    def showPath(self, index):
        return self.model.fileInfo(index).absoluteFilePath()

    def showFileName(self, index):
        return self.model.fileInfo(index).fileName()

    def showExtension(self, index):
        return self.model.fileInfo(index).suffix()

    def isFile(self, index):
        return self.model.fileInfo(index).isFile()

    def confirmBox(self, text):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('确认窗口')
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.setInformativeText('注意：删除后不可恢复！')
        msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msgBox.setButtonText(QMessageBox.Cancel, "取消")
        msgBox.setButtonText(QMessageBox.Ok, "确定")
        msgBox.setEscapeButton(QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Cancel)
        retval = msgBox.exec_()
        # Cancel = 4194304
        # Ok = 1024
        if retval == 1024:
            # user confirmed
            return True
        # anything else than OK
        return False