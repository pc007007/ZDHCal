# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_title_widget.ui'
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

class Ui_mainTitleWidget(object):
    def setupUi(self, mainTitleWidget):
        if not mainTitleWidget.objectName():
            mainTitleWidget.setObjectName(u"mainTitleWidget")
        mainTitleWidget.resize(606, 32)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainTitleWidget.sizePolicy().hasHeightForWidth())
        mainTitleWidget.setSizePolicy(sizePolicy)
        mainTitleWidget.setMinimumSize(QSize(0, 32))
        mainTitleWidget.setMaximumSize(QSize(16777215, 34))
        mainTitleWidget.setStyleSheet(u"QWidget#mainTitleWidget{\n"
"	border: 0px solid black;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 0px;\n"
"    text-decoration: none;\n"
"    border: 0px solid white;\n"
"}\n"
"QPushButton:checked {\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: black;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: grey;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(201,222,245);\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0,122,204);\n"
"	color:white\n"
"}")
        self.verticalLayout = QVBoxLayout(mainTitleWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_btn = QPushButton(mainTitleWidget)
        self.logo_btn.setObjectName(u"logo_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.logo_btn.sizePolicy().hasHeightForWidth())
        self.logo_btn.setSizePolicy(sizePolicy1)
        self.logo_btn.setMinimumSize(QSize(48, 32))
        self.logo_btn.setMaximumSize(QSize(48, 32))
        self.logo_btn.setAutoFillBackground(False)
        self.logo_btn.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid black;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/resource/EDI-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_btn.setIcon(icon)
        self.logo_btn.setIconSize(QSize(24, 24))
        self.logo_btn.setCheckable(True)
        self.logo_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.logo_btn)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, -1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.title_btn = QPushButton(mainTitleWidget)
        self.title_btn.setObjectName(u"title_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.title_btn.sizePolicy().hasHeightForWidth())
        self.title_btn.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.title_btn.setFont(font)
        self.title_btn.setStyleSheet(u"QPushButton#title_btn{\n"
"	background-color: rgb(224,227,230);\n"
"	padding-right: 10px;\n"
"	padding-left: 10px;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"}")

        self.horizontalLayout.addWidget(self.title_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.min_btn = QPushButton(mainTitleWidget)
        self.min_btn.setObjectName(u"min_btn")
        sizePolicy1.setHeightForWidth(self.min_btn.sizePolicy().hasHeightForWidth())
        self.min_btn.setSizePolicy(sizePolicy1)
        self.min_btn.setMinimumSize(QSize(48, 32))
        self.min_btn.setMaximumSize(QSize(48, 32))
        self.min_btn.setAutoFillBackground(False)
        self.min_btn.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/resource/ChromeMinimize_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.min_btn.setIcon(icon1)
        self.min_btn.setCheckable(True)
        self.min_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.min_btn)

        self.full_btn = QPushButton(mainTitleWidget)
        self.full_btn.setObjectName(u"full_btn")
        sizePolicy1.setHeightForWidth(self.full_btn.sizePolicy().hasHeightForWidth())
        self.full_btn.setSizePolicy(sizePolicy1)
        self.full_btn.setMinimumSize(QSize(48, 32))
        self.full_btn.setMaximumSize(QSize(48, 32))
        self.full_btn.setAutoFillBackground(False)
        self.full_btn.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/resource/ChromeMaximize_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.full_btn.setIcon(icon2)
        self.full_btn.setCheckable(True)
        self.full_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.full_btn)

        self.close_btn = QPushButton(mainTitleWidget)
        self.close_btn.setObjectName(u"close_btn")
        sizePolicy1.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy1)
        self.close_btn.setMinimumSize(QSize(48, 32))
        self.close_btn.setMaximumSize(QSize(48, 32))
        self.close_btn.setLayoutDirection(Qt.LeftToRight)
        self.close_btn.setAutoFillBackground(False)
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid black;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/resource/ChromeClose_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_btn.setIcon(icon3)
        self.close_btn.setCheckable(True)
        self.close_btn.setFlat(True)

        self.horizontalLayout.addWidget(self.close_btn)

        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(mainTitleWidget)

        QMetaObject.connectSlotsByName(mainTitleWidget)
    # setupUi

    def retranslateUi(self, mainTitleWidget):
        mainTitleWidget.setWindowTitle(QCoreApplication.translate("mainTitleWidget", u"Form", None))
        self.logo_btn.setText("")
        self.title_btn.setText(QCoreApplication.translate("mainTitleWidget", u"\u5f00\u59cb", None))
#if QT_CONFIG(tooltip)
        self.min_btn.setToolTip(QCoreApplication.translate("mainTitleWidget", u"\u6700\u5c0f\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.min_btn.setText("")
#if QT_CONFIG(tooltip)
        self.full_btn.setToolTip(QCoreApplication.translate("mainTitleWidget", u"\u6700\u5927\u5316", None))
#endif // QT_CONFIG(tooltip)
        self.full_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("mainTitleWidget", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
    # retranslateUi

