#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:00:21 2021

@author: yavar001
"""
import os
import sys
import glob, shutil, re
from random import randint
import requests
from bs4 import BeautifulSoup, SoupStrainer

from PyQt5.QtCore import (QCoreApplication, 
                          QObject,
                          QRunnable,
                          QThread,
                          QThreadPool,
                          pyqtSignal)

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
    QProgressBar,
    QMessageBox,
)





##############  READ RUN_DIRECTORY and element list from main

rundir="./"
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
        
        self.listofselected=[]

        self.elementlist = QLabel("Elements")
        
        

        
        

        layout1.addWidget(self.elementlist)

        
        self.pseudolb = QLabel("       load offline files       ")
        
        self.connectionlabel = QLabel()
        
        
        
        
        
        
        ################   Internet connection  ###############
        
        url = "https://www.quantum-espresso.org/pseudopotentials"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            self.connectionlabel.setText("\nNetwork\nConnected")
            self.connectionlabel.setStyleSheet("background-color : lightgreen;")
        except (requests.ConnectionError, requests.Timeout) as exception:
            self.connectionlabel.setText("Network\nDisconnected")
            self.connectionlabel.setStyleSheet("background-color : red; color:yellow")            

        
        ########################################################
                
        layout1.addWidget(self.connectionlabel)
        verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout1.addItem(verticalSpacer)
        
        
        
        self.updatebut=QPushButton("UPDATE")
        
        
        layout2.addWidget(self.pseudolb)
        
        self.findlocalbt = QPushButton("pseudo local directory    ")
        layout2.addWidget(self.findlocalbt)

        layout2.addWidget(self.updatebut)
        
        layout2.addItem(verticalSpacer)
        
        self.selectlb = QLabel("Load online             ")
        self.explorer = QPushButton("Search online libraries     ")
        
        self.downloadmsg_lb = QLabel("None")
        
        
        self.downloader = QPushButton("Download selected files     ")
        self.progress = QProgressBar() 
        self.progress.setFixedHeight(20)
        self.progress.setFixedWidth(200)

        
        layout2.addWidget(self.downloadmsg_lb)
        layout3.addWidget(self.selectlb)
        layout3.addWidget(self.explorer)
        layout3.addWidget(self.downloader)
        layout3.addWidget(self.progress)

        layout3.addStretch()
        
        
        
        #########  FUNCTIONS

        self.findlocalbt.clicked.connect(self.selectdirectory)
        self.updatebut.clicked.connect(self.updateselected)
        self.explorer.clicked.connect(self.pseudo_finder)
        self.downloader.clicked.connect(self.on_pushButton_clicked)
        
        
        
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
        '''
        

        Returns
        -------
        This function updates selected pseudo files and remove other pseudo file in
        run directory and copies only selected ones

        '''
        
        list1=[]
        for element in elements:
            ellineedit = self.findChild(QLineEdit, element+"lineedit")
            cmbo1=self.findChild(QComboBox, element+"combo")
            list1.append(cmbo1.currentText())
            ellineedit.setText(cmbo1.currentText().split("/")[-1])
        
            
        self.listofselected=list1
        dirname=rundir
        files = glob.glob(dirname+'/*UPF')
        files.extend(glob.glob(dirname+'/*upf'))
        
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
        
        for pseudofile in list1:
            shutil.copy(pseudofile, dirname)
            
        
            
        
        
        
        
#        print(self.pseudodict)
##############  online pseudo


    def pseudo_finder(self):
        
        
        url = "https://www.quantum-espresso.org/pseudopotentials/ps-library/"
        
        for element in elements:
            page = requests.get(url+element.lower())
            data = page.text
            soup = BeautifulSoup(data)
            pseudolist=[]
            for link in soup.find_all('a'):
                pseudolist.append(link.get('href'))
                
            listtemp=[x for x in pseudolist if x is not None]
            listtemp1=[x for x in listtemp if 'UPF' in x]
            
            #  Extract only file names
            
            pseudoname = [re.sub('/upf_files/', '', fname) for fname in listtemp1]
            
            
            cmbo1=self.findChild(QComboBox, element+"combo")
            cmbo1.addItems(pseudoname)
            
            



#####   we need  a downloader             
            
    # Download button event
    def on_pushButton_clicked(self):
        values=[]
        elnum=len(elements)
        sect=100.0/elnum
        for i in range(elnum):
            values.append(int(sect)*(i))
        values.append(100)
        
        j=1
        for element in elements:
            selectedcmbo = self.findChild(QComboBox, element+"combo")
            selectedpseudo = selectedcmbo.currentText()
            ellineedit = self.findChild(QLineEdit, element+"lineedit")
            ellineedit.setText(selectedpseudo)
            the_url = 'https://www.quantum-espresso.org/upf_files/'+selectedpseudo
            r = requests.get(the_url, allow_redirects=True)
            the_filepath ="./"+selectedpseudo
            open(the_filepath, 'wb').write(r.content)
            #### Create a download thread
            self.progress.setValue(values[j])
            j=j+1







       



app = QApplication(sys.argv)
w = pseudo()
w.show()
app.exec_()