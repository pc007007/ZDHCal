# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecentContent.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_RecentContentLink(object):
    def setupUi(self, RecentContentLink):
        if not RecentContentLink.objectName():
            RecentContentLink.setObjectName(u"RecentContentLink")
        RecentContentLink.resize(270, 60)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecentContentLink.sizePolicy().hasHeightForWidth())
        RecentContentLink.setSizePolicy(sizePolicy)
        RecentContentLink.setMinimumSize(QSize(270, 60))
        RecentContentLink.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(10)
        RecentContentLink.setFont(font)
        RecentContentLink.setStyleSheet(u"QPushButton#pushButton_rcl{\n"
"	border: 0px solid black;\n"
"	margin-left: 8px;\n"
"}\n"
"QPushButton#pushButton_rcl_2{\n"
"	padding: 0px;\n"
"	margin-left: 10px;\n"
"	margin-right: 10px;\n"
"	border: 0px solid black;\n"
"}\n"
"QPushButton#pushButton_rcl_2:hover{\n"
"	border: 0px solid black;\n"
"	background-color: rgba(14,112,192,1);\n"
"}\n"
"QPushButton#pushButton_rcl_2:checked{\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgba(79,79,79,1)\n"
"}\n"
"\n"
"QWidget#RecentContentLink:hover{\n"
"	background-color: rgba(201,222,245,1);\n"
"}\n"
"QWidget#RecentContentLink:pressed, QLabel:pressed{\n"
"	color: white;\n"
"	background-color: rgba(0,122,204,1);\n"
"}\n"
"QWidget#RecentContentLink{\n"
"	border: 0px solid black;\n"
"}\n"
"\n"
"QWidget#RecentContentLink:disabled{\n"
"	background-color: rgba(0,0,0,0.05);\n"
"}\n"
"\n"
"QToolButton#toolButton{\n"
"	margin:0px;\n"
"	padding:0px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(RecentContentLink)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_rcl = QToolButton(RecentContentLink)
        self.toolButton_rcl.setObjectName(u"toolButton_rcl")
        icon = QIcon()
        icon.addFile(u":/resource/AFCFile_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_rcl.setIcon(icon)
        self.toolButton_rcl.setIconSize(QSize(24, 24))
        self.toolButton_rcl.setAutoRaise(True)

        self.horizontalLayout.addWidget(self.toolButton_rcl)

        self.pushButton_rcl = QPushButton(RecentContentLink)
        self.pushButton_rcl.setObjectName(u"pushButton_rcl")
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton_rcl.setFont(font1)
        self.pushButton_rcl.setIconSize(QSize(24, 24))
        self.pushButton_rcl.setAutoRepeat(False)
        self.pushButton_rcl.setAutoRepeatInterval(100)
        self.pushButton_rcl.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_rcl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.time_label = QLabel(RecentContentLink)
        self.time_label.setObjectName(u"time_label")

        self.horizontalLayout.addWidget(self.time_label)

        self.pushButton_rcl_2 = QPushButton(RecentContentLink)
        self.pushButton_rcl_2.setObjectName(u"pushButton_rcl_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_rcl_2.sizePolicy().hasHeightForWidth())
        self.pushButton_rcl_2.setSizePolicy(sizePolicy1)
        self.pushButton_rcl_2.setMinimumSize(QSize(0, 0))
        self.pushButton_rcl_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_rcl_2.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/resource/PushpinUnpin_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/resource/Pushpin_16x.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_rcl_2.setIcon(icon1)
        self.pushButton_rcl_2.setIconSize(QSize(16, 16))
        self.pushButton_rcl_2.setCheckable(True)
        self.pushButton_rcl_2.setChecked(False)
        self.pushButton_rcl_2.setAutoRepeat(False)
        self.pushButton_rcl_2.setAutoExclusive(False)
        self.pushButton_rcl_2.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_rcl_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(33, 24, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_rcl = QLabel(RecentContentLink)
        self.label_rcl.setObjectName(u"label_rcl")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.label_rcl.setFont(font2)
        self.label_rcl.setInputMethodHints(Qt.ImhNone)
        self.label_rcl.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_rcl)

        self.horizontalSpacer_3 = QSpacerItem(26, 24, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(RecentContentLink)

        QMetaObject.connectSlotsByName(RecentContentLink)
    # setupUi

    def retranslateUi(self, RecentContentLink):
        RecentContentLink.setWindowTitle(QCoreApplication.translate("RecentContentLink", u"Form", None))
        self.toolButton_rcl.setText(QCoreApplication.translate("RecentContentLink", u"...", None))
        self.pushButton_rcl.setText(QCoreApplication.translate("RecentContentLink", u"\u6d4b\u8bd5\u9879\u76ee01.afc", None))
#if QT_CONFIG(shortcut)
        self.pushButton_rcl.setShortcut(QCoreApplication.translate("RecentContentLink", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.time_label.setText(QCoreApplication.translate("RecentContentLink", u"2021/3/21 4:24", None))
        self.pushButton_rcl_2.setText("")
        self.label_rcl.setText(QCoreApplication.translate("RecentContentLink", u"C:Userspc080OneDrive1Pyside\u5929\u6d251\u53f7\u7ebf\u6d4b\u8bd5\u9879\u76ee01111111111111.afc", None))
    # retranslateUi

