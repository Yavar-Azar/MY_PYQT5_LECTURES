#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:00:21 2021

@author: yavar001
"""

import sys
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class firstwind(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
        self.setGeometry(800,200, 200, 400)
        self.setStyleSheet("""
        QWidget {
            border: 2px solid black;
            border-radius: 1px;
            background-color: rgb(55, 100, 255);
            color: rgb(255, 155, 10);            
            }
        """)
        layout = QVBoxLayout()
        
        self.label = QLabel("  Label1")
        self.label.setGeometry(10,10,100,100)
        self.bott = QPushButton("click")  
        
        self.bott.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}")
        layout.addWidget(self.label)
        layout.addWidget(self.bott)
        layout.addStretch()
        self.setLayout(layout)
