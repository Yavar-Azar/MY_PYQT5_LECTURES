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
    QComboBox,
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
        
        self.pseudodict={}

        self.elementlist = QLabel("Elements")
        

        layout1.addWidget(self.elementlist)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout1.addItem(verticalSpacer)
        
        self.pseudolb = QLabel("        pseudo file name       ")
        
        self.updatebut=QPushButton("UPDATE")
        
        
        layout2.addWidget(self.pseudolb)
        layout2.addWidget(self.updatebut)
        layout2.addItem(verticalSpacer)
        
        self.selectlb = QLabel("Select pseudo file")
        layout3.addWidget(self.selectlb)
        self.findlocalbt = QPushButton("pseudo local directory    ")
        layout3.addWidget(self.findlocalbt)
        layout3.addStretch()
        
        #########  FUNCTIONS

        self.findlocalbt.clicked.connect(self.selectdirectory)
        self.updatebut.clicked.connect(self.updateselected)
        
        for element in elements:
            bott = QPushButton(self)
            bott.setObjectName(element+"pushbut")
            bott.setText(element)
            bott.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}")
            layout1.addWidget(bott)
            elemntld =QLineEdit(self)
            elemntld.setObjectName(element+"lineedit")
            layout2.addWidget(elemntld)
            cmbo = QComboBox(self)
           # cmbo.addItems(listofseudo)
            cmbo.setObjectName(element+"combo")
            layout3.addWidget(cmbo)
            
            
        
        
        Hbox.addLayout(layout1)
        Hbox.addLayout(layout2)
        Hbox.addLayout(layout3)
        self.setLayout(Hbox)


    def selectdirectory(self):
        '''
        

        Returns
        -------
        my_dir : string
            local repository for pseudo files.
        pseudodict : dictionary
            dictionary with pseudo address .
        '''
        
        my_dir = QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            "./",
            QFileDialog.ShowDirsOnly
            )
        print("selected PATH is "+my_dir)
        
        
        for element in elements:
            search1=my_dir+"/"+element+"*.upf"
            search2=my_dir+"/"+element+"*.UPF"
            listofseudo=glob.glob(search1)
            listofseudo.extend(glob.glob(search2))
            self.pseudodict.update({element: listofseudo})
            cmbo1=self.findChild(QComboBox, element+"combo")
            cmbo1.addItems(listofseudo)


    def updateselected(self):
        
        
        for element in elements:
            ellineedit = self.findChild(QLineEdit, element+"lineedit")
            cmbo1=self.findChild(QComboBox, element+"combo")
            ellineedit.setText(cmbo1.currentText().split("/")[-1])
        
            
        
        
        
        
#        print(self.pseudodict)




    
        
    
    
    
        
       



app = QApplication(sys.argv)
w = pseudo()
w.show()
app.exec_()