#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui , QtCore
from MainWindow import MainWindow
from Widget import LinWidget

class Lindict():
   def __init__(self):
      self.clipboard = QtGui.QApplication.clipboard()
      self.mainwindow = MainWindow()
      self.mainwindow.show()
      self.widget = LinWidget()
      self.clipboard.selectionChanged.connect(self.display_widget)

      

   def display_widget(self):
      if self.mainwindow.real_time_status:
         test = self.clipboard.text("plain", QtGui.QClipboard.Selection)
         test = str(test).strip()
         if test != self.mainwindow.lineEdit.text():
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
