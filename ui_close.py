# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ui_close.ui'
#
# Created: Mon Apr  2 17:50:01 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, CloseDialog):
        CloseDialog.setObjectName(_fromUtf8("CloseDialog"))
        CloseDialog.setGeometry(QtCore.QRect(0, 0, 284, 122))
        CloseDialog.setMinimumSize(QtCore.QSize(284, 122))
        CloseDialog.setMaximumSize(QtCore.QSize(284, 122))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/youdao.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CloseDialog.setWindowIcon(icon)
        self.ok_Btn = QtGui.QPushButton(CloseDialog)
        self.ok_Btn.setGeometry(QtCore.QRect(140, 90, 70, 28))
        self.ok_Btn.setObjectName(_fromUtf8("ok_Btn"))
        self.cancel_Btn = QtGui.QPushButton(CloseDialog)
        self.cancel_Btn.setGeometry(QtCore.QRect(210, 90, 70, 28))
        self.cancel_Btn.setObjectName(_fromUtf8("cancel_Btn"))
        self.checkBox = QtGui.QCheckBox(CloseDialog)
        self.checkBox.setGeometry(QtCore.QRect(0, 90, 131, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.tray_RBtn = QtGui.QRadioButton(CloseDialog)
        self.tray_RBtn.setGeometry(QtCore.QRect(20, 50, 120, 20))
        self.tray_RBtn.setChecked(True)
        self.tray_RBtn.setObjectName(_fromUtf8("tray_RBtn"))
        self.exit_RBtn = QtGui.QRadioButton(CloseDialog)
        self.exit_RBtn.setGeometry(QtCore.QRect(160, 50, 120, 20))
        self.exit_RBtn.setObjectName(_fromUtf8("exit_RBtn"))
        self.label = QtGui.QLabel(CloseDialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(CloseDialog)
        QtCore.QMetaObject.connectSlotsByName(CloseDialog)

    def retranslateUi(self, CloseDialog):
        CloseDialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Lindict-关闭窗口", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_Btn.setText(QtGui.QApplication.translate("Dialog", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_Btn.setText(QtGui.QApplication.translate("Dialog", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Dialog", "下次不要再提示", None, QtGui.QApplication.UnicodeUTF8))
        self.tray_RBtn.setText(QtGui.QApplication.translate("Dialog", "最小化到托盘", None, QtGui.QApplication.UnicodeUTF8))
        self.exit_RBtn.setText(QtGui.QApplication.translate("Dialog", "直接退出程序", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "当关闭窗口时：", None, QtGui.QApplication.UnicodeUTF8))

import youdao_rc
