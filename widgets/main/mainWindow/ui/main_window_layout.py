# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_layout.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTabWidget, QTextEdit,
    QToolBar, QToolButton, QVBoxLayout, QWidget)

from widgets.main.mainWindow.ui.ToolBar import ToolBar
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(916, 767)
        MainWindow.setFocusPolicy(Qt.NoFocus)
        MainWindow.setStyleSheet(u"QToolBar::handle{\n"
"	background-image: url(:/resource/handler.svg);\n"
"}\n"
"QMainWindow#MainWindow{\n"
"	background-color: rgb(238, 238, 242);\n"
"}\n"
"\n"
"QTextEdit#textEdit{\n"
"	background-color: rgb(240, 240, 240);\n"
"}\n"
"QDockWidget {\n"
"	color: black;\n"
"	margin-bottom:5px;\n"
"	border:1px solid black;\n"
"}\n"
"\n"
"QDockWidget:unchecked {\n"
"	color: rgb(0, 255, 0);\n"
"}\n"
"\n"
"QDockWidget::title {\n"
"    text-align: left;\n"
"	color: white;\n"
"    /*background-color: rgb(0, 122, 204);*/\n"
"	background-color:rgb(238,238,242);\n"
"	padding-left:5px;\n"
"	padding-right:5px;\n"
"	border: 1px solid rgb(204,206,219);\n"
"	margin-left:5px;\n"
"	margin-right:5px;\n"
"	margin-bottom:-1px;\n"
"}\n"
"\n"
"QDockWidget::close-button{\n"
"}\n"
"\n"
"QMainWindow::separator {\n"
"	width: 10px;\n"
"	height: 0px;\n"
"	margin: 0px;\n"
"	padding: 0px,1px;\n"
"}\n"
"\n"
"QWidget#scrollAreaWidgetContents,QWidget#scrollAreaWidgetContents_2, QScrollArea#scrollArea, QScrollArea#scrollArea_2{\n"
"	border: 0px "
                        "solid black;\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"\n"
"QMenu{\n"
"	background-color: white;\n"
"	border:1px solid rgb(82,130,164);\n"
"}\n"
"\n"
"QMenu::item:selected \n"
"{\n"
"	background-color:rgba(201,222,245,1);\n"
"	color: black;\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical,QScrollBar:horizontal\n"
"{\n"
"    width:8px;\n"
"    background-color: white;\n"
"    margin:0px,0px,0px,0px;\n"
"    padding-top:9px;  \n"
"    padding-bottom:9px;\n"
"}\n"
"QScrollBar::handle:vertical,QScrollBar::handle:horizontal\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,25%);\n"
"    border-radius:4px;  \n"
"    min-height:20;\n"
"}\n"
"/*\n"
"QScrollBar::handle:vertical:hover,QScrollBar::handle:horizontal:hover\n"
"{\n"
"    width:8px;\n"
"    background:rgba(0,0,0,50%);   \n"
"    border-radius:4px;\n"
"    min-height:20;\n"
"}\n"
"*/\n"
"QScrollBar::add-line:vertical ,QScrollBar::add-line:horizontal\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/3.png);\n"
"    subcontrol-positi"
                        "on:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical,QScrollBar::sub-line:horizontal\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/1.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-line:vertical:hover,QScrollBar::add-line:horizontal:hover\n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/4.png);\n"
"    subcontrol-position:bottom;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:horizontal:hover \n"
"{\n"
"    height:9px;width:8px;\n"
"    border-image:url(:/images/a/2.png);\n"
"    subcontrol-position:top;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical,QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal\n"
"{\n"
"    background:rgba(0,0,0,10%);\n"
"    border-radius:4px;\n"
"}\n"
"QPushButton#pin_button{\n"
"	padding:0px;\n"
"}\n"
"QPushButton#pin_button:checked{\n"
"	border: None\n"
"}\n"
"QPushButton#pin_button:pressed{\n"
"	border: None\n"
"}\n"
"QPushButton#recent_button{\n"
"	padding:0px;\n"
""
                        "}\n"
"QPushButton#recent_button:checked{\n"
"	border: None\n"
"}\n"
"QPushButton#recent_button:pressed{\n"
"	border: None\n"
"}\n"
"\n"
"")
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u":/resource/NewFile_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/resource/OpenFolder_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/resource/Save_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSaveas = QAction(MainWindow)
        self.actionSaveas.setObjectName(u"actionSaveas")
        self.actionRun = QAction(MainWindow)
        self.actionRun.setObjectName(u"actionRun")
        self.actionRun.setCheckable(False)
        icon3 = QIcon()
        icon3.addFile(u":/resource/Run_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRun.setIcon(icon3)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_bug_report = QAction(MainWindow)
        self.action_bug_report.setObjectName(u"action_bug_report")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainContent = QTabWidget(self.centralwidget)
        self.mainContent.setObjectName(u"mainContent")
        self.mainContent.setEnabled(True)
        self.mainContent.setStyleSheet(u"QTabWidget {\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget::pane {\n"
"	border:1px solid rgb(204,206,219);\n"
"	background-color: rgb(251, 251, 251);\n"
"	border-top: 2px solid rgb(0,122,204);\n"
"}\n"
"QTavWidget::tab-bar{\n"
"	\n"
"}\n"
"QTabBar::tab{\n"
"	background:rgb(240, 240, 240);\n"
"	color:black;\n"
"	min-width:100px;\n"
"	min-height:23px;\n"
"	max-height:23px\n"
"}\n"
"QTabBar::tab:hover{\n"
"	background:rgb(28,151,234);\n"
"	color:white;\n"
"}\n"
"QTabBar::tab:selected{\n"
"	border-color:black;\n"
"	background:rgb(0, 122, 204);\n"
"	color:white;\n"
"}\n"
"\n"
"QTabBar::close-button{\n"
"	image: url(:/resource/Close_WhiteNoHalo_12x_16x.svg);\n"
"}\n"
"QTabBar::close-button:selected{\n"
"	image: url(:/resource/Close_WhiteNoHalo_12x_16x.svg);\n"
"}")
        self.mainContent.setIconSize(QSize(12, 12))
        self.mainContent.setTabsClosable(True)
        self.mainContent.setMovable(False)
        self.mainContent.setTabBarAutoHide(False)
        self.start = QWidget()
        self.start.setObjectName(u"start")
        self.start.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.start)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.start)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_12.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setMinimumSize(QSize(300, 300))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 300, 300))
        self.scrollAreaWidgetContents.setStyleSheet(u"QToolButton#toolButton{\n"
"	padding: 0px;\n"
"	background-color: transparent;\n"
"	image: url(:/resource/GlyphRight_1ENoHalo_16x.svg);\n"
"}\n"
"QToolButton#toolButton:hover{\n"
"	image: url(:/resource/GlyphRight_1ENoHalo_16x - blue.svg);\n"
"}\n"
"\n"
"QToolButton#toolButton:checked{\n"
"	image: url(:/resource/ScrollbarArrowsDownRight_noHalo1E_16x.svg);\n"
"}\n"
"\n"
"QToolButton#toolButton:checked:hover{\n"
"	image: url(:/resource/ScrollbarArrowsDownRight_noHalo1E_16x - blue.svg);\n"
"}\n"
"\n"
"QToolButton#toolButton_2{\n"
"	padding: 0px;\n"
"	background-color: transparent;\n"
"	image: url(:/resource/GlyphRight_1ENoHalo_16x.svg);\n"
"}\n"
"QToolButton#toolButton_2:hover{\n"
"	image: url(:/resource/GlyphRight_1ENoHalo_16x - blue.svg);\n"
"}\n"
"\n"
"QToolButton#toolButton_2:checked{\n"
"	image: url(:/resource/ScrollbarArrowsDownRight_noHalo1E_16x.svg);\n"
"}\n"
"\n"
"QToolButton#toolButton_2:checked:hover{\n"
"	image: url(:/resource/ScrollbarArrowsDownRight_noHalo1E_16x - blue.svg);\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton = QToolButton(self.scrollAreaWidgetContents)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(0, 30))
        self.toolButton.setMaximumSize(QSize(16777215, 30))
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setStyleSheet(u"")
        self.toolButton.setIconSize(QSize(24, 24))
        self.toolButton.setCheckable(True)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton.setAutoRaise(False)
        self.toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_2.addWidget(self.toolButton)

        self.pin_button = QPushButton(self.scrollAreaWidgetContents)
        self.pin_button.setObjectName(u"pin_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pin_button.sizePolicy().hasHeightForWidth())
        self.pin_button.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.pin_button.setFont(font1)
        self.pin_button.setStyleSheet(u"")
        self.pin_button.setIconSize(QSize(16, 16))
        self.pin_button.setCheckable(True)
        self.pin_button.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pin_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")

        self.verticalLayout_11.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addWidget(self.frame_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.toolButton_2 = QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setMinimumSize(QSize(0, 30))
        self.toolButton_2.setMaximumSize(QSize(16777215, 30))
        self.toolButton_2.setIconSize(QSize(24, 24))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setArrowType(Qt.NoArrow)

        self.horizontalLayout_3.addWidget(self.toolButton_2)

        self.recent_button = QPushButton(self.scrollAreaWidgetContents)
        self.recent_button.setObjectName(u"recent_button")
        sizePolicy2.setHeightForWidth(self.recent_button.sizePolicy().hasHeightForWidth())
        self.recent_button.setSizePolicy(sizePolicy2)
        self.recent_button.setFont(font1)
        self.recent_button.setStyleSheet(u"")
        self.recent_button.setIconSize(QSize(16, 16))
        self.recent_button.setCheckable(True)
        self.recent_button.setFlat(True)

        self.horizontalLayout_3.addWidget(self.recent_button)

        self.clear_recent_btn = QPushButton(self.scrollAreaWidgetContents)
        self.clear_recent_btn.setObjectName(u"clear_recent_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(50)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.clear_recent_btn.sizePolicy().hasHeightForWidth())
        self.clear_recent_btn.setSizePolicy(sizePolicy3)
        self.clear_recent_btn.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_3.addWidget(self.clear_recent_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(20, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_13.addLayout(self.verticalLayout_7)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_4)

        self.verticalLayout_10.setStretch(4, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_12.addWidget(self.scrollArea)


        self.gridLayout_2.addLayout(self.verticalLayout_12, 1, 0, 2, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.sw_name_label = QLabel(self.frame)
        self.sw_name_label.setObjectName(u"sw_name_label")
        sizePolicy.setHeightForWidth(self.sw_name_label.sizePolicy().hasHeightForWidth())
        self.sw_name_label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(25)
        self.sw_name_label.setFont(font2)

        self.verticalLayout_5.addWidget(self.sw_name_label)

        self.department_label = QLabel(self.frame)
        self.department_label.setObjectName(u"department_label")
        sizePolicy.setHeightForWidth(self.department_label.sizePolicy().hasHeightForWidth())
        self.department_label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(11)
        self.department_label.setFont(font3)

        self.verticalLayout_5.addWidget(self.department_label)

        self.blank_label = QLabel(self.frame)
        self.blank_label.setObjectName(u"blank_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.blank_label.sizePolicy().hasHeightForWidth())
        self.blank_label.setSizePolicy(sizePolicy4)

        self.verticalLayout_5.addWidget(self.blank_label)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 2, 1)

        self.gridLayout_2.setColumnStretch(1, 1)

        self.verticalLayout_6.addLayout(self.gridLayout_2)


        self.verticalLayout_8.addWidget(self.frame)

        self.mainContent.addTab(self.start, "")
        self.view_testing = QWidget()
        self.view_testing.setObjectName(u"view_testing")
        self.verticalLayout_15 = QVBoxLayout(self.view_testing)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.afcx_view_layout = QVBoxLayout()
        self.afcx_view_layout.setObjectName(u"afcx_view_layout")

        self.verticalLayout_15.addLayout(self.afcx_view_layout)

        self.mainContent.addTab(self.view_testing, "")

        self.gridLayout.addWidget(self.mainContent, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 916, 22))
        self.menubar.setMinimumSize(QSize(0, 0))
        self.menubar.setStyleSheet(u"QMenuBar#menubar{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QMenuBar#menubar::selected{\n"
"	background-color: black;\n"
"}\n"
"\n"
"QMenuBar#menubar::item:selected{\n"
"	background-color: rgba(201,222,245,1);\n"
"}\n"
"\n"
"QMenuBar#menubar::item:pressed{\n"
"	background-color: white;\n"
"	border: 1px solid rgb(82,130,164);\n"
"	border-bottom: 0px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"QMenu{\n"
"	background-color: white;\n"
"	border:1px solid rgb(82,130,164);\n"
"}\n"
"\n"
"QMenu::item:selected \n"
"{\n"
"	background-color:rgba(201,222,245,1);\n"
"	color: black;\n"
"}\n"
"")
        self.menubar.setNativeMenuBar(True)
        self.fileMenu = QMenu(self.menubar)
        self.fileMenu.setObjectName(u"fileMenu")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.fileMenu.sizePolicy().hasHeightForWidth())
        self.fileMenu.setSizePolicy(sizePolicy6)
        self.fileMenu.setMinimumSize(QSize(0, 0))
        self.fileMenu.setMaximumSize(QSize(16777215, 16777215))
        self.fileMenu.setTearOffEnabled(False)
        self.fileMenu.setSeparatorsCollapsible(False)
        self.fileMenu.setToolTipsVisible(True)
        self.editMenu = QMenu(self.menubar)
        self.editMenu.setObjectName(u"editMenu")
        self.editMenu.setMinimumSize(QSize(0, 0))
        self.viewMenu = QMenu(self.menubar)
        self.viewMenu.setObjectName(u"viewMenu")
        self.helpMenu = QMenu(self.menubar)
        self.helpMenu.setObjectName(u"helpMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setMinimumSize(QSize(0, 23))
        self.statusbar.setMaximumSize(QSize(16777215, 23))
        self.statusbar.setAutoFillBackground(False)
        self.statusbar.setStyleSheet(u"QStatusBar#statusbar{\n"
"	background-color: rgb(0,122,204);\n"
"	color: rgb(245, 245, 245);\n"
"	border-top: 0px solid rgb(238,238,242);\n"
"}\n"
"\n"
"QStatusBar#statusbar::item{\n"
"	border: None;\n"
"}\n"
"")
        MainWindow.setStatusBar(self.statusbar)
        self.projWin = QDockWidget(MainWindow)
        self.projWin.setObjectName(u"projWin")
        sizePolicy6.setHeightForWidth(self.projWin.sizePolicy().hasHeightForWidth())
        self.projWin.setSizePolicy(sizePolicy6)
        self.projWin.setBaseSize(QSize(0, 0))
        self.projWin.setFocusPolicy(Qt.StrongFocus)
        self.projWin.setStyleSheet(u"QDockWidget#projWin{\n"
"	border : 1px solid rgb(204,206,219);\n"
"}\n"
"")
        self.projWin.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidgetContents_12 = QWidget()
        self.dockWidgetContents_12.setObjectName(u"dockWidgetContents_12")
        self.dockWidgetContents_12.setBaseSize(QSize(0, 0))
        self.dockWidgetContents_12.setFocusPolicy(Qt.StrongFocus)
        self.dockWidgetContents_12.setStyleSheet(u"QWidget#dockWidgetContents_12{\n"
"	border : 1px solid rgb(204,206,219);\n"
"}\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.dockWidgetContents_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.projWin.setWidget(self.dockWidgetContents_12)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.projWin)
        self.configWin = QDockWidget(MainWindow)
        self.configWin.setObjectName(u"configWin")
        sizePolicy6.setHeightForWidth(self.configWin.sizePolicy().hasHeightForWidth())
        self.configWin.setSizePolicy(sizePolicy6)
        self.configWin.setMaximumSize(QSize(524287, 524287))
        self.configWin.setFocusPolicy(Qt.StrongFocus)
        self.configWin.setStyleSheet(u"QDockWidget#configWin{\n"
"	border : 0px solid black;\n"
"}\n"
"")
        self.configWin.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.configWin.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.configWin_content = QWidget()
        self.configWin_content.setObjectName(u"configWin_content")
        sizePolicy6.setHeightForWidth(self.configWin_content.sizePolicy().hasHeightForWidth())
        self.configWin_content.setSizePolicy(sizePolicy6)
        self.configWin_content.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.configWin_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.configWin_content)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy7)
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"	background-color: rgb(245,245,245);\n"
"	border:1px solid rgb(204,206,219);\n"
"	margin-right:0px;\n"
"	margin-left:0px;\n"
"	margin-top:1px\n"
"}")
        self.textEdit_2.setFrameShape(QFrame.NoFrame)
        self.textEdit_2.setFrameShadow(QFrame.Plain)
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit_2)

        self.configWin.setWidget(self.configWin_content)
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.configWin)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setStyleSheet(u"QDockWidget#dockWidget{\n"
"	border : 0px solid black;\n"
"}\n"
"")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.verticalLayout_3 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.dockWidgetContents)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit#textEdit{\n"
"	border:1px solid rgb(204,206,219);\n"
"	border-top: 0px solid rgb(204,206,219);\n"
"	background-color: white;\n"
"}\n"
"")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setFrameShadow(QFrame.Plain)
        self.textEdit.setAutoFormatting(QTextEdit.AutoNone)
        self.textEdit.setReadOnly(False)
        self.textEdit.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_3.addWidget(self.textEdit)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)
        self.toolBar_left = QToolBar(MainWindow)
        self.toolBar_left.setObjectName(u"toolBar_left")
        self.toolBar_left.setStyleSheet(u"\n"
"QToolBar#toolBar_left{\n"
"	border: 0px solid rgb(204,206,219);\n"
"	background-color: rgba(238,238,242);\n"
"	padding-right: 10px\n"
"}\n"
"\n"
"\n"
"")
        self.toolBar_left.setMovable(False)
        self.toolBar_left.setOrientation(Qt.Vertical)
        self.toolBar_left.setIconSize(QSize(16, 16))
        self.toolBar_left.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar_left.setFloatable(False)
        MainWindow.addToolBar(Qt.LeftToolBarArea, self.toolBar_left)
        self.toolBar_menu = ToolBar(MainWindow)
        self.toolBar_menu.setObjectName(u"toolBar_menu")
        self.toolBar_menu.setMinimumSize(QSize(0, 0))
        self.toolBar_menu.setStyleSheet(u"QToolBar#toolBar_menu{\n"
"	border: 0px solid rgb(204,206,219);\n"
"	border-bottom: 0px solid rgb(204,206,219);\n"
"	border-left: 0px solid rgb(204,206,219);\n"
"	border-right: 0px solid rgb(204,206,219);\n"
"	margin: 0px;\n"
"	padding: 0px\n"
"}")
        self.toolBar_menu.setMovable(False)
        self.toolBar_menu.setAllowedAreas(Qt.NoToolBarArea)
        self.toolBar_menu.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_menu)
        self.toolBar = ToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setStyleSheet(u"QToolBar#toolBar{\n"
"	border: 0px solid rgb(204,206,219);\n"
"	border-bottom: 0px solid rgb(204,206,219);\n"
"	border-left: 0px solid rgb(204,206,219);\n"
"	border-right: 0px solid rgb(204,206,219);	\n"
"	margin: 5px;\n"
"}\n"
"")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(Qt.AllToolBarAreas)
        self.toolBar.setOrientation(Qt.Horizontal)
        self.toolBar.setIconSize(QSize(16, 16))
        self.toolBar.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.toolBar_right = QToolBar(MainWindow)
        self.toolBar_right.setObjectName(u"toolBar_right")
        self.toolBar_right.setStyleSheet(u"QToolBar#toolBar_right{\n"
"	border: 0px solid rgb(204,206,219);\n"
"	background-color: rgba(238,238,242);\n"
"	padding: 1px\n"
"}\n"
"")
        self.toolBar_right.setMovable(False)
        self.toolBar_right.setFloatable(False)
        MainWindow.addToolBar(Qt.RightToolBarArea, self.toolBar_right)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.editMenu.menuAction())
        self.menubar.addAction(self.viewMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
        self.fileMenu.addAction(self.actionNew)
        self.fileMenu.addAction(self.actionOpen)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionSave)
        self.fileMenu.addAction(self.actionSaveas)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionExit)
        self.editMenu.addAction(self.actionRun)
        self.helpMenu.addAction(self.action_bug_report)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.action_about)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.mainContent.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa(&N)", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(&O)", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58(&S)", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSaveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a...(&A)", None))
