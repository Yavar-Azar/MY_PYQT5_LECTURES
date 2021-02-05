#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:09:18 2021

@author: yavar0001
"""

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


class Widget(QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent=parent)
        self.verticalLayout = QVBoxLayout(self)
        # self.verticalLayout.setObjectName("verticalLayout")
        for i in range(10):
            pushButton = QPushButton(self)
            pushButton.setObjectName("pushButton{}".format(i))
            pushButton.setText(str(i))
            self.verticalLayout.addWidget(pushButton)

        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.updateText)
        timer.start()

    def updateText(self):
        for i in range(10):
            child = self.findChild(QPushButton, "pushButton{}".format(i))
            counter = int(child.text())
            child.setText(str(counter+1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())