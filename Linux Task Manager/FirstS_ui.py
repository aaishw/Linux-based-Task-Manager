# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First_s.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
from Fourth_s import Ui_Fourth_s
from Second_s import Ui_Second_s
from Third_s import Ui_Third_s

#self.fname = ""

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

class Ui_First_s(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self)

    def setupUi(self, First_s):
        First_s.setObjectName(_fromUtf8("First_s"))
	First_s.setGeometry(100,60,800,500)
        self.label = QtGui.QLabel(First_s)
        self.label.setGeometry(QtCore.QRect(70, 50, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.username_first = QtGui.QTextEdit(First_s)
        self.username_first.setGeometry(QtCore.QRect(160, 40, 181, 31))
        self.username_first.setObjectName(_fromUtf8("username_first"))
        self.file_radiobtn = QtGui.QRadioButton(First_s)
        self.file_radiobtn.setGeometry(QtCore.QRect(160, 100, 117, 22))
        self.file_radiobtn.setObjectName(_fromUtf8("file_radiobtn"))
        self.network_radiobtn = QtGui.QRadioButton(First_s)
        self.network_radiobtn.setGeometry(QtCore.QRect(260, 100, 117, 22))
        self.network_radiobtn.setObjectName(_fromUtf8("network_radiobtn"))
        self.label_2 = QtGui.QLabel(First_s)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.submit_first = QtGui.QPushButton(First_s)
        self.submit_first.setGeometry(QtCore.QRect(160, 140, 181, 27))
        self.submit_first.setObjectName(_fromUtf8("submit_first"))

        self.retranslateUi(First_s)
        QtCore.QMetaObject.connectSlotsByName(First_s)

    def retranslateUi(self, First_s):
        First_s.setWindowTitle(_translate("First_s", "File and Network activities", None))
        self.label.setText(_translate("First_s", "Username:", None))
        self.file_radiobtn.setText(_translate("First_s", "File I/O", None))
        self.network_radiobtn.setText(_translate("First_s", "Network I/O", None))
        #self.label_2.setText(_translate("First_s", None, None))
        self.submit_first.setText(_translate("First_s", "Submit", None))		
	self.submit_first.clicked.connect(self.GoToNext)

    def GoToNext(self):
	username_null = 0
	username = self.username_first.toPlainText()	
	
	#if username == "":
	#	self.showMessageBox("Enter Username or '*'")
	#	username_null = 1
	
	if self.file_radiobtn.isChecked(): #and username !="":	
		radioButton = self.file_radiobtn.text()
		self.StartFileIOStat(username)	

	elif self.network_radiobtn.isChecked(): #and username !="":
		radioButton = self.network_radiobtn.text()		
		self.StartNetworkStat(username)
	else:
		if username_null == 0:
			self.showMessageBox("Select any of the two radio buttonn")

    def StartFileIOStat(self,username):
	self.second = QtGui.QWidget()
	self.ui = Ui_Second_s()
	self.ui.setupUi(self.second)
	self.ui.usernameLineEdit.setText(username)
	self.hide()
	self.second.show()
	self.ui.submit_Second_s.clicked.connect(lambda :self.call_Third_s(username,self.ui.fname_lineEdit.text()))
	self.ui.previousScreen_Second_s.clicked.connect(lambda :self.BackToFirst())

    def call_Third_s(self,username,fname):
	#self.ui = Ui_Second_s()
	#self.fname = self.ui.fname_lineEdit.text()
	self.third = QtGui.QWidget()
	self.ui = Ui_Third_s()
	self.ui.setupUi(self.third)
	id_to_uname_map = self.ui.mapUserIdToUsername()
	self.ui.ftable(username,fname,id_to_uname_map)
	self.ui.back_to_first.clicked.connect(lambda :self.BackToSecond(username))
	self.ui.UName_search.textEdited.connect(lambda :self.ui.getFilterResult(username,fname,id_to_uname_map))
	self.ui.PName_search.textEdited.connect(lambda :self.ui.getFilterResult(username,fname,id_to_uname_map))
	self.ui.LAdd_search.textEdited.connect(lambda :self.ui.getFilterResult(username,fname,id_to_uname_map))
	self.ui.RAdd_search.textEdited.connect(lambda :self.ui.getFilterResult(username,fname,id_to_uname_map))
	self.second.hide()
	self.third.show()
	self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(lambda :self.ui.ftable(username,fname,id_to_uname_map))
	self.timer.start()

    def BackToSecond(self,username):
	self.timer.stop()	
	self.StartFileIOStat(username)
	self.third.hide()	

    def BackToFirst(self):
	self.second.hide()
	self.show()	

    def StartNetworkStat(self,username):
	self.fourthScreen = QtGui.QWidget()
	self.ui = Ui_Fourth_s()
	self.ui.setupUi(self.fourthScreen)
	id_to_uname_map = self.ui.mapUserIdToUsername()	
	self.ui.ntable(username,id_to_uname_map)
	self.ui.UName_search.textEdited.connect(lambda :self.ui.getFilterResult(username,id_to_uname_map))
	self.ui.PName_search.textEdited.connect(lambda :self.ui.getFilterResult(username,id_to_uname_map))
	self.ui.LAdd_search.textEdited.connect(lambda :self.ui.getFilterResult(username,id_to_uname_map))
	self.ui.RAdd_search.textEdited.connect(lambda :self.ui.getFilterResult(username,id_to_uname_map))
	self.hide()
	self.fourthScreen.show()
	self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(lambda :self.ui.ntable(username,id_to_uname_map))
	self.timer.start()
	self.ui.back_to_first.clicked.connect(lambda :self.restoreMainScreen())	

    def restoreMainScreen(self):
	self.timer.stop()
	self.fourthScreen.hide()
	self.show()

   	#msgBox.setWindowTitle(title)
	#msgBox.setText(message)
	#msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
	#msgBox.exec_()

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_First_s()
	ex.show()
	sys.exit(app.exec_())
