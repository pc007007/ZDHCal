# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'afcCalMain.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_afcCalMain(object):
    def setupUi(self, afcCalMain):
        if not afcCalMain.objectName():
            afcCalMain.setObjectName(u"afcCalMain")
        afcCalMain.resize(870, 725)
        afcCalMain.setStyleSheet(u"/*\n"
"QPushButton {\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"	padding: 4px 8px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid rgb(0, 122, 204);\n"
"}\n"
"QPushButton:checked {\n"
"    background-color: rgb(0, 122, 204);\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: white;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: grey;\n"
"    border: 1px solid grey;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 122, 204);\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 122, 204);\n"
"}\n"
"*/\n"
"\n"
"QPushButton {\n"
"	border-radius: 0px;\n"
"    color: white;\n"
"	padding: 4px 12px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid white;\n"
"}\n"
"QPush"
                        "Button:checked {\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: black;\n"
"	border: 1px solid rgb(51,153,255);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: white;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    color: grey;\n"
"    border: 1px solid white;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(201,222,245);\n"
"    color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0,122,204);\n"
"	color:white\n"
"}\n"
"\n"
"/*tablewidget \u6837\u5f0f*/\n"
"QTableView , QTableWidget{\n"
"	selection-background-color: rgb(178,215,240);\n"
"	background-color:white;/*\u6574\u4e2a\u8868\u683c\u7684\u80cc\u666f\u8272\uff0c\u8fd9\u91cc\u4e3a\u767d\u8272*/\n"
"	alternate-background-color: rgb(250, 250, 250);\n"
"	border:0px solid #E0DDDC;/*\u8fb9\u6846\u4e3a1\u50cf\u7d20\uff0c\u7070\u8272*/\n"
"	border-top:0px solid #E0DDDC;\n"
"	border-bottom:0px solid #E0DDDC;\n"
"	gridline-color:lightgray;/*\u8fd9"
                        "\u4e2a\u662f\u8868\u683c\u7684\u683c\u5b50\u7ebf\u7684\u989c\u8272\uff0c\u4e3a\u4eae\u7070*/\n"
"}\n"
"/*\u8fd9\u91cc\u662f\u8868\u683c\u8868\u5934\u6837\u5f0f*/\n"
"QHeaderView::section{\n"
"	background-color:white;/*\u80cc\u666f\u8272 \u767d\u8272*/\n"
"	border:0px solid #E0DDDC;/*\u5148\u628a\u8fb9\u6846\u5bbd\u5ea6\u8bbe\u4e3a0\uff0c\u5373\u9690\u85cf\u6240\u6709\u8868\u5934\u8fb9\u6846*/\n"
"	border-bottom:1px solid #E0DDDC;/*\u7136\u540e\u53ea\u663e\u793a\u4e0b\u8fb9\u6846\uff0c\u56e0\u4e3a\u4e0a\u8fb9\u6846\u548c\u5de6\u53f3\u8fb9\u6846\u662f\u6574\u4e2aTable\u7684\u8fb9\u6846\uff0c\u90fd\u663e\u793a\u4f1a\u67092px\u7684\u8fb9\u6846\u5bbd\u5ea6*/\n"
"	height:50px;/*\u8868\u5934\u9ad8\u5ea6*/\n"
"}\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"	border:0px solid #E0DDDC;\n"
"	background-color:white;\n"
"	border-top:0px solid #E0DDDC;\n"
"	border-left:0px solid #E0DDDC;\n"
"	border-right:0px solid #E0DDDC;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(afcCalMain)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(afcCalMain)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"\n"
"}\n"
"QTabWidget::pane {\n"
"	border:0px solid rgb(204,206,219);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTavWidget::tab-bar{\n"
"	\n"
"}\n"
"QTabBar::tab{\n"
"\n"
"}\n"
"QTabBar::tab:hover{\n"
"\n"
"}\n"
"QTabBar::tab:selected{\n"
"\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tab_recent = QWidget()
        self.tab_recent.setObjectName(u"tab_recent")
        self.gridLayout_2 = QGridLayout(self.tab_recent)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, 9, 0)
        self.o4Btn = QPushButton(self.tab_recent)
        self.o4Btn.setObjectName(u"o4Btn")
        font = QFont()
        font.setPointSize(9)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.o4Btn.setFont(font)
        self.o4Btn.setCheckable(True)

        self.gridLayout_2.addWidget(self.o4Btn, 0, 4, 1, 1)

        self.o2Btn = QPushButton(self.tab_recent)
        self.o2Btn.setObjectName(u"o2Btn")
        self.o2Btn.setCheckable(True)

        self.gridLayout_2.addWidget(self.o2Btn, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.tab_recent)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.o1Wdiget = QWidget()
        self.o1Wdiget.setObjectName(u"o1Wdiget")
        self.verticalLayout = QVBoxLayout(self.o1Wdiget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.o1tableWidget = QTableWidget(self.o1Wdiget)
        self.o1tableWidget.setObjectName(u"o1tableWidget")

        self.verticalLayout.addWidget(self.o1tableWidget)

        self.stackedWidget.addWidget(self.o1Wdiget)
        self.o2Wdiget = QWidget()
        self.o2Wdiget.setObjectName(u"o2Wdiget")
        self.verticalLayout_2 = QVBoxLayout(self.o2Wdiget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.o2tableWidget = QTableWidget(self.o2Wdiget)
        self.o2tableWidget.setObjectName(u"o2tableWidget")

        self.verticalLayout_2.addWidget(self.o2tableWidget)

        self.stackedWidget.addWidget(self.o2Wdiget)
        self.o3Wdiget = QWidget()
        self.o3Wdiget.setObjectName(u"o3Wdiget")
        self.verticalLayout_3 = QVBoxLayout(self.o3Wdiget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.o3tableWidget = QTableWidget(self.o3Wdiget)
        self.o3tableWidget.setObjectName(u"o3tableWidget")

        self.verticalLayout_3.addWidget(self.o3tableWidget)

        self.stackedWidget.addWidget(self.o3Wdiget)
        self.o4Wdiget = QWidget()
        self.o4Wdiget.setObjectName(u"o4Wdiget")
        self.verticalLayout_4 = QVBoxLayout(self.o4Wdiget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.o4tableWidget = QTableWidget(self.o4Wdiget)
        self.o4tableWidget.setObjectName(u"o4tableWidget")

        self.verticalLayout_4.addWidget(self.o4tableWidget)

        self.stackedWidget.addWidget(self.o4Wdiget)
        self.o5Widget = QWidget()
        self.o5Widget.setObjectName(u"o5Widget")
        self.verticalLayout_13 = QVBoxLayout(self.o5Widget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.o5tableWidget = QTableWidget(self.o5Widget)
        self.o5tableWidget.setObjectName(u"o5tableWidget")

        self.verticalLayout_13.addWidget(self.o5tableWidget)

        self.stackedWidget.addWidget(self.o5Widget)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 9)

        self.o1Btn = QPushButton(self.tab_recent)
        self.o1Btn.setObjectName(u"o1Btn")
        self.o1Btn.setCheckable(True)
        self.o1Btn.setChecked(False)
        self.o1Btn.setAutoExclusive(False)
        self.o1Btn.setFlat(False)

        self.gridLayout_2.addWidget(self.o1Btn, 0, 0, 1, 1)

        self.o3Btn = QPushButton(self.tab_recent)
        self.o3Btn.setObjectName(u"o3Btn")
        self.o3Btn.setCheckable(True)

        self.gridLayout_2.addWidget(self.o3Btn, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(531, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 5, 1, 1)

        self.toExcelBtn = QPushButton(self.tab_recent)
        self.toExcelBtn.setObjectName(u"toExcelBtn")
        self.toExcelBtn.setStyleSheet(u"padding:5px")
        icon = QIcon()
        icon.addFile(u":/resource/ExportToExcel_16x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toExcelBtn.setIcon(icon)
        self.toExcelBtn.setIconSize(QSize(16, 16))

        self.gridLayout_2.addWidget(self.toExcelBtn, 0, 6, 1, 3)

        self.o5Btn = QPushButton(self.tab_recent)
        self.o5Btn.setObjectName(u"o5Btn")
        self.o5Btn.setCheckable(True)

        self.gridLayout_2.addWidget(self.o5Btn, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_recent, "")
        self.tab_far = QWidget()
        self.tab_far.setObjectName(u"tab_far")
        self.gridLayout = QGridLayout(self.tab_far)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.stackedWidget_2 = QStackedWidget(self.tab_far)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"")
        self.o1Wdiget_2 = QWidget()
        self.o1Wdiget_2.setObjectName(u"o1Wdiget_2")
        self.verticalLayout_6 = QVBoxLayout(self.o1Wdiget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.o1tableWidget_2 = QTableWidget(self.o1Wdiget_2)
        self.o1tableWidget_2.setObjectName(u"o1tableWidget_2")

        self.verticalLayout_6.addWidget(self.o1tableWidget_2)

        self.stackedWidget_2.addWidget(self.o1Wdiget_2)
        self.o2Wdiget_2 = QWidget()
        self.o2Wdiget_2.setObjectName(u"o2Wdiget_2")
        self.verticalLayout_7 = QVBoxLayout(self.o2Wdiget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.o2tableWidget_2 = QTableWidget(self.o2Wdiget_2)
        self.o2tableWidget_2.setObjectName(u"o2tableWidget_2")

        self.verticalLayout_7.addWidget(self.o2tableWidget_2)

        self.stackedWidget_2.addWidget(self.o2Wdiget_2)
        self.o3Wdiget_2 = QWidget()
        self.o3Wdiget_2.setObjectName(u"o3Wdiget_2")
        self.verticalLayout_8 = QVBoxLayout(self.o3Wdiget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.o3tableWidget_2 = QTableWidget(self.o3Wdiget_2)
        self.o3tableWidget_2.setObjectName(u"o3tableWidget_2")

        self.verticalLayout_8.addWidget(self.o3tableWidget_2)

        self.stackedWidget_2.addWidget(self.o3Wdiget_2)
        self.o4Wdiget_2 = QWidget()
        self.o4Wdiget_2.setObjectName(u"o4Wdiget_2")
        self.verticalLayout_9 = QVBoxLayout(self.o4Wdiget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.o4tableWidget_2 = QTableWidget(self.o4Wdiget_2)
        self.o4tableWidget_2.setObjectName(u"o4tableWidget_2")

        self.verticalLayout_9.addWidget(self.o4tableWidget_2)

        self.stackedWidget_2.addWidget(self.o4Wdiget_2)
        self.o5Widget_2 = QWidget()
        self.o5Widget_2.setObjectName(u"o5Widget_2")
        self.verticalLayout_19 = QVBoxLayout(self.o5Widget_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.o5tableWidget_2 = QTableWidget(self.o5Widget_2)
        self.o5tableWidget_2.setObjectName(u"o5tableWidget_2")

        self.verticalLayout_19.addWidget(self.o5tableWidget_2)

        self.stackedWidget_2.addWidget(self.o5Widget_2)

        self.gridLayout.addWidget(self.stackedWidget_2, 1, 0, 1, 8)

        self.o3Btn_2 = QPushButton(self.tab_far)
        self.o3Btn_2.setObjectName(u"o3Btn_2")
        self.o3Btn_2.setCheckable(True)

        self.gridLayout.addWidget(self.o3Btn_2, 0, 2, 1, 1)

        self.o1Btn_2 = QPushButton(self.tab_far)
        self.o1Btn_2.setObjectName(u"o1Btn_2")
        self.o1Btn_2.setCheckable(True)
        self.o1Btn_2.setChecked(False)
        self.o1Btn_2.setAutoExclusive(False)
        self.o1Btn_2.setFlat(False)

        self.gridLayout.addWidget(self.o1Btn_2, 0, 0, 1, 1)

        self.o4Btn_2 = QPushButton(self.tab_far)
        self.o4Btn_2.setObjectName(u"o4Btn_2")
        self.o4Btn_2.setCheckable(True)

        self.gridLayout.addWidget(self.o4Btn_2, 0, 4, 1, 1)

        self.toExcelBtn_2 = QPushButton(self.tab_far)
        self.toExcelBtn_2.setObjectName(u"toExcelBtn_2")
        self.toExcelBtn_2.setStyleSheet(u"padding:5px")
        self.toExcelBtn_2.setIcon(icon)
        self.toExcelBtn_2.setIconSize(QSize(16, 16))

        self.gridLayout.addWidget(self.toExcelBtn_2, 0, 6, 1, 2)

        self.o2Btn_2 = QPushButton(self.tab_far)
        self.o2Btn_2.setObjectName(u"o2Btn_2")
        self.o2Btn_2.setCheckable(True)

        self.gridLayout.addWidget(self.o2Btn_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(531, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 1, 1)

        self.o5Btn_2 = QPushButton(self.tab_far)
        self.o5Btn_2.setObjectName(u"o5Btn_2")
        self.o5Btn_2.setCheckable(True)

        self.gridLayout.addWidget(self.o5Btn_2, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_far, "")
        self.tab_figure = QWidget()
        self.tab_figure.setObjectName(u"tab_figure")
        self.verticalLayout_10 = QVBoxLayout(self.tab_figure)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.tab_figure)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"	border:1px solid rgb(204,206,219);\n"
"     background-color: transparent;\n"
"     border-top: 10px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-left: 10px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-bottom: 10px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  #ececef);\n"
"     border-right: 10px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 #ececef);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_2)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")

        self.verticalLayout_31.addLayout(self.verticalLayout_30)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 2, 1)

        self.frame = QFrame(self.tab_figure)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	border:1px solid rgb(204,206,219);\n"
"     background-color: transparent;\n"
"     border-top: 10px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-left: 10px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-bottom: 10px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  #ececef);\n"
"     border-right: 10px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 #ececef);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_12.addWidget(self.label)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_12.addWidget(self.comboBox)


        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 2, 2)

        self.tabWidget_2 = QTabWidget(self.frame)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabBarAutoHide(True)
        self.bar_tab = QWidget()
        self.bar_tab.setObjectName(u"bar_tab")
        self.verticalLayout_15 = QVBoxLayout(self.bar_tab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.label_2 = QLabel(self.bar_tab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_15.addWidget(self.label_2)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addLayout(self.verticalLayout_16)

        self.label_3 = QLabel(self.bar_tab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_15.addWidget(self.label_3)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_15.addLayout(self.verticalLayout_17)

        self.label_5 = QLabel(self.bar_tab)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_15.addWidget(self.label_5)

        self.mode_combo_box = QComboBox(self.bar_tab)
        self.mode_combo_box.addItem("")
        self.mode_combo_box.addItem("")
        self.mode_combo_box.setObjectName(u"mode_combo_box")

        self.verticalLayout_15.addWidget(self.mode_combo_box)

        self.generate_bar_button = QPushButton(self.bar_tab)
        self.generate_bar_button.setObjectName(u"generate_bar_button")
        self.generate_bar_button.setStyleSheet(u"QPushButton{\n"
"	border:1px solid black;\n"
"}")

        self.verticalLayout_15.addWidget(self.generate_bar_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer)

        self.tabWidget_2.addTab(self.bar_tab, "")
        self.parallel_tab = QWidget()
        self.parallel_tab.setObjectName(u"parallel_tab")
        self.verticalLayout_11 = QVBoxLayout(self.parallel_tab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.parallel_tab)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)

        self.verticalLayout_5.addLayout(self.verticalLayout_14)

        self.label_7 = QLabel(self.parallel_tab)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(5, 5, 5, 5)
        self.checkBox = QCheckBox(self.parallel_tab)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_18.addWidget(self.checkBox)


        self.verticalLayout_5.addLayout(self.verticalLayout_18)

        self.generate_parallel_button = QPushButton(self.parallel_tab)
        self.generate_parallel_button.setObjectName(u"generate_parallel_button")
        self.generate_parallel_button.setStyleSheet(u"QPushButton{\n"
"	border:1px solid black;\n"
"}")

        self.verticalLayout_5.addWidget(self.generate_parallel_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_11.addLayout(self.verticalLayout_5)

        self.tabWidget_2.addTab(self.parallel_tab, "")
        self.pie_tab = QWidget()
        self.pie_tab.setObjectName(u"pie_tab")
        self.verticalLayout_27 = QVBoxLayout(self.pie_tab)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_13 = QLabel(self.pie_tab)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_26.addWidget(self.label_13)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(5, 5, 5, 5)
        self.radioButton = QRadioButton(self.pie_tab)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setChecked(True)

        self.verticalLayout_28.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.pie_tab)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_28.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.pie_tab)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_28.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.pie_tab)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.verticalLayout_28.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.pie_tab)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.verticalLayout_28.addWidget(self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.pie_tab)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.verticalLayout_28.addWidget(self.radioButton_6)


        self.verticalLayout_26.addLayout(self.verticalLayout_28)

        self.generate_pie_button = QPushButton(self.pie_tab)
        self.generate_pie_button.setObjectName(u"generate_pie_button")
        self.generate_pie_button.setStyleSheet(u"QPushButton{\n"
"	border:1px solid black;\n"
"}")

        self.verticalLayout_26.addWidget(self.generate_pie_button)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_5)


        self.verticalLayout_27.addLayout(self.verticalLayout_26)

        self.tabWidget_2.addTab(self.pie_tab, "")

        self.gridLayout_5.addWidget(self.tabWidget_2, 2, 0, 1, 1)


        self.verticalLayout_29.addLayout(self.gridLayout_5)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 2, 1)

        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 6)

        self.verticalLayout_10.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.tab_figure, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame#frame_3{\n"
"	border:1px solid rgb(204,206,219);\n"
"     background-color: transparent;\n"
"     border-top: 10px solid qlineargradient(y0:0, y1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-left: 10px solid qlineargradient(x0:0, x1:1,stop: 0 #ececef, stop: 1 white);\n"
"     border-bottom: 10px solid qlineargradient(y0:0, y1:1,stop: 0 white, stop: 1  #ececef);\n"
"     border-right: 10px solid qlineargradient(x0:0, x1:1,stop:  0 white, stop: 1 #ececef);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.exp_button = QPushButton(self.frame_3)
        self.exp_button.setObjectName(u"exp_button")
        self.exp_button.setMinimumSize(QSize(0, 50))

        self.verticalLayout_22.addWidget(self.exp_button)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")

        self.verticalLayout_22.addLayout(self.verticalLayout_21)


        self.verticalLayout_20.addWidget(self.frame_3)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(afcCalMain)

        self.tabWidget.setCurrentIndex(3)
        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(afcCalMain)
    # setupUi

    def retranslateUi(self, afcCalMain):
        afcCalMain.setWindowTitle(QCoreApplication.translate("afcCalMain", u"Form", None))
        self.o4Btn.setText(QCoreApplication.translate("afcCalMain", u"\u63d0\u8d44\u6599\u6570\u91cf", None))
        self.o2Btn.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa1", None))
        self.o1Btn.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u5165\u8d44\u6599", None))
        self.o3Btn.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa2", None))
        self.toExcelBtn.setText("")
        self.o5Btn.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recent), QCoreApplication.translate("afcCalMain", u"\u8fd1\u671f", None))
        self.o3Btn_2.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa2", None))
        self.o1Btn_2.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u5165\u8d44\u6599", None))
        self.o4Btn_2.setText(QCoreApplication.translate("afcCalMain", u"\u63d0\u8d44\u6599\u6570\u91cf", None))
        self.toExcelBtn_2.setText("")
        self.o2Btn_2.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa1", None))
        self.o5Btn_2.setText(QCoreApplication.translate("afcCalMain", u"\u8f93\u51fa3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_far), QCoreApplication.translate("afcCalMain", u"\u8fdc\u671f", None))
        self.label.setText(QCoreApplication.translate("afcCalMain", u"\u8868\u683c\u7c7b\u578b", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("afcCalMain", u"\u67f1\u72b6\u56fe", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("afcCalMain", u"\u5e73\u884c\u5206\u7c7b\u56fe", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("afcCalMain", u"\u997c\u56fe", None))

        self.label_2.setText(QCoreApplication.translate("afcCalMain", u"x\u8f74", None))
        self.label_3.setText(QCoreApplication.translate("afcCalMain", u"y\u8f74", None))
        self.label_5.setText(QCoreApplication.translate("afcCalMain", u"\u6a21\u5f0f", None))
        self.mode_combo_box.setItemText(0, QCoreApplication.translate("afcCalMain", u"\u5806\u53e0", None))
        self.mode_combo_box.setItemText(1, QCoreApplication.translate("afcCalMain", u"\u7ec4\u5408", None))

        self.generate_bar_button.setText(QCoreApplication.translate("afcCalMain", u"\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.bar_tab), QCoreApplication.translate("afcCalMain", u"bar", None))
        self.label_6.setText(QCoreApplication.translate("afcCalMain", u"\u7ef4\u5ea6", None))
        self.label_7.setText(QCoreApplication.translate("afcCalMain", u"\u5f52\u7c7b\u989c\u8272", None))
        self.checkBox.setText(QCoreApplication.translate("afcCalMain", u"\u7a7a", None))
        self.generate_parallel_button.setText(QCoreApplication.translate("afcCalMain", u"\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.parallel_tab), QCoreApplication.translate("afcCalMain", u"parallel", None))
        self.label_13.setText(QCoreApplication.translate("afcCalMain", u"\u503c", None))
        self.radioButton.setText(QCoreApplication.translate("afcCalMain", u"\u8fdb\u7ad9\u68c0\u7968\u673a", None))
        self.radioButton_2.setText(QCoreApplication.translate("afcCalMain", u"\u51fa\u7ad9\u68c0\u7968\u673a", None))
        self.radioButton_3.setText(QCoreApplication.translate("afcCalMain", u"\u53cc\u5411\u68c0\u7968\u673a", None))
        self.radioButton_4.setText(QCoreApplication.translate("afcCalMain", u"\u53cc\u5411\u68c0\u7968\u673a\n"
"(\u5bbd)", None))
        self.radioButton_5.setText(QCoreApplication.translate("afcCalMain", u"\u51fa\u7ad9\u68c0\u7968\u673a\n"
"(\u603b\u53ef\u7528\u91cf)", None))
        self.radioButton_6.setText(QCoreApplication.translate("afcCalMain", u"\u81ea\u52a8\u552e\u7968\u673a", None))
        self.generate_pie_button.setText(QCoreApplication.translate("afcCalMain", u"\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.pie_tab), QCoreApplication.translate("afcCalMain", u"pie", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_figure), QCoreApplication.translate("afcCalMain", u"\u81ea\u5b9a\u4e49\u56fe\u8868", None))
        self.exp_button.setText(QCoreApplication.translate("afcCalMain", u"\u751f\u6210\u62a5\u544a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("afcCalMain", u"\u521b\u65b0\u6027\u63a2\u7d22", None))
    # retranslateUi

