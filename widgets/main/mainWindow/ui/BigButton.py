# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BigButton.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_BigButton(object):
    def setupUi(self, BigButton):
        if not BigButton.objectName():
            BigButton.setObjectName(u"BigButton")
        BigButton.resize(340, 75)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BigButton.sizePolicy().hasHeightForWidth())
        BigButton.setSizePolicy(sizePolicy)
        BigButton.setMinimumSize(QSize(340, 75))
        BigButton.setMaximumSize(QSize(340, 75))
        BigButton.setStyleSheet(u"QWidget#BigButton{\n"
"	background-color: rgb(238, 235, 235);\n"
"	border: 0px solid black;\n"
"}\n"
"QWidget#BigButton:hover{\n"
"	background-color: rgb(201, 222, 245);\n"
"}\n"
"QWidget#BigButton:selection{\n"
"	background-color: rgb(217, 224, 248);\n"
"}\n"
"QPushButton#icon_button{\n"
"	margin:0px;\n"
"	margin-left: 6px;\n"
"	margin-right: 6px;\n"
"}\n"
"QLabel#description_label_01,#description_label_02{\n"
"	color: rgb(79, 79, 79);\n"
"}")
        self.verticalLayout = QVBoxLayout(BigButton)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.icon_button = QPushButton(BigButton)
        self.icon_button.setObjectName(u"icon_button")
        icon = QIcon()
        icon.addFile(u":/resource/OpenFolder_16x-o.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_button.setIcon(icon)
        self.icon_button.setIconSize(QSize(32, 32))
        self.icon_button.setFlat(True)

        self.verticalLayout_4.addWidget(self.icon_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.title_label = QLabel(BigButton)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: rgb(30, 30, 30);")

        self.verticalLayout_5.addWidget(self.title_label)

        self.description_label_01 = QLabel(BigButton)
        self.description_label_01.setObjectName(u"description_label_01")
        self.description_label_01.setStyleSheet(u"color: rgb(79, 79, 79);")

        self.verticalLayout_5.addWidget(self.description_label_01)

        self.description_label_02 = QLabel(BigButton)
        self.description_label_02.setObjectName(u"description_label_02")
        self.description_label_02.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.description_label_02)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(BigButton)

        QMetaObject.connectSlotsByName(BigButton)
    # setupUi

    def retranslateUi(self, BigButton):
        BigButton.setWindowTitle(QCoreApplication.translate("BigButton", u"Form", None))
        self.icon_button.setText("")
        self.title_label.setText(QCoreApplication.translate("BigButton", u"Title", None))
        self.description_label_01.setText("")
        self.description_label_02.setText("")
    # retranslateUi

