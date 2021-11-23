import time

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import QSize, QTimer
from PySide6.QtGui import Qt, QMouseEvent, QStandardItemModel, QStandardItem, QFont, QFontMetrics, QMovie, QMoveEvent, \
    QResizeEvent, QCloseEvent, QPaintEvent
from PySide6.QtWidgets import QSplashScreen, QComboBox, QListView, QWidget, QLineEdit, QListWidgetItem, QCheckBox, \
    QListWidget, QMainWindow, QLabel, QHBoxLayout


class SplashScreen(QSplashScreen):
    def __init__(self, gif_path):
        self.pixmap = QtGui.QPixmap(gif_path)
        self.pixmap_gif = QtGui.QMovie(gif_path)

        super().__init__(self.pixmap)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setEnabled(False)
        self.setGif()
        self.showMessage("<h1><font color='white'>这里应该显示文字</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.white)

    def setGif(self):
        splashlabel = QtWidgets.QLabel(self)
        splashgif = self.pixmap_gif
        splashlabel.setMovie(splashgif)
        splashgif.start()

    def effect(self, app, delay_time=1):
        self.show()
        self.setWindowOpacity(0)
        timer = QtCore.QElapsedTimer()
        timer.start()
        delay_time_ms = delay_time * 1000
        while timer.elapsed() < delay_time_ms:
            while timer.elapsed() < 350:
                self.setWindowOpacity(timer.elapsed() / 350)
            app.processEvents()


def show_text(function):
    def wrapped(self, *args, **kwargs):
        if self.vars["showTextLock"]:
            self.vars["showTextLock"] = False
            result = function(self, *args, **kwargs)
            items = self.get_selected()
            l = len(items)
            l_ = self.vars["listViewModel"].rowCount() - 1
            self.vars["listViewModel"].item(0).setCheckState(
                Qt.Checked if l == l_ else Qt.Unchecked if l == 0 else Qt.PartiallyChecked)
            self.vars["lineEdit"].setText(
                "(全选)" if l == l_ else "(无选择)" if l == 0 else ";".join((item.text() for item in items)))
            self.vars["showTextLock"] = True
        else:
            result = function(self, *args, **kwargs)
        return result

    return wrapped


class QComboCheckBox(QComboBox):
    class MyListView(QListView):
        def __init__(self, parent: QWidget = None, vars=None):
            super().__init__(parent)
            self.vars = vars

        def mousePressEvent(self, event: QMouseEvent):
            self.vars["lock"] = False
            super().mousePressEvent(event)

        def mouseDoubleClickEvent(self, event: QMouseEvent):
            self.vars["lock"] = False
            super().mouseDoubleClickEvent(event)

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.vars = dict()
        self.vars["lock"] = True
        self.vars["showTextLock"] = True
        # 装饰器锁，避免批量操作时重复改变lineEdit的显示
        self.vars["lineEdit"] = QLineEdit(self)
        self.vars["lineEdit"].setReadOnly(True)
        self.vars["listView"] = self.MyListView(self, self.vars)
        self.vars["listViewModel"] = QStandardItemModel(self)
        self.setModel(self.vars["listViewModel"])
        self.setView(self.vars["listView"])
        self.setLineEdit(self.vars["lineEdit"])

        self.activated.connect(self.__show_selected)

        self.add_item("(全选)")

    def count(self):
        # 返回子项数
        return super().count() - 1

    @show_text
    def add_item(self, text: "str"):
        # 根据文本添加子项
        item = QStandardItem()
        item.setText(text)
        item.setCheckable(True)
        item.setCheckState(Qt.Checked)
        self.vars["listViewModel"].appendRow(item)

    @show_text
    def add_items(self, texts: "tuple or list"):
        # 根据文本列表添加子项
        for text in texts:
            self.add_item(text)

    @show_text
    def clear_items(self):
        # 清空所有子项
        self.vars["listViewModel"].clear()
        self.add_item("(全选)")

    def find_index(self, index: "int"):
        # 根据索引查找子项
        return self.vars["listViewModel"].item(index if index < 0 else index + 1)

    def find_indexs(self, indexs: "tuple or list"):
        # 根据索引列表查找子项
        return [self.find_index(index) for index in indexs]

    def find_text(self, text: "str"):
        # 根据文本查找子项
        tempList = self.vars["listViewModel"].findItems(text)
        tempList.pop(0) if tempList and tempList[0].row() == 0 else tempList
        return tempList

    def find_texts(self, texts: "tuple or list"):
        # 根据文本列表查找子项
        return {text: self.find_text(text) for text in texts}

    def get_text(self, index: "int"):
        # 根据索引返回文本
        return self.vars["listViewModel"].item(index if index < 0 else index + 1).text()

    def get_texts(self, indexs: "tuple or list"):
        # 根据索引列表返回文本
        return [self.get_text(index) for index in indexs]

    def change_text(self, index: "int", text: "str"):
        # 根据索引改变某一子项的文本
        self.vars["listViewModel"].item(index if index < 0 else index + 1).setText(text)

    @show_text
    def select_index(self, index: "int", state: "bool" = True):
        # 根据索引选中子项，state=False时为取消选中
        self.vars["listViewModel"].item(index if index < 0 else index + 1).setCheckState(
            Qt.Checked if state else Qt.Unchecked)

    @show_text
    def select_indexs(self, indexs: "tuple or list", state: "bool" = True):
        # 根据索引列表选中子项，state=False时为取消选中
        for index in indexs:
            self.select_index(index, state)

    @show_text
    def select_text(self, text: "str", state: "bool" = True):
        # 根据文本选中子项，state=False时为取消选中
        for item in self.find_text(text):
            item.setCheckState(Qt.Checked if state else Qt.Unchecked)

    @show_text
    def select_texts(self, texts: "tuple or list", state: "bool" = True):
        # 根据文本列表选中子项，state=False时为取消选中
        for text in texts:
            self.select_text(text, state)

    @show_text
    def select_reverse(self):
        # 反转选择
        if self.vars["listViewModel"].item(0).checkState() == Qt.Unchecked:
            self.select_all()
        elif self.vars["listViewModel"].item(0).checkState() == Qt.Checked:
            self.select_clear()
        else:
            for row in range(1, self.vars["listViewModel"].rowCount()):
                self.__select_reverse(row)

    def __select_reverse(self, row: "int"):
        item = self.vars["listViewModel"].item(row)
        item.setCheckState(Qt.Unchecked if item.checkState() == Qt.Checked else Qt.Checked)

    @show_text
    def select_all(self):
        # 全选
        for row in range(0, self.vars["listViewModel"].rowCount()):
            self.vars["listViewModel"].item(row).setCheckState(Qt.Checked)

    @show_text
    def select_clear(self):
        # 全不选
        for row in range(0, self.vars["listViewModel"].rowCount()):
            self.vars["listViewModel"].item(row).setCheckState(Qt.Unchecked)

    @show_text
    def remove_index(self, index: "int"):
        # 根据索引移除子项
        return self.vars["listViewModel"].takeRow(index if index < 0 else index + 1)

    @show_text
    def remove_indexs(self, indexs: "tuple or list"):
        # 根据索引列表移除子项
        return [self.remove_index(index) for index in sorted(indexs, reverse=True)]

    @show_text
    def remove_text(self, text: "str"):
        # 根据文本移除子项
        items = self.find_text(text)
        indexs = [item.row() for item in items]
        return [self.vars["listViewModel"].takeRow(index) for index in sorted(indexs, reverse=True)]

    @show_text
    def remove_texts(self, texts: "tuple or list"):
        # 根据文本列表移除子项
        return {text: self.remove_text(text) for text in texts}

    def get_selected(self):
        # 获取当前选择的子项
        items = list()
        for row in range(1, self.vars["listViewModel"].rowCount()):
            item = self.vars["listViewModel"].item(row)
            if item.checkState() == Qt.Checked:
                items.append(item)
        return items

    def get_selected_text_list(self):
        items = self.get_selected()
        y_list = list()

        for i in items:
            y_list.append(i.text())

        return y_list

    def is_all(self):
        # 判断是否是全选
        return True if self.vars["listViewModel"].item(0).checkState() == Qt.Checked else False

    def sort(self, order=Qt.AscendingOrder):
        # 排序，默认正序
        self.vars["listViewModel"].sort(0, order)

    @show_text
    def __show_selected(self, index):
        if not self.vars["lock"]:
            if index == 0:
                if self.vars["listViewModel"].item(0).checkState() == Qt.Checked:
                    self.select_clear()
                else:
                    self.select_all()
            else:
                self.__select_reverse(index)

            self.vars["lock"] = True

    def hidePopup(self):
        if self.vars["lock"]:
            super().hidePopup()


class LoadingMask(QMainWindow):
    def __init__(self, parent, gif=None, tip=None, min=0):
        """
        gif优先级高于 tip，两者同时赋值优先使用 gif
        :param parent:
        :param gif:
        :param tip:
        :param min:
        """
        super(LoadingMask, self).__init__(parent)

        self.min = min
        self.show_time = 0

        parent.installEventFilter(self)

        self.label = QLabel()

        if not tip is None:
            self.label.setText(tip)
            font = QFont('Microsoft YaHei', 10, QFont.Normal)
            font_metrics = QFontMetrics(font)
            self.label.setFont(font)
            self.label.setFixedSize(font_metrics.width(tip, len(tip)) + 10, font_metrics.height() + 5)
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet(
                'QLabel{background-color: rgba(0,0,0,70%);border-radius: 4px; color: white; padding: 5px;}')

        if not gif is None:
            self.movie = QMovie(gif)
            self.label.setMovie(self.movie)
            self.label.setAttribute(Qt.WA_TranslucentBackground)
            self.label.setFixedSize(QSize(160, 160))
            self.label.setScaledContents(True)
            self.movie.start()

        layout = QHBoxLayout()
        widget = QWidget()
        widget.setObjectName('background')
        # widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setStyleSheet('QWidget#background{background-color: rgba(255, 255, 255, 40%);}')
        widget.setLayout(layout)
        layout.addWidget(self.label)

        self.setCentralWidget(widget)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.hide()

    def eventFilter(self, widget, event):
        events = {QMoveEvent, QResizeEvent, QPaintEvent}
        if widget == self.parent():
            if type(event) == QCloseEvent:
                self.close()
                return True
            elif type(event) in events:
                self.moveWithParent()
                return True
        return super(LoadingMask, self).eventFilter(widget, event)

    def moveWithParent(self):
        if self.parent().isVisible():
            self.move(self.parent().geometry().x(), self.parent().geometry().y())
            self.setFixedSize(QSize(self.parent().geometry().width(), self.parent().geometry().height()))

    def show(self):
        super(LoadingMask, self).show()
        self.show_time = time.time()
        self.moveWithParent()

    def close(self):
        # 显示时间不够最小显示时间 设置Timer延时删除
        if (time.time() - self.show_time) * 1000 < self.min:
            QTimer().singleShot((time.time() - self.show_time) * 1000 + 10, self.close)
        else:
            super(LoadingMask, self).hide()
            super(LoadingMask, self).deleteLater()

    @staticmethod
    def showToast(window, tip='加载中...', duration=500, appended_task=None):
        mask = LoadingMask(window, tip=tip)
        mask.show()

        def task():
            mask.deleteLater()
            if callable(appended_task):
                appended_task()

        # 一段时间后移除组件
        QTimer().singleShot(duration, task)

