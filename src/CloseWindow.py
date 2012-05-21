#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from ui_close import Ui_Dialog
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, SIGNAL


class CloseDialog(QDialog, Ui_Dialog):
    def __init__(self,parent):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.connect(self.tray_RBtn, SIGNAL("clicked()"), self.check_RBtn)
        self.connect(self.exit_RBtn, SIGNAL("clicked()"), self.check_RBtn)
        self.connect(self.ok_Btn, SIGNAL("clicked()"), self.press_ok)
        self.connect(self.cancel_Btn, SIGNAL("clicked()"), self.press_cancel)
        #return self.result()
        
        
    def check_RBtn(self):
        if self.tray_RBtn.isChecked() :
            self.exit_RBtn.setChecked(False)
        elif self.exit_RBtn.isChecked() :
            self.tray_RBtn.setChecked(False)
    
    def press_ok(self):
        if self.tray_RBtn.isChecked() :
           if self.checkBox.isChecked() :
              # self.setResult(0) # 0 meaning hide and don't ask for next time
              self.done(0)
           elif not self.checkBox.isChecked() :
               #elf.setResult(1) # 1 meaning hide but ask for next time
               self.done(1)
        elif not self.tray_RBtn.isChecked() :
            if self.checkBox.isChecked() :
                #elf.setResult(2) # 2 meaning don't hide and ask for next time
                self.done(2)
            elif not self.checkBox.isChecked() :
                #self.setResult(3) # 3 meaning don't hide but ask for next time
                self.done(3)
    def press_cancel(self):
        self.done(4)
        
