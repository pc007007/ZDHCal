# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myDockTitleWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QToolButton, QWidget)
import resources_rc

class Ui_myDockTitleWidget(object):
    def setupUi(self, myDockTitleWidget):
        if not myDockTitleWidget.objectName():
            myDockTitleWidget.setObjectName(u"myDockTitleWidget")
        myDockTitleWidget.resize(318, 20)
        myDockTitleWidget.setMinimumSize(QSize(0, 20))
        myDockTitleWidget.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(8)
        myDockTitleWidget.setFont(font)
        myDockTitleWidget.setStyleSheet(u"QLabel#label{\n"
"	background-image: url(:/resource/handler-h.svg);\n"
"	margin: 5px;\n"
"}\n"
"QWidget#myDockTitleWidget{\n"
"	background-color: rgb(238,238,242);\n"
"}\n"
"\n"
"QPushButton#closeBtn{\n"
"	background-color: rgb(238,238,242)\n"
"}\n"
"\n"
"QPushButton#closeBtn:hover{\n"
"	background-color: rgba(255, 255, 255,0.5)\n"
"}\n"
"\n"
"\n"
"QFrame#frame_dock_title{\n"
"background-color: transparent;\n"
"border:1px solid rgb(204,206,219);\n"
"border-bottom:0px solid rgb(204,206,219);\n"
"margin-left:0px;\n"
"margin-right:0px;\n"
"margin-bottom:0px;\n"
"padding-right:5px;\n"
"padding-left:5px;\n"
"}\n"
"\n"
"\n"
"QScrollArea#scrollArea{\n"
"	background-color: rgb(238,238,242);\n"
"}\n"
"\n"
"QLabel#line{\n"
"	background-color: rgb(238,238,242);\n"
"	color: rgb(150,150,150);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(myDockTitleWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_dock_title = QFrame(myDockTitleWidget)
        self.frame_dock_title.setObjectName(u"frame_dock_title")
        self.frame_dock_title.setMaximumSize(QSize(16777215, 20))
        self.frame_dock_title.setStyleSheet(u"")
        self.frame_dock_title.setFrameShape(QFrame.StyledPanel)
        self.frame_dock_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_dock_title)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.frame_dock_title)
        self.title.setObjectName(u"title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.title)

        self.label = QLabel(self.frame_dock_title)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_3.addWidget(self.label)

        self.flotBtn = QToolButton(self.frame_dock_title)
        self.flotBtn.setObjectName(u"flotBtn")
        icon = QIcon()
        icon.addFile(u":/resource/Undock_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.flotBtn.setIcon(icon)
        self.flotBtn.setIconSize(QSize(12, 12))
        self.flotBtn.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.flotBtn)

        self.closeBtn = QToolButton(self.frame_dock_title)
        self.closeBtn.setObjectName(u"closeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/resource/Close_16x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon1)
        self.closeBtn.setIconSize(QSize(12, 14))
        self.closeBtn.setAutoRaise(True)

        self.horizontalLayout_3.addWidget(self.closeBtn)


        self.horizontalLayout.addWidget(self.frame_dock_title)


        self.retranslateUi(myDockTitleWidget)

        QMetaObject.connectSlotsByName(myDockTitleWidget)
    # setupUi

    def retranslateUi(self, myDockTitleWidget):
        myDockTitleWidget.setWindowTitle(QCoreApplication.translate("myDockTitleWidget", u"Form", None))
        self.title.setText(QCoreApplication.translate("myDockTitleWidget", u"\u6807\u9898", None))
        self.label.setText("")
        self.flotBtn.setText(QCoreApplication.translate("myDockTitleWidget", u"...", None))
        self.closeBtn.setText(QCoreApplication.translate("myDockTitleWidget", u"...", None))
    # retranslateUi

