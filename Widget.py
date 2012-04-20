#! /usr/bin/python

import sys
from PyQt4 import QtGui , QtCore
import Lookup
import commands

from PyQt4.QtCore import Qt, SIGNAL
from PyQt4.QtGui import *
from PyQt4 import QtGui, QtCore

class Lin_Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
    
        self.setGeometry(400,400,300,200)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setBackgroundRole(19)

        gl =QtGui.QGridLayout()
        gl.setSpacing(10)        
        self.textedit = QtGui.QTextEdit()
        self.textedit.setGeometry(QtCore.QRect(150,200,300,200))
        self.textedit.setReadOnly(True)
        self.textedit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textedit.setAlignment(Qt.AlignTop)
        gl.addWidget(self.textedit, 3, 0, 5, 2)
        self.setLayout(gl)
        self.setAttribute(Qt.WA_X11DoNotAcceptFocus, True)
         
    def Translate(self):
	myClipBoard = QtGui.QApplication.clipboard()
	word = myClipBoard.text("plain",QtGui.QClipboard.Selection)      
        word = word.toLower()
        result =Lookup.look_up(word)
        reload(sys)
        sys.setdefaultencoding('utf-8')
        res=unicode(result)
        self.textedit.setText(result)

    def leaveEvent(self,event):
        self.close()

            
