#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 07:59:41 2021

@author: yavar001
"""

import sys
from random import randint
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)



##########  import windows apps

from wind1 import *



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 600, 400) 
        self.window1 = firstwind()
        self.window2 = firstwind()



        lh=QHBoxLayout()
        lh.addStretch()


        l = QVBoxLayout()
        l.addStretch()

        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(
            lambda checked: self.toggle_window(self.window1)
        )
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.window2)
        )
        l.addWidget(button2)
        
        
        

        
        l2= QVBoxLayout()
        button3=QPushButton("test")
        l2.addWidget(button3)
        

        
        lh.addLayout(l)
        lh.addLayout(l2)


        
        w = QWidget()
        w.setLayout(lh)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()