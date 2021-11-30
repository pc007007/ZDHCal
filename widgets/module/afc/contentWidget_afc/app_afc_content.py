from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QFileDialog, QComboBox, QRadioButton, \
    QLabel
from PySide6.QtCore import Qt, Slot, QUrl, QObject, Signal, QThread
from PySide6 import QtWidgets, QtGui
from PySide6.QtWebEngineWidgets import QWebEngineView
from tools.customWidget import QComboCheckBox
from widgets.module.afc.contentWidget_afc.ui.afcCalMain import Ui_afcCalMain
import pandas as pd
import tools.afcCalculationV2 as afcCalculation
import decimal
import os
import plotly_express as px
# import dtale


# class Report(QObject):
#     finished = Signal(str)
#
#     def __init__(self, manual_df, id):
#         super(Report, self).__init__()
#         self.manual_df = manual_df
#         self.id = id
#
#     def run(self):
#         self.d = dtale.show(self.manual_df)
#         print("已完成服务器启动")
#         url = dtale.get_instance(self.id).main_url()
#         self.finished.emit(url)


class WebEngineView(QWebEngineView):
    def createWindow(self,QWebEnginePage_WebWindowType):

        page = WebEngineView(self)
        page.urlChanged.connect(self.on_url_changed)
        return page

    def on_url_changed(self,url):
        self.setUrl(url)