#if QT_CONFIG(shortcut)
        self.actionSaveas.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionRun.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c(&R)", None))
#if QT_CONFIG(tooltip)
        self.actionRun.setToolTip(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c(Ctrl+R)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionRun.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa(&X)", None))
#if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_about.setIconText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.action_about.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        self.action_bug_report.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u95ee\u9898", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6700\u8fd1\u4f7f\u7528\u7684\u7684\u5185\u5bb9", None))
        self.toolButton.setText("")
#if QT_CONFIG(shortcut)
        self.toolButton.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.pin_button.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u56fa\u5b9a", None))
        self.toolButton_2.setText("")
        self.recent_button.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1", None))
        self.clear_recent_btn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a(&C)", None))
        self.sw_name_label.setText(QCoreApplication.translate("MainWindow", u"\u7efc\u5408\u8bbe\u8ba1\u5e73\u53f0 2021", None))
        self.department_label.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u5316\u4fe1\u606f\u8bbe\u8ba1\u6240", None))
        self.blank_label.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u4f7f\u7528", None))
        self.mainContent.setTabText(self.mainContent.indexOf(self.start), QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.mainContent.setTabText(self.mainContent.indexOf(self.view_testing), QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.fileMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.editMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.viewMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe(&V)", None))
        self.helpMenu.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.projWin.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b", None))
        self.configWin.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5c5e\u6027", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.toolBar_left.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.toolBar_menu.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_3", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_right.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

