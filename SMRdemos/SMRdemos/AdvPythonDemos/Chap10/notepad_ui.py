# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notepad_ui.ui '
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_notepad(object):
    def setupUi(self, notepad):
        notepad.setObjectName(_fromUtf8("notepad"))
        notepad.resize(601, 600)
        self.centralwidget = QtGui.QWidget(notepad)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(530, 0, 75, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.button_open = QtGui.QPushButton(self.centralwidget)
        self.button_open.setGeometry(QtCore.QRect(0, 0, 261, 23))
        self.button_open.setObjectName(_fromUtf8("button_open"))
        self.editor_window = QtGui.QTextEdit(self.centralwidget)
        self.editor_window.setGeometry(QtCore.QRect(0, 20, 601, 571))
        self.editor_window.setObjectName(_fromUtf8("editor_window"))
        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(270, 0, 251, 23))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        notepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(notepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        notepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(notepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        notepad.setStatusBar(self.statusbar)

        self.retranslateUi(notepad)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), notepad.close)
        QtCore.QMetaObject.connectSlotsByName(notepad)

    def retranslateUi(self, notepad):
        notepad.setWindowTitle(_translate("notepad", "MainWindow", None))
        self.closeButton.setText(_translate("notepad", "Quit", None))
        self.button_open.setText(_translate("notepad", "Open", None))
        self.button_save.setText(_translate("notepad", "Save", None))

