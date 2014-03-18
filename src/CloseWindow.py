#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################################
#  Copyright (C) 2012 by Jactry Zeng                                     #
#                                                                        #
#  This program is free software: you can redistribute it and/or modify  #
#  it under the terms of the GNU General Public License as published by  #
#  the Free Software Foundation, either version 3 of the License, or     #
#  (at your option) any later version.                                   #
#                                                                        #
#  This program is distributed in the hope that it will be useful,       #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#  GNU General Public License for more details.                          #
#                                                                        #
#  You should have received a copy of the GNU General Public License     #
#  along with this program.  If not, see <http://www.gnu.org/licenses/>. #
##########################################################################

from PyQt4 import QtGui
from ui_close import Ui_Dialog
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt, SIGNAL


class CloseDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.connect(self.tray_RBtn, SIGNAL("clicked()"), self.check_RBtn)
        self.connect(self.exit_RBtn, SIGNAL("clicked()"), self.check_RBtn)
        self.connect(self.ok_Btn, SIGNAL("clicked()"), self.press_ok)
        self.connect(self.cancel_Btn, SIGNAL("clicked()"), self.press_cancel)

    def check_RBtn(self):
        if self.tray_RBtn.isChecked():
            self.exit_RBtn.setChecked(False)
        elif self.exit_RBtn.isChecked():
            self.tray_RBtn.setChecked(False)

    def press_ok(self):
        if self.tray_RBtn.isChecked():
            if self.checkBox.isChecked():
              # self.setResult(0) # 0 meaning hide and don't ask for next time
                self.done(0)
            elif not self.checkBox.isChecked():
               #elf.setResult(1) # 1 meaning hide but ask for next time
                self.done(1)
        elif not self.tray_RBtn.isChecked():
            if self.checkBox.isChecked():
                #elf.setResult(2) # 2 meaning don't hide and ask for next time
                self.done(2)
            elif not self.checkBox.isChecked():
                #self.setResult(3) # 3 meaning don't hide but ask for next time
                self.done(3)

    def press_cancel(self):
        self.done(4)
