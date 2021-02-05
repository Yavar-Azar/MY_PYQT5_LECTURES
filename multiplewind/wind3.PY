#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:00:21 2021

@author: yavar001
"""

import sys
import glob
from random import randint

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QSpacerItem,
    QSizePolicy,   
    QLineEdit,
    QFileDialog,
)




elements=['Cs', 'Pb', 'Cl', 'I']


class pseudo(QWidget):
    """
    This "window" is a QWidget. If it has no parent,
    it will appear as a free-floating window.
    """

    def __init__(self):
        super().__init__()
#        self.setGeometry(800,200, 200, 400)
        self.setStyleSheet("""
        QLabel {
            border: 1px solid gray;
            border-radius: 1px;
            background-color: rgb(155, 200, 255);
            color: rgb(55, 0, 255);            
            }
        """)
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        
        
        
        Hbox = QHBoxLayout()
        
        
        self.elementlist = QLabel("Elements")

        layout1.addWidget(self.elementlist)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout1.addItem(verticalSpacer)
        
        self.pseudolb = QLabel("pseudofiles")
        
        layout2.addWidget(self.pseudolb)
        layout2.addItem(verticalSpacer)
        
        self.selectlb = QLabel("Select pseudo file")
        layout3.addWidget(self.selectlb)
        
        
        for element in elements:
            self.bott = QPushButton(element)
            self.bott.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}")
            layout1.addWidget(self.bott)
            self.elemntld =QLineEdit("")
            layout2.addWidget(self.elemntld)
        
        
        Hbox.addLayout(layout1)
        Hbox.addLayout(layout2)
        self.setLayout(Hbox)


    def selectdirectory(self):
        
        my_dir = QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            "./",
            QFileDialog.ShowDirsOnly
            )
        print("selected PATH is "+my_dir)
        
        
        for element in elements:
            serach=my_dir+"/"+element+"*.UPF"
            
        
        
                
        return my_dir
    
    
    
        
       



app = QApplication(sys.argv)
w = pseudo()
w.show()
app.exec_()