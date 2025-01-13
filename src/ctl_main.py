import time

import keyboard
from PySide6.QtCore import QThread, QWaitCondition, QMutex
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget

from ui_main import Ui_Form


class Worker(QThread):

    def __init__(self, presstime, releasetime):
        super().__init__()
        self.presstime = float(presstime)
        self.releasetime = float(releasetime)
        self._isPause = False
        self.cond = QWaitCondition()
        self.mutex = QMutex()

    def pause(self):
        self._isPause = True

    def resume(self):
        self._isPause = False
        self.cond.wakeOne()

    def run(self):
        while 1:
            self.mutex.lock()
            if self._isPause:
                self.cond.wait(self.mutex)

            # 按下键盘
            keyboard.press('space')
            time.sleep(self.presstime)
            print(self.presstime)
            # 松开键盘
            keyboard.release('space')
            time.sleep(self.releasetime)
            print(self.releasetime)

            self.mutex.unlock()


class MainApp(QWidget, Ui_Form):

    def init_slot(self):
        self.pushButton_start.clicked.connect(self.slot_start)
        self.pushButton_stop.clicked.connect(self.slot_pause)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setWindowTitle('v0.0.1')
        self.init_slot()
        self.thread = Worker(self.lineEdit_presstime.text(), self.lineEdit_releasetime.text())
        print('pause')
        self.thread.pause()
        print('start')
        self.thread.start()

    def slot_start(self):
        print('resume')
        self.lineEdit_presstime.setDisabled(True)
        self.lineEdit_releasetime.setDisabled(True)
        self.thread.resume()

    def slot_pause(self):
        print('pause')
        self.thread.pause()
        self.lineEdit_presstime.setDisabled(False)
        self.lineEdit_releasetime.setDisabled(False)

    def closeEvent(self, a0):
        self.thread.pause()
        self.thread.deleteLater()
        super().closeEvent(a0)
        exit(0)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.m_drag:
            self.move(event.globalPos() - self.m_DragPosition)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_drag = False
