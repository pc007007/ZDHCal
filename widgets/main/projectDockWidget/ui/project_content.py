# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_content.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QSizePolicy,
    QTreeView, QVBoxLayout, QWidget)

class Ui_Project(object):
    def setupUi(self, Project):
        if not Project.objectName():
            Project.setObjectName(u"Project")
        Project.resize(238, 197)
        self.verticalLayout = QVBoxLayout(Project)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Project)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	border:1px solid rgb(204,206,219);\n"
"	border-top: 0px solid black;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.treeView = QTreeView(self.frame)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"QTreeView{\n"
"	background-color: rgb(245, 245, 245);\n"
"}")
        self.treeView.setFrameShape(QFrame.StyledPanel)
        self.treeView.setFrameShadow(QFrame.Raised)
        self.treeView.setTabKeyNavigation(False)
        self.treeView.setIconSize(QSize(16, 16))
        self.treeView.setUniformRowHeights(True)

        self.verticalLayout_2.addWidget(self.treeView)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Project)

        QMetaObject.connectSlotsByName(Project)
    # setupUi

    def retranslateUi(self, Project):
        Project.setWindowTitle(QCoreApplication.translate("Project", u"Form", None))
    # retranslateUi