class afc_content(QWidget):
    def __init__(self, filepath):
        super().__init__()
        self.ui = Ui_afcCalMain()
        self.ui.setupUi(self)

        # 初始赋值
        self.type = 'afc'
        self.filepath = filepath
        self.filename = os.path.split(filepath)[-1].split('.')[0]

        self.manual_df_recent = pd.DataFrame()
        self.df_recent = pd.DataFrame()
        self.manual_df_far = pd.DataFrame()
        self.df_far = pd.DataFrame()
        self.previousValue = ''
        self.changed = False
        self.table_recent = []
        self.table_far = []
        self.index = 0  # 当前AFC content的tab序号
        self.tab_name = ''  # 当前AFC content的tab名称
        self.close_tab_name = ''  # 当前关闭的AFC content的tab名称
        self.id = 1

        self.web_view_01 = QWebEngineView()
        self.web_view_02 = QWebEngineView()
        self.web_view_03 = QWebEngineView()
        self.web_view_exp = WebEngineView()
        # 初始模块配置
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.o1Btn.setDisabled(True)
        self.ui.o2Btn.setDisabled(True)
        self.ui.o3Btn.setDisabled(True)
        self.ui.o4Btn.setDisabled(True)
        self.ui.o5Btn.setDisabled(True)
        stylesheet = "::section{" \
                     "Background-color:white ;" \
                     "border:1px solid #E0DDDC; " \
                     "border-left:0px solid #E0DDDC;" \
                     "border-top:0px solid #E0DDDC;" \
                     "border-bottom:0px solid #E0DDDC;" \
                     "}"
        self.ui.o1tableWidget.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o2tableWidget.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o3tableWidget.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o4tableWidget.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o5tableWidget.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o1tableWidget_2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o2tableWidget_2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o3tableWidget_2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o4tableWidget_2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o5tableWidget_2.verticalHeader().setStyleSheet(stylesheet)
        self.ui.o1Btn_2.setDisabled(True)
        self.ui.o2Btn_2.setDisabled(True)
        self.ui.o3Btn_2.setDisabled(True)
        self.ui.o4Btn_2.setDisabled(True)
        self.ui.o5Btn_2.setDisabled(True)

        # 装载模块

        self.ui.verticalLayout_30.addWidget(self.web_view_01)
        self.ui.verticalLayout_30.addWidget(self.web_view_02)
        self.x_combo_checkbox_bar = QComboCheckBox()
        self.y_combo_checkbox_bar = QComboCheckBox()
        self.x_combo_checkbox_bar.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.y_combo_checkbox_bar.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.ui.verticalLayout_16.addWidget(self.x_combo_checkbox_bar)
        self.ui.verticalLayout_17.addWidget(self.y_combo_checkbox_bar)
        self.dim_combo_checkbox_parallel = QComboCheckBox()
        self.dim_combo_checkbox_parallel.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.ui.verticalLayout_14.addWidget(self.dim_combo_checkbox_parallel)
        self.ui.tabWidget_2.setCurrentIndex(0)
        self.ui.tabWidget_2.tabBar().hide()

        self.ui.tabWidget.removeTab(3)

        self.initSlot()

    def initSlot(self):
        # 信号槽
        self.ui.o1Btn.clicked.connect(self.show_o1tableView)
        self.ui.o2Btn.clicked.connect(self.show_o2tableView)
        self.ui.o3Btn.clicked.connect(self.show_o3tableView)
        self.ui.o4Btn.clicked.connect(self.show_o4tableView)
        self.ui.o5Btn.clicked.connect(self.show_o5tableView)

        self.ui.o1Btn_2.clicked.connect(self.show_o1tableView_2)
        self.ui.o2Btn_2.clicked.connect(self.show_o2tableView_2)
        self.ui.o3Btn_2.clicked.connect(self.show_o3tableView_2)
        self.ui.o4Btn_2.clicked.connect(self.show_o4tableView_2)
        self.ui.o5Btn_2.clicked.connect(self.show_o5tableView_2)

        self.ui.toExcelBtn.clicked.connect(self.toExcel_recent)
        self.ui.toExcelBtn_2.clicked.connect(self.toExcel_far)
        self.ui.generate_bar_button.clicked.connect(self.slot_generate_bar_figure)
        self.dim_combo_checkbox_parallel.editTextChanged.connect(self.slot_update_color_combobox)
        self.ui.generate_parallel_button.clicked.connect(self.slot_generate_parallel_figure)
        self.ui.generate_pie_button.clicked.connect(self.slot_generate_pie_figure)
        self.ui.comboBox.currentIndexChanged.connect(self.slot_select_fig_type)

        # self.ui.exp_button.clicked.connect(self.slot_generate_exp_report)

    def initialLoadHtml(self, df, name):
        self.initialFigGenerator(df, name)

    def initialFigGenerator(self, df_recent, df_far, show=True):
        self.manual_df_recent = df_recent
        self.manual_df_far = df_far
        title_01 = "近期图表"
        filename_01 = f"{self.filename}-近期图表"
        title_02 = "远期图表"
        filename_02 = f"{self.filename}-远期图表"

        html_path_01 = self.createFigureFilePath(filename_01)
        html_path_02 = self.createFigureFilePath(filename_02)

        # df_recent.loc['莫阳路站':'莫阳路站'] # 单行值
        indexs = df_recent.index.tolist()
        columns = df_recent.columns.tolist()
        self.x_combo_checkbox_bar.add_items(indexs)
        self.y_combo_checkbox_bar.add_items(columns)
        self.y_combo_checkbox_bar.select_texts(columns, state=False)
        self.y_combo_checkbox_bar.select_texts(['进站检票机', '出站检票机', '双向检票机', '双向检票机\n(宽)'])

        self.dim_combo_checkbox_parallel.add_items(columns)

        x_list = self.x_combo_checkbox_bar.get_selected_text_list()
        y_list = self.y_combo_checkbox_bar.get_selected_text_list()

        t = self.ui.mode_combo_box.currentText()
        if t == '堆叠':
            mode = 'stack'
        if t == '组合':
            mode = 'group'


        fig01 = px.bar(df_recent.loc[x_list,:], y=y_list,
                       labels=dict(index="车站名称", variable='设备', value='值'),
                       title=title_01,
                       barmode=mode
                       )

        fig02 = px.bar(df_far.loc[x_list,:], y=y_list,
                       labels=dict(index="车站名称", variable='设备', value='值'),
                       title=title_02,
                       barmode=mode
                       )

        fig01.write_html(html_path_01)
        fig02.write_html(html_path_02)

        if show:
            self.web_view_01.load(QUrl(html_path_01))
            self.web_view_02.load(QUrl(html_path_02))

    @Slot()
    def slot_select_fig_type(self, index):
        self.ui.tabWidget_2.setCurrentIndex(index)

    @Slot()
    def slot_generate_bar_figure(self):
        df_recent = self.df_recent
        df_far = self.df_far
        title_01 = "近期图表"
        filename_01 = f"{self.filename}-近期图表"
        title_02 = "远期图表"
        filename_02 = f"{self.filename}-远期图表"
        html_path_01 = self.createFigureFilePath(filename_01)
        html_path_02 = self.createFigureFilePath(filename_02)

        x_list = self.x_combo_checkbox_bar.get_selected_text_list()
        y_list = self.y_combo_checkbox_bar.get_selected_text_list()

        t = self.ui.mode_combo_box.currentText()
        if t == '堆叠':
            mode = 'stack'
        if t == '组合':
            mode = 'group'

        fig01 = px.bar(df_recent.loc[x_list, :], y=y_list,
                       labels=dict(index="车站名称", variable='设备', value='值'),
                       title=title_01,
                       barmode=mode
                       )

        fig02 = px.bar(df_far.loc[x_list, :], y=y_list,
                       labels=dict(index="车站名称", variable='设备', value='值'),
                       title=title_02,
                       barmode=mode
                       )

        fig01.write_html(html_path_01)
        fig02.write_html(html_path_02)

        self.web_view_01.load(QUrl(html_path_01))
        self.web_view_02.load(QUrl(html_path_02))

    @Slot()
    def slot_update_color_combobox(self):
        items = self.dim_combo_checkbox_parallel.get_selected_text_list()
        num = self.ui.verticalLayout_18.count()
        for i in reversed(range(num)):
            self.ui.verticalLayout_18.itemAt(i).widget().setParent(None)
        for t in items:
            radio_button = QRadioButton(t)
            self.ui.verticalLayout_18.addWidget(radio_button)
            radio_button.setChecked(1)

    @Slot()
    def slot_generate_parallel_figure(self):
        df_recent = self.df_recent
        df_far = self.df_far
        title_01 = "近期图表"
        filename_01 = f"{self.filename}-近期图表"
        title_02 = "远期图表"
        filename_02 = f"{self.filename}-远期图表"
        html_path_01 = self.createFigureFilePath(filename_01)
        html_path_02 = self.createFigureFilePath(filename_02)

        y_list = self.dim_combo_checkbox_parallel.get_selected_text_list()
        color_type = self.get_parallel_color()
        fig01 = px.parallel_categories(df_recent, dimensions=y_list,
                                       title=title_01,
                                       color=color_type)
        fig02 = px.parallel_categories(df_far, dimensions=y_list,
                                       title=title_02,
                                       color=color_type)

        fig01.write_html(html_path_01)
        fig02.write_html(html_path_02)

        self.web_view_01.load(QUrl(html_path_01))
        self.web_view_02.load(QUrl(html_path_02))

    @Slot()
    def slot_generate_pie_figure(self):
        df_recent = self.df_recent
        df_far = self.df_far

        title_01 = "近期图表"
        filename_01 = f"{self.filename}-近期图表"
        title_02 = "远期图表"
        filename_02 = f"{self.filename}-远期图表"
        html_path_01 = self.createFigureFilePath(filename_01)
        html_path_02 = self.createFigureFilePath(filename_02)

        value = self.get_pie_value()

        fig01 = px.pie(df_recent, values=value,names=value, title=title_01)
        fig02 = px.pie(df_far, values=value,names=value, title=title_02)

        fig01.write_html(html_path_01)
        fig02.write_html(html_path_02)

        self.web_view_01.load(QUrl(html_path_01))
        self.web_view_02.load(QUrl(html_path_02))

    # @Slot()
    # def slot_generate_exp_report(self):
    #     self.ui.exp_button.setText("报告生成中...")
    #     self.ui.exp_button.setDisabled(1)
    #
    #     pixmap_gif = QtGui.QMovie(u":/resource/loading.gif")
    #     loading_label = QLabel()
    #     loading_label.setAlignment(Qt.AlignCenter)
    #     loading_label.setMovie(pixmap_gif)
    #     pixmap_gif.start()
    #     self.ui.verticalLayout_21.addWidget(loading_label)
    #
    #     self.thread = QThread()
    #     self.report = Report(self.manual_df_recent, self.id)
    #     self.report.moveToThread(self.thread)
    #     self.thread.started.connect(self.report.run)
    #     self.report.finished.connect(lambda: self.ui.exp_button.deleteLater())
    #     self.report.finished.connect(lambda: self.ui.verticalLayout_21.addWidget(self.web_view_exp))
    #     self.report.finished.connect(lambda: loading_label.deleteLater())
    #     self.report.finished.connect(lambda url: self.web_view_exp.load(QUrl(url)))
    #     self.thread.start()

        # d = dtale.show(self.manual_df_recent, port=self.port, force=True)
        # self.web_view_exp.load(QUrl(d._url))


    def get_parallel_color(self):
        num = self.ui.verticalLayout_18.count()
        for i in range(num):
            radio_boutton = self.ui.verticalLayout_18.itemAt(i).widget()
            if radio_boutton.isChecked():
                return radio_boutton.text()
        return None

    def get_pie_value(self):
        num = self.ui.verticalLayout_28.count()
        for i in range(num):
            radio_boutton = self.ui.verticalLayout_28.itemAt(i).widget()
            if radio_boutton.isChecked():
                return radio_boutton.text()
        return None

    def createFig(self, df, name, show=True):
        html_path_01 = self.createFigureFilePath(name + "01")
        html_path_02 = self.createFigureFilePath(name + "02")

        fig = px.parallel_categories(df)
        fig.write_html(html_path_01)
        fig.write_html(html_path_02)

        if show:
            self.web_view_01.load(QUrl(html_path_01))
            self.web_view_02.load(QUrl(html_path_02))

    def createFigureFilePath(self, name):
        base_path = os.path.dirname(self.filepath)
        folder_path = base_path + "/figure"
        folder = os.path.exists(folder_path)
        if not folder:
            print("创建文件夹" + folder_path)
            os.makedirs(folder_path)
        else:
            print("文件夹已存在!")
        html_path = folder_path + "/" + name + ".html"
        return html_path

    def setTableWidget_recent(self, df: pd.DataFrame, table: QTableWidget, editable=0,
                              manual_df=pd.DataFrame(['apple'])):
        """
        :param editable: 是否可以编辑
        :param df: dataframe格式的自动计算输出文件
        :param manual_df: dataframe格式的手动调节计算输出文件
        :param table: 需要展示在的tablewidget
        :return: None
        """
        self.manual_df_recent = manual_df
        self.df_recent = df

        rowCount = len(df.index)
        colCount = len(df.columns)
        if editable == 1:
            table.setColumnCount(colCount - 4)
        if editable == 0:
            table.setColumnCount(colCount)
        table.setRowCount(rowCount)
        table.setHorizontalHeaderLabels(df.columns.tolist())
        table.setVerticalHeaderLabels(df.index.tolist())
        table.setAlternatingRowColors(True)

        if editable:
            table.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)
        else:
            table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        if len(manual_df.index) == len(df.index):
            flag = True
        else:
            flag = False

        for i in range(rowCount):
            for j in range(colCount):
                if editable == 1:
                    if j <= 3:
                        if flag:
                            cal_value = decimal.Decimal(str(df.iloc[i, j])).quantize(decimal.Decimal('0.00'),
                                                                                     rounding=decimal.ROUND_HALF_UP)
                            manual_value = decimal.Decimal(str(manual_df.iloc[i, j])).quantize(decimal.Decimal('0.00'),
                                                                                               rounding=decimal.ROUND_HALF_UP)
                            if cal_value == manual_value:
                                data = QTableWidgetItem(str(df.iloc[i, j]))
                                data.setTextAlignment(Qt.AlignCenter)
                                table.setItem(i, j, data)
                            else:
                                x1 = df.iloc[i, j]
                                x2 = manual_df.iloc[i, j]
                                data = QTableWidgetItem(str(x2) + "(" + str(x1) + ")")
                                data.setTextAlignment(Qt.AlignCenter)
                                data.setForeground(QtGui.QColor('red'))
                                table.setItem(i, j, data)
                        else:
                            x = manual_df.iloc[i, j]
                            data = QTableWidgetItem(str(x))
                            data.setTextAlignment(Qt.AlignCenter)
                            table.setItem(i, j, data)
                    else:
                        x = manual_df.iloc[i, j]
                        if j != 4 and j!= 7:
                            x = decimal.Decimal(str(x)).quantize(decimal.Decimal('0.00'),
                                                                 rounding=decimal.ROUND_HALF_UP)
                        data = QTableWidgetItem(str(x))
                        if x <= 30 and j == 6:
                            data.setBackground(QBrush(QColor("yellow")))
                        else:
                            data.setBackground(QBrush(QColor(245, 245, 245)))
                        data.setTextAlignment(Qt.AlignCenter)
                        data.setFlags(Qt.ItemIsEnabled)
                        table.setItem(i, j, data)
                if editable == 0:
                    x = df.iloc[i, j]
                    data = QTableWidgetItem(str(x))
                    data.setTextAlignment(Qt.AlignCenter)
                    table.setItem(i, j, data)

        table.resizeColumnsToContents()
        table.cellChanged.connect(self.onCellChanged)
        table.cellDoubleClicked.connect(self.onCellDoubleClicked)

    @Slot()
    def onCellChanged(self, row, column):
        if self.changed:
            self.changed = False
            """
            步骤1：更新并保存调整的单元格
            """
            input_text = self.ui.o4tableWidget.item(row, column).text()
            cal_value = self.df_recent.copy().iloc[row, column]
            self.manual_df_recent.iloc[row, column] = input_text
            if int(input_text) != int(cal_value):
                data = QTableWidgetItem(f"{input_text}({cal_value})")
                data.setTextAlignment(Qt.AlignCenter)
                data.setForeground(QtGui.QColor('red'))
                self.ui.o4tableWidget.setItem(row, column, data)
            else:
                data = QTableWidgetItem(str(input_text))
                data.setTextAlignment(Qt.AlignCenter)
                data.setForeground(QtGui.QColor('black'))
                self.ui.o4tableWidget.setItem(row, column, data)
            """
            步骤2：手动调整出站检票机的数量
            """
            if column == 1:
                num_gate_total = int(int(input_text) + int(self.manual_df_recent.iloc[row, 2])/2 + int(self.manual_df_recent.iloc[row, 3])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget.setItem(row, 4, data)

                self.manual_df_recent.iloc[row, 4] = str(num_gate_total)
            """
            步骤3：手动调整双向检票机的数量
            """
            if column == 2:
                num_gate_total = int(int(input_text)/2 + int(self.manual_df_recent.iloc[row, 1]) + int(self.manual_df_recent.iloc[row, 3])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget.setItem(row, 4, data)
                self.manual_df_recent.iloc[row, 4] = str(num_gate_total)
            """
            步骤4：手动调整双向检票机(宽)的数量
            """
            if column == 3:
                num_gate_total = int(int(input_text)/2 + int(self.manual_df_recent.iloc[row, 1]) + int(self.manual_df_recent.iloc[row, 2])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget.setItem(row, 4, data)
                self.manual_df_recent.iloc[row, 4] = str(num_gate_total)
            """
            步骤5：调整自动检票机通过时间及空闲时间
            """
            tktGateRlTm = float(self.manual_df_recent.iloc[row, 9]) / float(self.manual_df_recent.iloc[row, 11]) / \
                              float(self.ui.o4tableWidget.item(row, 4).text())
            tktGateRlTm = decimal.Decimal(str(tktGateRlTm)).quantize(decimal.Decimal('0.00'),
                                                                     rounding=decimal.ROUND_HALF_UP)
            data_tktGateRlTm = QTableWidgetItem(str(tktGateRlTm))
            data_tktGateRlTm.setTextAlignment(Qt.AlignCenter)
            data_tktGateRlTm.setBackground(QtGui.QColor(245, 245, 245))
            self.ui.o4tableWidget.setItem(row, 5, data_tktGateRlTm)
            self.manual_df_recent.iloc[row, 5] = str(tktGateRlTm)

            spare_time = (float(self.manual_df_recent.iloc[row, 8])-float(tktGateRlTm))*60
            spare_time = decimal.Decimal(str(spare_time)).quantize(decimal.Decimal('0.00'),
                                                                     rounding=decimal.ROUND_HALF_UP)
            data_tktGateRlTm = QTableWidgetItem(str(spare_time))
            data_tktGateRlTm.setTextAlignment(Qt.AlignCenter)
            if float(spare_time) <= 30:
                data_tktGateRlTm.setBackground(QtGui.QColor("yellow"))
            else:
                data_tktGateRlTm.setBackground(QtGui.QColor(245, 245, 245))
            self.ui.o4tableWidget.setItem(row, 6, data_tktGateRlTm)
            self.manual_df_recent.iloc[row, 6] = str(spare_time)

            """
            步骤3：保存手动调整的值
            """
            afcCalculation.save_dataFrame(self.manual_df_recent, 'output_recent', file_name=self.filepath)

    @Slot()
    def onCellDoubleClicked(self, row, column):
        # self.previousValue = self.manual_df_recent.iloc[row, column]
        self.changed = True

    def setTableWidget_far(self, df: pd.DataFrame, table: QTableWidget, editable=0, manual_df=pd.DataFrame(['apple'])):
        """
        :param editable: 是否可以编辑
        :param df: dataframe格式的自动计算输出文件
        :param manual_df: dataframe格式的手动调节计算输出文件
        :param table: 需要展示在的tablewidget
        :return: None
        """
        self.manual_df_far = manual_df
        self.df_far = df

        rowCount = len(df.index)
        colCount = len(df.columns)
        if editable == 1:
            table.setColumnCount(colCount - 4)
        if editable == 0:
            table.setColumnCount(colCount)
        table.setRowCount(rowCount)
        table.setHorizontalHeaderLabels(df.columns.tolist())
        table.setVerticalHeaderLabels(df.index.tolist())
        table.setAlternatingRowColors(True)

        if editable:
            table.setEditTriggers(QtWidgets.QTableWidget.DoubleClicked)
        else:
            table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        if len(manual_df.index) == len(df.index):
            flag = True
        else:
            flag = False

        for i in range(rowCount):
            for j in range(colCount):
                if editable == 1:
                    if j <= 3:
                        if flag:
                            cal_value = decimal.Decimal(str(df.iloc[i, j])).quantize(decimal.Decimal('0.00'),
                                                                                     rounding=decimal.ROUND_HALF_UP)
                            manual_value = decimal.Decimal(str(manual_df.iloc[i, j])).quantize(decimal.Decimal('0.00'),
                                                                                               rounding=decimal.ROUND_HALF_UP)
                            if cal_value == manual_value:
                                data = QTableWidgetItem(str(df.iloc[i, j]))
                                data.setTextAlignment(Qt.AlignCenter)
                                table.setItem(i, j, data)
                            else:
                                x1 = df.iloc[i, j]
                                x2 = manual_df.iloc[i, j]
                                data = QTableWidgetItem(str(x2) + "(" + str(x1) + ")")
                                data.setTextAlignment(Qt.AlignCenter)
                                data.setForeground(QtGui.QColor('red'))
                                table.setItem(i, j, data)
                        else:
                            x = manual_df.iloc[i, j]
                            data = QTableWidgetItem(str(x))
                            data.setTextAlignment(Qt.AlignCenter)
                            table.setItem(i, j, data)
                    else:
                        x = manual_df.iloc[i, j]
                        if j != 4 and j!= 7:
                            x = decimal.Decimal(str(x)).quantize(decimal.Decimal('0.00'),
                                                                 rounding=decimal.ROUND_HALF_UP)
                        data = QTableWidgetItem(str(x))
                        if x <= 30 and j == 6:
                            data.setBackground(QBrush(QColor("yellow")))
                        else:
                            data.setBackground(QBrush(QColor(245, 245, 245)))
                        data.setTextAlignment(Qt.AlignCenter)
                        data.setFlags(Qt.ItemIsEnabled)
                        table.setItem(i, j, data)
                if editable == 0:
                    x = df.iloc[i, j]
                    data = QTableWidgetItem(str(x))
                    data.setTextAlignment(Qt.AlignCenter)
                    table.setItem(i, j, data)

        table.resizeColumnsToContents()
        table.cellChanged.connect(self.onCellChanged_far)
        table.cellDoubleClicked.connect(self.onCellDoubleClicked_far)

    @Slot()
    def onCellChanged_far(self, row, column):
        if self.changed:
            self.changed = False
            """
            步骤1：更新并保存调整的单元格
            """
            input_text = self.ui.o4tableWidget_2.item(row, column).text()
            cal_value = self.df_far.copy().iloc[row, column]
            self.manual_df_far.iloc[row, column] = input_text
            if int(input_text) != int(cal_value):
                data = QTableWidgetItem(f"{input_text}({cal_value})")
                data.setTextAlignment(Qt.AlignCenter)
                data.setForeground(QtGui.QColor('red'))
                self.ui.o4tableWidget_2.setItem(row, column, data)
            else:
                data = QTableWidgetItem(str(input_text))
                data.setTextAlignment(Qt.AlignCenter)
                data.setForeground(QtGui.QColor('black'))
                self.ui.o4tableWidget_2.setItem(row, column, data)
            """
            步骤2：手动调整出站检票机的数量
            """
            if column == 1:
                num_gate_total = int(int(input_text) + int(self.manual_df_far.iloc[row, 2])/2 + int(self.manual_df_far.iloc[row, 3])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget_2.setItem(row, 4, data)

                self.manual_df_far.iloc[row, 4] = str(num_gate_total)
            """
            步骤3：手动调整双向检票机的数量
            """
            if column == 2:
                num_gate_total = int(int(input_text)/2 + int(self.manual_df_far.iloc[row, 1]) + int(self.manual_df_far.iloc[row, 3])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget_2.setItem(row, 4, data)
                self.manual_df_far.iloc[row, 4] = str(num_gate_total)
            """
            步骤4：手动调整双向检票机(宽)的数量
            """
            if column == 3:
                num_gate_total = int(int(input_text)/2 + int(self.manual_df_far.iloc[row, 1]) + int(self.manual_df_far.iloc[row, 2])/2)
                data = QTableWidgetItem(str(num_gate_total))
                data.setTextAlignment(Qt.AlignCenter)
                data.setBackground(QtGui.QColor(245, 245, 245))
                self.ui.o4tableWidget_2.setItem(row, 4, data)
                self.manual_df_far.iloc[row, 4] = str(num_gate_total)
            """
            步骤5：调整自动检票机通过时间及空闲时间
            """
            tktGateRlTm = float(self.manual_df_far.iloc[row, 9]) / float(self.manual_df_far.iloc[row, 11]) / \
                              float(self.ui.o4tableWidget_2.item(row, 4).text())
            tktGateRlTm = decimal.Decimal(str(tktGateRlTm)).quantize(decimal.Decimal('0.00'),
                                                                     rounding=decimal.ROUND_HALF_UP)
            data_tktGateRlTm = QTableWidgetItem(str(tktGateRlTm))
            data_tktGateRlTm.setTextAlignment(Qt.AlignCenter)
            data_tktGateRlTm.setBackground(QtGui.QColor(245, 245, 245))
            self.ui.o4tableWidget_2.setItem(row, 5, data_tktGateRlTm)
            self.manual_df_far.iloc[row, 5] = str(tktGateRlTm)

            spare_time = (float(self.manual_df_far.iloc[row, 8])-float(tktGateRlTm))*60
            spare_time = decimal.Decimal(str(spare_time)).quantize(decimal.Decimal('0.00'),
                                                                     rounding=decimal.ROUND_HALF_UP)
            data_tktGateRlTm = QTableWidgetItem(str(spare_time))
            data_tktGateRlTm.setTextAlignment(Qt.AlignCenter)
            if float(spare_time) <= 30:
                data_tktGateRlTm.setBackground(QtGui.QColor("yellow"))
            else:
                data_tktGateRlTm.setBackground(QtGui.QColor(245, 245, 245))
            self.ui.o4tableWidget_2.setItem(row, 6, data_tktGateRlTm)
            self.manual_df_far.iloc[row, 6] = str(spare_time)

            """
            步骤3：保存手动调整的值
            """
            afcCalculation.save_dataFrame(self.manual_df_far, 'output_far', file_name=self.filepath)

    @Slot()
    def onCellDoubleClicked_far(self, row, column):
        self.previousValue = self.ui.o4tableWidget_2.item(row, column).text()
        self.changed = True

    @Slot()
    def show_o1tableView(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.o1Btn.setChecked(True)
        self.ui.o2Btn.setChecked(False)
        self.ui.o3Btn.setChecked(False)
        self.ui.o4Btn.setChecked(False)
        self.ui.o5Btn.setChecked(False)

    @Slot()
    def show_o2tableView(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.o1Btn.setChecked(False)
        self.ui.o2Btn.setChecked(True)
        self.ui.o3Btn.setChecked(False)
        self.ui.o4Btn.setChecked(False)
        self.ui.o5Btn.setChecked(False)

    @Slot()
    def show_o3tableView(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.o1Btn.setChecked(False)
        self.ui.o2Btn.setChecked(False)
        self.ui.o3Btn.setChecked(True)
        self.ui.o4Btn.setChecked(False)
        self.ui.o5Btn.setChecked(False)

    @Slot()
    def show_o4tableView(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.o1Btn.setChecked(False)
        self.ui.o2Btn.setChecked(False)
        self.ui.o3Btn.setChecked(False)
        self.ui.o4Btn.setChecked(True)
        self.ui.o5Btn.setChecked(False)

    @Slot()
    def show_o5tableView(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.o1Btn.setChecked(False)
        self.ui.o2Btn.setChecked(False)
        self.ui.o3Btn.setChecked(False)
        self.ui.o4Btn.setChecked(False)
        self.ui.o5Btn.setChecked(True)

    @Slot()
    def show_o1tableView_2(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.o1Btn_2.setChecked(True)
        self.ui.o2Btn_2.setChecked(False)
        self.ui.o3Btn_2.setChecked(False)
        self.ui.o4Btn_2.setChecked(False)
        self.ui.o5Btn_2.setChecked(False)

    @Slot()
    def show_o2tableView_2(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.o1Btn_2.setChecked(False)
        self.ui.o2Btn_2.setChecked(True)
        self.ui.o3Btn_2.setChecked(False)
        self.ui.o4Btn_2.setChecked(False)
        self.ui.o5Btn_2.setChecked(False)

    @Slot()
    def show_o3tableView_2(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
        self.ui.o1Btn_2.setChecked(False)
        self.ui.o2Btn_2.setChecked(False)
        self.ui.o3Btn_2.setChecked(True)
        self.ui.o4Btn_2.setChecked(False)
        self.ui.o5Btn_2.setChecked(False)

    @Slot()
    def show_o4tableView_2(self):
        self.ui.stackedWidget_2.setCurrentIndex(3)
        self.ui.o1Btn_2.setChecked(False)
        self.ui.o2Btn_2.setChecked(False)
        self.ui.o3Btn_2.setChecked(False)
        self.ui.o4Btn_2.setChecked(True)
        self.ui.o5Btn_2.setChecked(False)

    @Slot()
    def show_o5tableView_2(self):
        self.ui.stackedWidget_2.setCurrentIndex(4)
        self.ui.o1Btn_2.setChecked(False)
        self.ui.o2Btn_2.setChecked(False)
        self.ui.o3Btn_2.setChecked(False)
        self.ui.o4Btn_2.setChecked(False)
        self.ui.o5Btn_2.setChecked(True)

    def enable_btn(self):
        """
        按钮使能

        :return: None
        """
        self.ui.o1Btn.setDisabled(False)
        self.ui.o2Btn.setDisabled(False)
        self.ui.o3Btn.setDisabled(False)
        self.ui.o4Btn.setDisabled(False)
        self.ui.o5Btn.setDisabled(False)
        self.ui.o1Btn_2.setDisabled(False)
        self.ui.o2Btn_2.setDisabled(False)
        self.ui.o3Btn_2.setDisabled(False)
        self.ui.o4Btn_2.setDisabled(False)
        self.ui.o5Btn_2.setDisabled(False)

    @Slot()
    def toExcel_recent(self):
        # 获取保存文件路径
        filename = f'近期客流计算结果({os.path.basename(os.path.splitext(self.filepath)[0])})'
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            '导出到Excel',
            filename,
            "AFC计算结果文件 (*.xlsx)"
        )
        if filepath != '':
            # 计算结果导出
            para, ridershipAddress = afcCalculation.loadParam(self.filepath)
            self.table_recent = afcCalculation.AFC_project(file_path=ridershipAddress, tab_names=["近期早高峰客流", "近期晚高峰客流"],
                                                           parameter_list=para).run()
            manual_output = afcCalculation.get_dataFrame('output_recent', self.filepath)

            if manual_output is None:
                manual_output = self.table_recent[3]
            afcCalculation.output_excel(filepath, self.table_recent, manual_output)

    @Slot()
    def toExcel_far(self):
        # 获取保存文件路径
        filename = f'远期客流计算结果({os.path.basename(os.path.splitext(self.filepath)[0])})'
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            '导出到Excel',
            filename,
            "AFC计算结果文件 (*.xlsx)"
        )
        if filepath != '':
            # 计算结果导出
            para, ridershipAddress = afcCalculation.loadParam(self.filepath)
            self.table_far = afcCalculation.AFC_project(file_path=ridershipAddress, tab_names=["远期早高峰客流", "远期晚高峰客流"],
                                                        parameter_list=para).run()
            manual_output = afcCalculation.get_dataFrame('output_far', self.filepath)
            if manual_output is None:
                manual_output = self.table_far[3]
            afcCalculation.output_excel(filepath, self.table_far, manual_output)
