#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui , QtCore
from MainWindow import MainWindow
from Widget import Lin_Widget



if __name__ == "__main__":

   def display_widget():
      if Lindict.real_time_status:
         test = Lin_clipboard.text("plain",QtGui.QClipboard.Selection)
         if test != "" and test != Lindict.lineEdit.text():
            widget.Translate()
            cursor = QtGui.QCursor.pos()
            widget.setGeometry(cursor.x(), cursor.y(), 300, 200)
           # widget.setFocusPolicy(QtCore.Qt.NoFocus)
            #widget.show()
           # widget.setAttribute(QtCore.Qt.WA_ShowWithoutActivating, False)
            widget.show()
         #   widget.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)

   app = QtGui.QApplication(sys.argv)
   Lin_clipboard = QtGui.QApplication.clipboard()
   Lin_clipboard.selectionChanged.connect(display_widget)
   Lindict = MainWindow()
   widget = Lin_Widget()
   reload(sys)
   sys.setdefaultencoding('utf-8')
   Lindict.show()
   sys.exit(app.exec_())
