# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_frame.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindowFrame(object):
    def setupUi(self, MainWindowFrame):
        if not MainWindowFrame.objectName():
            MainWindowFrame.setObjectName(u"MainWindowFrame")
        MainWindowFrame.resize(635, 546)
        icon = QIcon()
        icon.addFile(u":/resource/EDI-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/resource/EDI-logo.svg", QSize(), QIcon.Normal, QIcon.On)
        MainWindowFrame.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindowFrame)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_mainwindow = QFrame(self.centralwidget)
        self.frame_mainwindow.setObjectName(u"frame_mainwindow")
        self.frame_mainwindow.setStyleSheet(u"QFrame#frame_mainwindow{\n"
"	border: 1px solid rgb(155,159,185);\n"
"}")
        self.frame_mainwindow.setFrameShape(QFrame.StyledPanel)
        self.frame_mainwindow.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_mainwindow)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.frame_mainwindow)

        MainWindowFrame.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowFrame)

        QMetaObject.connectSlotsByName(MainWindowFrame)
    # setupUi

    def retranslateUi(self, MainWindowFrame):
        MainWindowFrame.setWindowTitle(QCoreApplication.translate("MainWindowFrame", u"MainWindow", None))
    # retranslateUi

