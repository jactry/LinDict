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
import Lookup

from PyQt4.QtCore import Qt
from PyQt4.QtGui import *


class LinWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setGeometry(400, 400, 300, 200)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setBackgroundRole(19)

        gl = QtGui.QGridLayout()
        gl.setSpacing(10)
        self.textedit = QtGui.QTextEdit()
        self.textedit.setGeometry(QtCore.QRect(150, 200, 300, 200))
        self.textedit.setReadOnly(True)
        self.textedit.setTextInteractionFlags(Qt.NoTextInteraction)
        self.textedit.setAlignment(Qt.AlignTop)
        gl.addWidget(self.textedit, 3, 0, 5, 2)
        self.setLayout(gl)
        self.setAttribute(Qt.WA_X11DoNotAcceptFocus, True)
        pl = self.textedit.palette()
        pl.setBrush(QPalette.Base, QBrush(QColor(255, 0, 0, 0)));
        self.textedit.setPalette(pl);
        self.textedit.setFrameShape(QFrame.NoFrame)

    def Translate(self):
        myClipBoard = QtGui.QApplication.clipboard()
        word = myClipBoard.text("plain", QtGui.QClipboard.Selection)
        result = Lookup.look_up(word)
        if not result:
            htmlfile = open("./template/404.html", 'r')
            self.textedit.setText(self.tr(htmlfile.read()))
            htmlfile.close()
        else:
            reload(sys)
            sys.setdefaultencoding('utf-8')
            unicode(result)
            self.textedit.setText(result)

    def leaveEvent(self, event):
        self.close()
