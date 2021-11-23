# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statusWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_statusWidget(object):
    def setupUi(self, statusWidget):
        if not statusWidget.objectName():
            statusWidget.setObjectName(u"statusWidget")
        statusWidget.resize(165, 24)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(statusWidget.sizePolicy().hasHeightForWidth())
        statusWidget.setSizePolicy(sizePolicy)
        statusWidget.setMinimumSize(QSize(0, 0))
        statusWidget.setMaximumSize(QSize(16777215, 16777215))
        statusWidget.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QWidget#statusWidget{\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(statusWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.commandButton = QPushButton(statusWidget)
        self.commandButton.setObjectName(u"commandButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.commandButton.sizePolicy().hasHeightForWidth())
        self.commandButton.setSizePolicy(sizePolicy1)
        self.commandButton.setMinimumSize(QSize(30, 24))
        self.commandButton.setMaximumSize(QSize(30, 24))
        font = QFont()
        font.setPointSize(8)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.commandButton.setFont(font)
        self.commandButton.setStyleSheet(u"QPushButton {\n"
"    border-radius: 0px;\n"
"    color: white;\n"
"    text-decoration: none;\n"
"    background-color: transparent;\n"
"	padding:0px;\n"
"	margin:0px\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgba(201,222,245,0.4);\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: black;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: grey;\n"
"    border: 1px solid white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgba(201,222,245,0.4);\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgba(201,222,245,0.4);\n"
"	color:black;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/resource/AddImmediateWindow_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commandButton.setIcon(icon)
        self.commandButton.setIconSize(QSize(14, 14))
        self.commandButton.setFlat(False)

        self.horizontalLayout.addWidget(self.commandButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(statusWidget)

        QMetaObject.connectSlotsByName(statusWidget)
    # setupUi

    def retranslateUi(self, statusWidget):
        statusWidget.setWindowTitle(QCoreApplication.translate("statusWidget", u"Form", None))
        self.commandButton.setText("")
    # retranslateUi

