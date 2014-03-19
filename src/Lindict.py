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

import sys
from PyQt4 import QtGui, QtCore
from MainWindow import MainWindow
from Widget import LinWidget


class Lindict():
    def __init__(self):
        self.clipboard = QtGui.QApplication.clipboard()
        self.mainwindow = MainWindow()
        self.mainwindow.show()
        self.widget = LinWidget()
        self.clipboard.selectionChanged.connect(self.display_widget)
        QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))

    def display_widget(self):
        if self.mainwindow.real_time_status:
            test = self.clipboard.text("plain", QtGui.QClipboard.Selection)
            test = str(test).strip()
            if test != str(self.mainwindow.lineEdit.text()):
                self.widget.Translate()
                self.cursor = QtGui.QCursor.pos()
                self.widget.setGeometry(self.cursor.x(), self.cursor.y(), 300, 200)
                self.widget.show()

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        Lindict = Lindict()
        reload(sys)
        sys.setdefaultencoding('utf-8')
        sys.exit(app.exec_())
