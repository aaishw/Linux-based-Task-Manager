# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Second_s.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os

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

class Ui_Second_s(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 

    def setupUi(self, Second_s):
        Second_s.setObjectName(_fromUtf8("Second_s"))
        Second_s.setGeometry(100,60,800,500)
        self.formLayout_2 = QtGui.QFormLayout(Second_s)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.formLayout)
        self.username = QtGui.QLabel(Second_s)
        self.username.setObjectName(_fromUtf8("username"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.username)
        
	self.usernameLineEdit = QtGui.QLabel(Second_s)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
	#self.usernameLineEdit.setReadOnly(True)
        
	self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.usernameLineEdit)
        self.monitorLabel = QtGui.QLabel(Second_s)
        #self.monitorLabel.setObjectName(_fromUtf8("monitorLabel"))
        #self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.monitorLabel)
        self.fileI_O_Label = QtGui.QLabel(Second_s)
        self.fileI_O_Label.setObjectName(_fromUtf8("fileI_O_Label"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.fileI_O_Label)
        self.fname_lineEdit = QtGui.QLineEdit(Second_s)
        self.fname_lineEdit.setObjectName(_fromUtf8("fname_lineEdit"))
	self.fname_lineEdit.setMaximumSize(QtCore.QSize(280, 16777215)) 
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.SpanningRole, self.fname_lineEdit)
        
	self.username.setFocusPolicy(QtCore.Qt.TabFocus)
	self.username.setFocus()

	self.submit_Second_s = QtGui.QPushButton(Second_s)
        self.submit_Second_s.setObjectName(_fromUtf8("submit_Second_s"))
	self.submit_Second_s.setMaximumSize(QtCore.QSize(100, 16777215))        
	self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.submit_Second_s)
        self.previousScreen_Second_s = QtGui.QPushButton(Second_s)
        self.previousScreen_Second_s.setObjectName(_fromUtf8("previousScreen_Second_s"))
	self.previousScreen_Second_s.setMaximumSize(QtCore.QSize(100, 16777215))
        
	self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.previousScreen_Second_s)

        self.retranslateUi(Second_s)
        QtCore.QMetaObject.connectSlotsByName(Second_s)

    def retranslateUi(self, Second_s):
        Second_s.setWindowTitle(_translate("Second_s", "File I/O", None))
        self.username.setText(_translate("Second_s", "Username", None))
        #self.monitorLabel.setText(_translate("Second_s", "Monitor", None))
        #self.fileI_O_Label.setText(_translate("Second_s", "File I/O", None))
        self.submit_Second_s.setText(_translate("Second_s", "Submit", None))
        self.previousScreen_Second_s.setText(_translate("Second_s", "Back", None))
	self.fname_lineEdit.setPlaceholderText(_translate("Second_s", " File Path", None))

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Second_s()
	ex.show()	
	sys.exit(app.exec_())
