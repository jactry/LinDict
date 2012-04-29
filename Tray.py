#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

class LinTray(QtGui.QSystemTrayIcon):
    def __init__(self,parent = None):
        QtGui.QSystemTrayIcon.__init__(self,parent)
        self.icon = QtGui.QIcon("./youdao.png")
        self.setIcon(self.icon)

        self.quit_Action = QtGui.QAction(u"&退出",self,triggered = QtGui.qApp.quit)
        self.Tray_Menu = QtGui.QMenu()
        self.Tray_Menu.addAction(self.quit_Action)
        self.setContextMenu(self.Tray_Menu)
