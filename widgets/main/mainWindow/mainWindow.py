import os
import json
import time

import psutil
from PySide6.QtGui import QIcon, QPixmap, QCursor, QFontMetrics, QMouseEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QFileDialog, QTextEdit, QLabel, QVBoxLayout, QPushButton, \
    QSizePolicy, QSpacerItem, QHBoxLayout, QApplication, QToolButton, QDockWidget, QToolBar, QWidgetAction
from PySide6 import QtCore, QtSvg, QtXml
from PySide6.QtCore import Slot, Qt, QPropertyAnimation, QRect, QByteArray, QPoint, QEasingCurve, QSize
# from PySide6 import QtCore, QtSvg, QtXml
from widgets.main.filedirectbar.main import FileDirectoryBar
from widgets.main.mainWindow.bigButtonWidget import BigButton
from widgets.main.mainWindow.mainTitleWidget import MainTitleWidget
from widgets.main.mainWindow.recentContentLinkWidget import RecentContentLink
from widgets.main.mainWindow.ui.ToolBar import ToolBar
from widgets.main.mainWindow.ui.main_window_layout import Ui_MainWindow
from widgets.main.projectDockWidget.app_project import Project
from widgets.module.afc.configDockWidget_afc.app_afc_configRidershipCal import Ridership_Config
from tools.afcCalculationV2 import AFC_project
import tools.afcCalculationV2 as afcCalculation
from widgets.module.afc.contentWidget_afc.app_afc_content import afc_content
from widgets.main.statusBarWidget.statusWidget import statusWidget
from widgets.main.dockTitleWidget.myDockTitleWidget import myDockTitleWidget
from widgets.main.newProjectWidget.NewProjectDlg import NewProjectDlg
from widgets.module.afc.toolbar.toolbar import AFCToolBar
from widgets.qss import Qss


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.curTabFilePath = "start"
        self.id = 1
        
        # 添加Project组件到projWin中
        self.projectWidget = Project()
        self.m_flag = False
        self.ui.setupUi(self)

        # 初始配置模块
        self.ui.configWin.hide()
        # self.ui.dockWidget.hide()  # 隐藏命令行

        # 匹配view视图action
        self.ui.projWin.toggleViewAction().setIcon(QIcon(":/resource/DocumentOutline_16x.svg"))
        self.ui.viewMenu.addAction(self.ui.projWin.toggleViewAction())
        self.ui.viewMenu.addAction(self.ui.configWin.toggleViewAction())
        self.ui.viewMenu.addAction(self.ui.dockWidget.toggleViewAction())

        # projectDock自定义标题栏
        self.ui.projWin.setContentsMargins(0, 0, 0, 0)
        self.ui.projWin.setTitleBarWidget(myDockTitleWidget())
        self.ui.projWin.setWidget(self.projectWidget)
        self.ui.projWin.titleBarWidget().setTitle("项目")
        # ConfigDock自定义标题栏
        self.ui.configWin.setTitleBarWidget(myDockTitleWidget())
        self.ui.configWin.titleBarWidget().setTitle("属性")
        # comandLineDock自定义标题栏
        self.ui.dockWidget.setTitleBarWidget(myDockTitleWidget())
        self.ui.dockWidget.titleBarWidget().setTitle("命令行")

        # 信号槽
        self.projectWidget.ui.treeView.doubleClicked.connect(self.slot_ProjectCtlg_was_doubleClicked)  # 点击项目文档相关动作
        self.ui.mainContent.currentChanged.connect(self.the_mainContent_was_changed)  # 内容切换配置列表也切换
        self.ui.mainContent.tabCloseRequested.connect(self.close_tab)  # 关闭标签

        # Action
        self.ui.actionOpen.triggered.connect(self.the_openProjectbutton_was_clicked)
        self.ui.actionRun.triggered.connect(self.runCal)
        self.ui.actionSave.triggered.connect(self.saveProject)
        self.ui.actionNew.triggered.connect(self.the_newProjectButton_was_clicked)
        self.ui.actionExit.triggered.connect(lambda: self.parent().parent().parent().close())
        self.ui.actionExit.setShortcut("Alt+F4")

        self.setup_titlebar()                                                      # 装载标题栏
        self.setup_file_directory_bar("C:/Users/pc080/OneDrive/1Pyside/天津1号线")   # 装载文件浏览toolbar
        self.setup_welcome_content()                                                # 装载开始界面的内容
        self.setup_left_toolbar()                                                   # 装载左侧工具栏
        self.status_bar = self.setup_statusbar()                                    # 设置状态栏
        self.setup_bottom_toolbar()                                                 # 添加底部Toolbar

        self.ui.mainContent.setCurrentIndex(0)

        # Test Area
        # self.ui.afcx_view_layout.addWidget(NodeEditor())

    def setFrame(self, frame):
        self.window_frame = frame

    def setup_statusbar(self):
        label = QLabel("就绪")
        label.setStyleSheet("color: white")
        self.ui.statusbar.addWidget(label)

        status_bar = statusWidget()
        self.ui.statusbar.addPermanentWidget(status_bar)  # 增加statusBar模块

        return status_bar

    def setup_file_directory_bar(self, filepath):
        file_toolbar = QToolBar()
        file_toolbar.setObjectName('toolBar_file')
        file_toolbar.setStyleSheet(Qss().toolbar_afc)
        self.addToolBarBreak(Qt.ToolBarArea.TopToolBarArea)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, file_toolbar)
        self.file_bar = FileDirectoryBar(filepath, self)
        self.file_bar.pathChanged.connect(lambda path: self.projectWidget.setPath(path))
        file_toolbar.addWidget(self.file_bar)
        file_toolbar.setMovable(False)
        file_toolbar.hide()

    def setup_welcome_content(self):
        self.ui.mainContent.widget(0).setProperty("full_path", "开始.start")
        self.ui.mainContent.widget(0).type = 'start'
        self.ui.clear_recent_btn.clicked.connect(self.slot_click_clear_recent_btn)
        self.ui.clear_recent_btn.hide()

        ex_bigbutton = BigButton()
        ex_bigbutton.setCustomIcon(QIcon(':/resource/Gallery_16x-o.svg'))
        ex_bigbutton.setTitle("示例项目")
        ex_bigbutton.setDescriptionL1('示例项目展示')
        self.ui.verticalLayout_2.insertWidget(1, ex_bigbutton)
        ex_bigbutton.clicked.connect(self.the_pushButton_was_clicked)

        new_bigbutton = BigButton()
        new_bigbutton.setCustomIcon(QIcon(':/resource/NewFileCollection_16x.svg'))
        new_bigbutton.setTitle("创建新项目")
        new_bigbutton.setDescriptionL1('根据需求类型创建的项目(*.afc)')
        new_bigbutton.setDescriptionL2('目前支持AFC客流计算')
        self.ui.verticalLayout_2.insertWidget(1, new_bigbutton)
        new_bigbutton.clicked.connect(self.the_newProjectButton_was_clicked)

        open_bigbutton = BigButton()
        open_bigbutton.setCustomIcon(QIcon(':/resource/OpenFolder_16x-o.svg'))
        open_bigbutton.setTitle("打开本地文件夹")
        open_bigbutton.setDescriptionL1('导航和编辑任何文件夹中的内容')
        self.ui.verticalLayout_2.insertWidget(1, open_bigbutton)
        open_bigbutton.clicked.connect(self.the_openProjectbutton_was_clicked)

        self.ui.toolButton.toggled.connect(lambda checked: self.ui.frame_2.setHidden(checked))
        self.ui.toolButton_2.toggled.connect(lambda checked: self.ui.frame_3.setHidden(checked))
        self.ui.pin_button.toggled.connect(lambda checked: self.ui.toolButton.setChecked(checked))
        self.ui.recent_button.toggled.connect(lambda checked: self.ui.toolButton_2.setChecked(checked))
        self.ui.toolButton.toggled.connect(lambda checked: self.ui.pin_button.setChecked(checked))
        self.ui.toolButton_2.toggled.connect(lambda checked: self.ui.recent_button.setChecked(checked))

    def setup_left_toolbar(self):
        action_project = self.ui.projWin.toggleViewAction()
        self.ui.toolBar_left.addAction(action_project)

    def setup_bottom_toolbar(self):
        toolbar_bottom = QToolBar()
        toolbar_bottom.setObjectName("toolBar_bottom")
        toolbar_bottom.setMovable(False)
        toolbar_bottom.setStyleSheet("""
            QToolBar#toolBar_bottom{
                border: 0px solid rgb(204,206,219);
                background-color: rgba(238,238,242);
                padding: 0px;
                margin: 0px;
            }
            """)
        self.addToolBar(Qt.ToolBarArea.BottomToolBarArea, toolbar_bottom)

    def setup_titlebar(self):
        menu_widget = QWidget()
        menu_widget.setContentsMargins(0, 0, 0, 0)
        menu_widget.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        layout01 = QVBoxLayout(menu_widget)
        layout01.setContentsMargins(0, 0, 0, 0)
        layout01.addStretch(1)
        layout01.addWidget(self.ui.menubar)
        layout01.addStretch(1)
        self.main_title_widget = MainTitleWidget()
        self.main_title_widget.ui.verticalLayout_2.addWidget(menu_widget)
        self.main_title_widget.ui.full_btn.clicked.connect(self.slot_full_restore_btn)
        self.main_title_widget.ui.close_btn.clicked.connect(lambda: self.window_frame.close())
        self.main_title_widget.ui.min_btn.clicked.connect(lambda: self.window_frame.showMinimized())
        self.ui.toolBar_menu.setContentsMargins(0, 0, 0, 0)
        self.ui.toolBar_menu.addWidget(self.main_title_widget)

    # def mouseMoveEvent(self, event:QMouseEvent) -> None:
    #     super(MainWindow, self).mouseMoveEvent(event)
    #     self.setCursor(Qt.ArrowCursor)

    @Slot()
    def slot_full_restore_btn(self):
        if self.window_frame.isMaximized():
            self.window_frame.showNormal()
            self.main_title_widget.ui.full_btn.setIcon(QIcon(":/resource/ChromeMaximize_16x.svg"))
            self.main_title_widget.ui.full_btn.setToolTip("最大化")
        else:
            self.window_frame.showMaximized()
            self.main_title_widget.ui.full_btn.setIcon(QIcon(":/resource/ChromeRestore_16x.svg"))
            self.main_title_widget.ui.full_btn.setToolTip("还原")

    def updProjectCtlg(self, projectPath):
        self.projectWidget.setPath(projectPath)

    def createRecntFilePathBtn(self, file_path, create_time):
        btn = RecentContentLink(file_path, create_time)
        btn.clicked.connect(lambda: self.openFileBaseOnPath(file_path, btn))

        return btn

    def slot_click_clear_recent_btn(self):
        """
        清空最近项目列表
        """
        # In[]
        # step 1: 删除最近列表所有项
        layout = self.ui.verticalLayout_7
        count = layout.count()
        for i in reversed(range(count)):
            layout.itemAt(i).widget().deleteLater()
        # step 2: 增加两个初始项并隐藏
        current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        btn1 = RecentContentLink("c:/app/blank.afc", current_time)
        btn2 = RecentContentLink("c:/app/blank.afc", current_time)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        btn1.hide()
        btn2.hide()

    def openFileBaseOnPath(self, file_path, btn=None):
        """
        根据获得的文件路径打开相应模块并新建Tab
        """
        if os.path.exists(file_path):
            file_name = os.path.split(file_path)[-1].split('.')[0]
            file_extension = os.path.split(file_path)[-1].split('.')[1]
            tabNum = self.ui.mainContent.count()
            isExisting = False
            for i in range(0, tabNum):
                if self.ui.mainContent.widget(i).property("full_path") == file_path:
                    isExisting = True
                    self.ui.mainContent.setCurrentIndex(i)
                    break
            if not isExisting:
                #  开始新建Tab
                if file_extension == 'afc':
                    self.create_new_project(file_path, file_name)
                    # 进行计算
                    self.runCal()
                elif file_extension == 'dc':
                    #  创建数据中心计算模块
                    content = QWidget()
                    content.setProperty("full_path", file_path)
                    tabIndex = self.ui.mainContent.addTab(content, file_name)
                    # 设定为当前tab
                    self.ui.mainContent.setCurrentIndex(tabIndex)
                else:
                    self.commdLine("文件类型无法识别", showtime=True, color="#FF0000")
        else:
            if btn is not None:
                btn.ui.toolButton_rcl.setDisabled(True)
            self.commdLine("文件不存在或已经删除", showtime=True, color="#FF0000")
            self.statusBar().showMessage("文件不存在或已经删除", timeout=3000)

    @Slot()
    def slot_ProjectCtlg_was_doubleClicked(self, index):
        """
        双击项目名称，判断文件后缀名称
        :param index: 双击文件索引号
        :return: None
        """
        if self.projectWidget.isFile(index):
            file_path = self.projectWidget.showPath(index)
            self.openFileBaseOnPath(file_path)
        else:
            self.commdLine("打开文件夹")

    @Slot()
    def the_pushButton_was_clicked(self):
        # projectDock导入项目目录并更新标题
        projectPath = "C:/Users/pc080/OneDrive/1Pyside/天津1号线"
        title = "项目"  # 全路径
        # title = "项目 (%s)" % os.path.split(path)[1] #父级文件名
        # self.projectWidget.setPath(projectPath)
        self.file_bar.filepath = projectPath
        self.ui.projWin.setWindowTitle(title)

    @Slot()
    def the_openProjectbutton_was_clicked(self):
        # 获取选择文件夹的目录
        selected_directory = QFileDialog().getExistingDirectory()
        # 更新项目目录
        if selected_directory != "":
            self.updProjectCtlg(selected_directory)

    @Slot()
    def the_mainContent_was_changed(self, index):
        # 获取当前Tab文件路径，以及扩展名
        self.curTabFilePath = self.ui.mainContent.widget(index).property("full_path")
        path = self.curTabFilePath
        filename = os.path.split(path)[-1].split('.')[0]
        self.main_title_widget.setTitle(filename)

        extension = os.path.splitext(self.curTabFilePath)[1]
        path, _ = os.path.split(self.curTabFilePath)
        # 更新项目配置组件内容
        if extension == '.start':
            self.ui.configWin.hide()
            content = QTextEdit()
            content.setStyleSheet(
                "QTextEdit{background-color: rgb(240, 240, 240);border:1px solid rgb(204,206,219);"
                "margin-right:5px;margin-left:5px;margin-bottom:5px}")
            content.setReadOnly(1)
            self.ui.configWin.setWidget(content)
            # ===========删除afc组件toolbar==================
            toolbar_afc = self.ui.toolBar.findChild(AFCToolBar, 'toolbar_afc')
            if toolbar_afc is not None:
                toolbar_afc.deleteLater()

        elif extension == '.afc':
            self.ui.configWin.show()
            self.ridership_config = Ridership_Config()
            self.ridership_config.loadFile(self.curTabFilePath)
            self.ui.configWin.setWidget(self.ridership_config)
            self.ridership_config.ui.srcbutton.clicked.connect(self.the_srcbutton_was_clicked)
            # =======增加用于afc计算的toolbar栏===============
            # 步骤 1：判断是否已经存在afc toolbar widget
            toolbar_afc = self.ui.toolBar.findChild(AFCToolBar, 'toolbar_afc')
            # 步骤 2：根据存在与否决定是否在toolbar中增加widget
            if toolbar_afc is None:
                self.ui.toolBar.addWidget(AFCToolBar(self))
        if extension == '.dc':
            print("这是数据中心的库")
            self.setWindowTitle("中铁电化院自动售检票系统计算 <%s>" % self.curTabFilePath)

    @Slot()
    def the_srcbutton_was_clicked(self):
        # 获取选择文件夹的目录
        selected_file = QFileDialog().getOpenFileName()[0]
        if selected_file != '':
            self.ridership_config.ui.lineEdit.setText(selected_file)
            self.commdLine("导入客流数据<%s>" % selected_file, showtime=True)

    @Slot()
    def the_newProjectButton_was_clicked(self):
        dlg = NewProjectDlg(self)
        dlg.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        dlg.created.connect(self.create_new_project)
        dlg.exec()

    def runCal(self):
        """
        AFC客流计算主函数，先执行保存命令，然后打开保存的Json文件读取基础数据，
        调用afcCalculation.py中的ACF_project函数

        :return: None
        """
        # 初始赋值
        curTabFilePath = self.curTabFilePath
        # 索引AFC计算主Widget
        content: afc_content = self.ui.mainContent.currentWidget()
        # 保存工程配置文件
        self.saveProject()
        table_recent = []
        table_far = []

        # 计算值
        try:
            para, ridershipAddress = afcCalculation.loadParam(curTabFilePath)
            table_recent = AFC_project(file_path=ridershipAddress, tab_names=["近期早高峰客流", "近期晚高峰客流"],
                                       parameter_list=para).run()
            table_far = AFC_project(file_path=ridershipAddress, tab_names=["远期早高峰客流", "远期晚高峰客流"],
                                    parameter_list=para).run()
        except Exception:
            self.commdLine("失败！客流文件目录有误或客流文件格式有误！", showtime=True, color="#FF0000")
            return

        # 近期表格赋值
        content.setTableWidget_recent(table_recent[0], content.ui.o1tableWidget)
        content.setTableWidget_recent(table_recent[1], content.ui.o2tableWidget)
        content.setTableWidget_recent(table_recent[2], content.ui.o3tableWidget)
        content.setTableWidget_recent(table_recent[4], content.ui.o5tableWidget)
        manual_df_recent = afcCalculation.get_dataFrame("output_recent", curTabFilePath)
        if manual_df_recent is None:
            manual_df_recent = table_recent[3].copy()
        content.setTableWidget_recent(table_recent[3], content.ui.o4tableWidget, editable=1, manual_df=manual_df_recent)

        # 远期表格赋值
        content.setTableWidget_far(table_far[0], content.ui.o1tableWidget_2)
        content.setTableWidget_far(table_far[1], content.ui.o2tableWidget_2)
        content.setTableWidget_far(table_far[2], content.ui.o3tableWidget_2)
        content.setTableWidget_far(table_far[4], content.ui.o5tableWidget_2)
        manual_df_far = afcCalculation.get_dataFrame("output_far", curTabFilePath)
        if manual_df_far is None:
            manual_df_far = table_far[3].copy()
        content.setTableWidget_far(table_far[3], content.ui.o4tableWidget_2, editable=1, manual_df=manual_df_far)
        content.enable_btn()
        content.show_o4tableView()
        content.show_o4tableView_2()
        self.commdLine("近期及远期报表已生成", showtime=True)

        # self.ui.mainContent.tabText(index)
        # 展示图表
        self.commdLine("图表已生成", showtime=True)
        content.initialFigGenerator(manual_df_recent, manual_df_far)

        info = psutil.virtual_memory()
        self.commdLine(u'当前进程的内存使用: %.4f GB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024 / 1024))
        self.commdLine(u"当前电脑总内存:%.4f GB" % (info.total / 1024 / 1024 / 1024))
        self.commdLine(f"当前使用的总内存占比: {info.percent}%")
        self.commdLine(f"cpu个数: {psutil.cpu_count()}")

        return table_recent, table_far, manual_df_recent, manual_df_far

    def create_new_project(self, file_path, file_name):
        #  创建AFC计算模块
        content = afc_content(file_path)
        content.setProperty("full_path", file_path)
        tab_name = file_name
        tabIndex = self.ui.mainContent.addTab(content, tab_name)

        content.tab_name = tab_name
        content.id = self.id
        self.id = self.id + 1
        # 设定为当前tab
        self.ui.mainContent.setCurrentIndex(tabIndex)
        # In[] 更新最近清单widget:
        # 步骤1 判断是从固定清单清单是否含有该地址：
        has_address = False
        for i in reversed(range(self.ui.verticalLayout_9.count())):
            path_in_list = self.ui.verticalLayout_9.itemAt(i).widget().text()
            if path_in_list == file_path:
                has_address = True
                break
        # 步骤2 如果是固定清单含有该地址不做任何操作，如果不含有执行更新最近清单widget。
        if has_address is not True:
            current_time = time.strftime('%Y-%m-%d %H:%M', time.localtime())
            btn = self.createRecntFilePathBtn(file_path, current_time)
            widget_count = self.ui.verticalLayout_7.count()
            for i in reversed(range(widget_count)):
                path_in_list = self.ui.verticalLayout_7.itemAt(i).widget().text()
                if path_in_list == btn.text():
                    self.ui.verticalLayout_7.itemAt(i).widget().deleteLater()
                    break
            self.ui.verticalLayout_7.insertWidget(0, btn)
            if widget_count > 10:
                self.ui.verticalLayout_7.itemAt(10).widget().deleteLater()

    # In[] 保存afc计算文件:
    def save_afc_project(self, filepath):
        """
        根据路径保存afc计算文件
        """
        filename = os.path.split(filepath)[-1]
        with open(filepath, 'r') as f:
            json_data = json.load(f)
            json_data['gate']['passRate'] = self.ridership_config.ui.G1.value()
            json_data['gate']['peakTrainPairs'] = self.ridership_config.ui.G2.value()
            json_data['gate']['minNum'] = self.ridership_config.ui.G3.value()
            json_data['gate']['maxNum'] = self.ridership_config.ui.G4.value()
            json_data['vendingMachine']['tktProcessingCap'] = self.ridership_config.ui.S1.value()
            json_data['vendingMachine']['minNum'] = self.ridership_config.ui.S2.value()
            json_data['vendingMachine']['rateOfRecentUse'] = self.ridership_config.ui.S3.value()
            json_data['vendingMachine']['rateOfFutureUse'] = self.ridership_config.ui.S4.value()
            json_data['ridershipAddress'] = self.ridership_config.ui.lineEdit.text()
        with open(filepath, 'w') as f:
            f.write(json.dumps(json_data))
        self.commdLine(f"保存文件 ({filename})", showtime=True)

    @Slot()
    def saveProject(self):
        """
        保存AFC计算工程
        :return: None
        """
        filepath = self.curTabFilePath
        self.save_afc_project(filepath)

    def saveProjectOnCLose(self, filepath):
        self.save_afc_project(filepath)

    @Slot()
    def close_tab(self, index):
        content: afc_content = self.ui.mainContent.widget(index)
        if content.type == 'start':
            print("开始界面无法关闭")
        if content.type == 'afc':
            self.saveProjectOnCLose(content.filepath)
            self.ui.mainContent.removeTab(index)
        # self.commdLine(f"图表展示引擎已关闭 (http://127.0.0.1:{content.port})", showtime=True, color="#FF0000")  # 红色

    def commdLine(self, text, showtime=False, color="#000000"):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if showtime is True:
            self.ui.textEdit.append(f"<div style='color:{color}'> {currentTime} {text}</div>")
        else:
            self.ui.textEdit.append(f"<div style='color:{color}'> {text}</div>")
