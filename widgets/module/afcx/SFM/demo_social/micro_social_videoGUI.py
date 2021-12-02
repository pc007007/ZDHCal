import gc
import sys
import os
from functools import wraps

import psutil
from PySide6.QtCore import QTimer, Signal
from PySide6.QtGui import QPixmap, Qt, QImage
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QSlider, \
    QStyleOptionSlider, QStyle, QMainWindow, QProgressBar

DEBUG: bool = True


def memory(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        previous_size = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        retval = f(*args, **kwargs)
        current_size = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
        print('   占用内存空间: %.1f' % (current_size - previous_size), 'MB')
        return retval
    return decorated


class MicroSocialGUI(QMainWindow):
    def __init__(self, parent=None):
        super(MicroSocialGUI, self).__init__(parent)

        # <<---定义变量--->>
        self.folder_name: str
        self.image_path: list[str]
        self.image_items: list[QPixmap]
        self.fps: int
        self.current_frame: int
        self.buffer_size: int

        # <<---初始化参数--->>
        self.folder_name = 'results/'
        self.fps = 20
        self.current_frame = 0
        self.buffer_size = 20

        # <<---参数赋值--->>
        self.image_path = [self.folder_name + img for img in os.listdir(self.folder_name) if img.endswith(".png")]
        self.image_items, self.images_count = self.image_buffer(self.image_path, self.current_frame,
                                                                buffer_size=self.buffer_size)

        # <<---初始化UI--->>
        self.iniUI()


    def iniUI(self):
        self.slider_pressed_flag: bool = False

        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.img_label = QLabel('展示图像部件')
        self.draw_label()
        layout.addWidget(self.img_label)

        self.start_stop_resume_btn = QPushButton('开始')
        layout.addWidget(self.start_stop_resume_btn)
        self.start_stop_resume_btn.clicked.connect(self.start_stop_resume_btn_click)

        self.slider = Slider(Qt.Horizontal)
        layout.addWidget(self.slider)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.images_count - 1)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)
        self.slider.valueSteepChanged.connect(self.slider_steep_value_changed)

        self.half_speed_btn = QPushButton('半速')
        layout.addWidget(self.half_speed_btn)
        self.half_speed_btn.clicked.connect(self.half_speed_btn_click)

        self.normal_speed_btn = QPushButton('正常')
        layout.addWidget(self.normal_speed_btn)
        self.normal_speed_btn.clicked.connect(self.normal_speed_btn_click)

        self.double_speed_btn = QPushButton('2倍速')
        layout.addWidget(self.double_speed_btn)
        self.double_speed_btn.clicked.connect(self.double_speed_btn_click)

        self.clrup_mem_btn = QPushButton('清理内存')
        layout.addWidget(self.clrup_mem_btn)
        self.clrup_mem_btn.clicked.connect(self.clrup_mem_btn_click)

        self.disable_adjust_speed_btn(True)

        current_mem = self.current_memory()
        self.progress = QProgressBar()
        self.progress.setMinimum(0)
        self.progress.setMaximum(1000)
        self.statusBar().addPermanentWidget(self.progress)
        self.progress.setValue(current_mem)
        self.mem_usage_label = QLabel(f'内存使用：{current_mem} MB/1000MB')
        self.statusBar().addPermanentWidget(self.mem_usage_label)

        self.timer: QTimer = QTimer()
        self.timer.timeout.connect(self.update_label)
        self.mem_timer: QTimer = QTimer()
        self.mem_timer.start(1000)
        self.mem_timer.timeout.connect(self.update_mem_status)

    def current_memory(self):
        return int(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024)

    @memory
    def image_buffer_all(self, images_path: list, current_frame: int) -> (list, int):
        """
        将images_path内所有文件读入内存
        """
        total_memory: float = 0.0
        images: list = []
        for image in images_path[current_frame:]:
            with open(image, 'rb') as f:
                img = f.read()
                image_data = QImage.fromData(img)
                pixmap = QPixmap.fromImage(image_data)
                images.append(pixmap)
                total_memory = total_memory + (image_data.sizeInBytes() / 1024 / 1024)

        images_count = len(images)
        if DEBUG:
            print('---图片存入内存---')
            print('   图片总数：', images_count)

        return images, images_count

    @memory
    def image_buffer(self, images_path: list, current_frame: int, buffer_size: int=10) -> (list, int):
        """
        将images_path部分文件读入内存
        """
        total_memory: float = 0.0
        images: list = []
        for image in images_path[current_frame:current_frame+buffer_size]:
            with open(image, 'rb') as f:
                img = f.read()
                image_data = QImage.fromData(img)
                pixmap = QPixmap.fromImage(image_data)
                images.append(pixmap)
                total_memory = total_memory + (image_data.sizeInBytes() / 1024 / 1024)

        images_count = len(images)
        if DEBUG:
            print('---图片存入内存---')
            print('   图片总数：', images_count)

        return images, images_count

    def play(self, fps: int, current_frame: int = 0) -> None:
        """
        播放图片
        fps: 帧数
        current_frame: 起始帧，默认从0开始
        """
        self.current_frame = current_frame

        self.draw_label()

        interval = int(1000 / fps)
        self.timer.start(interval)
        if DEBUG:
            print('---播放参数---')
            print('   间隔：', interval, 'ms')
            print('   当前FPS:', 1000/interval)
            print('   当前帧序号：', self.current_frame)

    def draw_label(self):
        self.img_label.setPixmap(self.image_items[self.current_frame])

    def update_label(self):
        # if self.current_frame < self.images_count:
        try:
            # <<---增加图片到images--->>
            self.image_items: list
            with open(self.image_path[self.current_frame + self.buffer_size], 'rb') as f:
                img = f.read()
                image_data = QImage.fromData(img)
                pixmap = QPixmap.fromImage(image_data)
                self.image_items.append(pixmap)
            self.draw_label()
            if not self.slider_pressed_flag: self.slider.setValue(self.current_frame)
            self.current_frame += 1
        except:
            self.timer.stop()
            self.slider.setValue(0)
            self.start_stop_resume_btn.setText('开始')

    def start_stop_resume_btn_click(self):
        if self.start_stop_resume_btn.text() == '开始':
            self.play(self.fps, current_frame=0)
            self.start_stop_resume_btn.setText('暂停')
            self.disable_adjust_speed_btn(False)
            return

        if self.timer.isActive():
            self.timer.stop()
            self.start_stop_resume_btn.setText('继续')
            self.disable_adjust_speed_btn(True)
        else:
            self.timer.start()
            self.start_stop_resume_btn.setText('暂停')
            self.disable_adjust_speed_btn(False)

    def disable_adjust_speed_btn(self, disable: bool) -> None:
        self.half_speed_btn.setDisabled(disable)
        self.normal_speed_btn.setDisabled(disable)
        self.double_speed_btn.setDisabled(disable)

    def slider_value_changed(self, value):
        self.current_frame = value
        self.draw_label()

    def slider_steep_value_changed(self, value):
        # 判断是否位于开始状态
        if self.start_stop_resume_btn.text() == '开始':
            self.play(self.fps, current_frame=value)
            self.timer.stop()
            self.start_stop_resume_btn.setText('继续')

    def slider_pressed(self):
        self.slider_pressed_flag = True

    def slider_released(self):
        self.slider_pressed_flag = False

    def half_speed_btn_click(self):
        fps = int(self.fps / 2)
        self.play(fps=fps, current_frame=self.current_frame)

    def double_speed_btn_click(self):
        fps = int(self.fps * 2)
        self.play(fps=fps, current_frame=self.current_frame)

    def normal_speed_btn_click(self):
        fps = self.fps
        self.play(fps=fps, current_frame=self.current_frame)

    def clrup_mem_btn_click(self):
        i = int(len(self.image_items) / 2)
        while i != 0 :
            self.image_items.pop()
            i -= 1
        print(len(self.image_items))
        gc.collect()

    def update_mem_status(self):
        current_used_mem = int(psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024)
        self.progress.setValue(int(current_used_mem))
        self.mem_usage_label.setText(f'内存使用：{current_used_mem} MB/1000MB')


class Slider(QSlider):
    valueSteepChanged = Signal(int)

    def mousePressEvent(self, event):
        super(Slider, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            val = self.pixelPosToRangeValue(event.position())
            self.setValue(val)
            self.valueSteepChanged.emit(val)

    def pixelPosToRangeValue(self, pos):
        opt = QStyleOptionSlider()
        self.initStyleOption(opt)
        gr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
        sr = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

        if self.orientation() == Qt.Horizontal:
            sliderLength = sr.width()
            sliderMin = gr.x()
            sliderMax = gr.right() - sliderLength + 1
        else:
            sliderLength = sr.height()
            sliderMin = gr.y()
            sliderMax = gr.bottom() - sliderLength + 1;
        pr = pos - sr.center() + sr.topLeft()
        p = pr.x() if self.orientation() == Qt.Horizontal else pr.y()
        return QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - sliderMin,
                                              sliderMax - sliderMin, opt.upsideDown)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window: MicroSocialGUI = MicroSocialGUI()
    window.show()

    sys.exit(app.exec())
