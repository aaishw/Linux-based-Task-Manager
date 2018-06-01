# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Third_s.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os, datetime

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

class Ui_Third_s(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 	

    def setupUi(self, Third_s):
        Third_s.setObjectName(_fromUtf8("Third_s"))
        Third_s.setGeometry(100,60,800,500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Third_s)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.main_verticalLayout = QtGui.QVBoxLayout()
        self.main_verticalLayout.setObjectName(_fromUtf8("main_verticalLayout"))
        self.horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("horizontalLayout_For_LineEditSearchBox"))
        self.UName_search = QtGui.QLineEdit(Third_s)
        self.UName_search.setObjectName(_fromUtf8("UName_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.UName_search)
        self.PName_search = QtGui.QLineEdit(Third_s)
        self.PName_search.setObjectName(_fromUtf8("PName_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.PName_search)
        self.LAdd_search = QtGui.QLineEdit(Third_s)
        self.LAdd_search.setObjectName(_fromUtf8("LAdd_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.LAdd_search)
        self.RAdd_search = QtGui.QLineEdit(Third_s)
        self.RAdd_search.setObjectName(_fromUtf8("RAdd_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.RAdd_search)
        self.main_verticalLayout.addLayout(self.horizontalLayout_For_LineEditSearchBox)
        self.main_Stacked_Widget = QtGui.QStackedWidget(Third_s)
        self.main_Stacked_Widget.setObjectName(_fromUtf8("main_Stacked_Widget"))
        self.stacked_widget_pageOne = QtGui.QWidget()
        self.stacked_widget_pageOne.setObjectName(_fromUtf8("stacked_widget_pageOne"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.stacked_widget_pageOne)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.stacked_widget_pageOne)
        self.tableWidget.setWordWrap(True)
	self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)        
	#self.tableWidget.horizontalHeader().setResizeMode(1)
	#self.tableWidget.horizontalHeader().setHorizontalScrollBarPolicy(2)
	self.tableWidget.resizeColumnsToContents()
        self.tableWidget.verticalHeader().hide()
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.main_Stacked_Widget.addWidget(self.stacked_widget_pageOne)
        self.main_verticalLayout.addWidget(self.main_Stacked_Widget)

	self.back_to_first = QtGui.QPushButton(Third_s)
	self.back_to_first.setObjectName(_fromUtf8("back_to_first"))
	self.main_verticalLayout.addWidget(self.back_to_first)
	self.back_to_first.setMaximumSize(QtCore.QSize(100, 16777215))

	self.back_to_first.setFocusPolicy(QtCore.Qt.TabFocus)
	self.back_to_first.setFocus()

        self.verticalLayout_2.addLayout(self.main_verticalLayout)

        self.retranslateUi(Third_s)
        QtCore.QMetaObject.connectSlotsByName(Third_s)

    def retranslateUi(self, Third_s):
        Third_s.setWindowTitle(_translate("Third_s", "File I/O ", None))
        self.UName_search.setPlaceholderText(_translate("Third_s","", None))
        self.PName_search.setPlaceholderText(_translate("Third_s", "", None))
        self.LAdd_search.setPlaceholderText(_translate("Third_s", "", None))
        self.RAdd_search.setPlaceholderText(_translate("Third_s", "", None))
	self.back_to_first.setText(_translate("Third_s", "Back", None))		
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Third_s", "User Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Third_s", "Process Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Third_s", "Access Time", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Third_s", "Path Name", None))

    def mapUserIdToUsername(self):
	self.id_to_uname_map = {}
	with open('/etc/passwd','r') as fd:
		for line in fd:
        		data = line.split(":")
			uid = int(data[2])
			uname = data[0] 
			self.id_to_uname_map[uid] = uname
	return self.id_to_uname_map 

    def table(self,openFiles):
	self.tableWidget.setSortingEnabled(False)
	self.tableWidget.setRowCount(len(openFiles))
	for row in range(len(openFiles)):
       		for column in range(4):
			userFileitem = QtGui.QTableWidgetItem(str(openFiles[row][column]))
			self.tableWidget.setItem(row,column,userFileitem)		
	#self.tableWidget.setSotingEnabled(True)
	self.tableWidget.resizeColumnsToContents()	
	self.tableWidget.horizontalHeader().setResizeMode(0)
	self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def getFilterResult(self,username,fname,id_to_uname_map):
	
	File = False
	try:
		if(len(self.UName_search.text()) > 2):
			file_stat = self.ftable(username,fname,id_to_uname_map)
			file_stat = [usern for usern in file_stat if usern[0].startswith(self.UName_search.text())]
			File = True	
		if(len(self.PName_search.text()) > 2):
			file_stat = self.ftable(username,fname,id_to_uname_map)
			file_stat = [processn for processn in file_stat if processn[1].startswith(self.PName_search.text())]
			File = True	
		if(len(self.LAdd_search.text()) > 2):
			file_stat = self.ftable(username,fname,id_to_uname_map)
			file_stat = [ladd for ladd in file_stat if ladd[2].startswith(self.LAdd_search.text())]
			File = True	
		if(len(self.RAdd_search.text()) > 2):
			file_stat = self.ftable(username,fname,id_to_uname_map)
			file_stat = [radd for radd in file_stat if radd[3].startswith(self.RAdd_search.text())]
			File = True
		if(len(self.UName_search.text()) == 0 and len(self.PName_search.text()) == 0 and len(self.LAdd_search.text()) == 0 and len(self.RAdd_search.text()) == 0):
			file_stat = self.ftable(username,fname,id_to_uname_map)	
			File = True	
	except TypeError:
		print ""
	if(File == True):
		self.table(file_stat)
	
    def ftable(self,username,fname,id_to_uname_map):
	openFiles = []
	processDirectoryInProc = os.listdir('/proc')
	for processId in processDirectoryInProc:
		bool = any(not char.isdigit() for char in processId)
		if not bool:
			processPath = '/proc/'+processId+"/"
			try:
				statusData = ""
				with open(processPath+"status") as userId:
					statusData = userId.readlines() 
				if username == "*" or str(username) in str(id_to_uname_map.get(int(statusData[8].split()[1]))):	
					for fds in os.listdir(processPath+"fd/"):
					 #def showMessageBox(self,title,message):
					#msgBox = QtGui.QMessageBox()
					#msgBox.setIcon(QtGui.QMessageBox.Warning)

            					if os.path.isfile(processPath+"fd/"+fds) or os.path.isdir(processPath+"fd/"+fds):
                					filepath = os.readlink(processPath+"fd/"+fds)
                					if os.path.isfile(filepath) or os.path.isdir(processPath+"fd/"+fds):
                    						if str(fname) in str(filepath) or fname == "*":
                        						filterStrings = ['/dev/', 'socket:[', 'pipe','anon_inode:']
                        						found = False
									
                        						for filter1 in filterStrings:
                            							if filter1 in filepath:
                                							found = True
                                							break
                       	 						if not found:
                            							time_access = datetime.datetime.fromtimestamp(os.stat(filepath).st_atime)
        									stime_access = time_access.strftime('%b %d, %Y - %H:%M:%S')
                            							openFiles.append([id_to_uname_map.get(int(statusData[8].split()[1])),(statusData[0].split()[1]),stime_access,filepath])
							
			except IOError:		
				continue;
	if(len(self.UName_search.text()) == 0 and len(self.PName_search.text()) == 0 and len(self.LAdd_search.text()) == 0 and len(self.RAdd_search.text()) == 0):
		self.table(openFiles)

	return openFiles		

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Third_s()
	ex.show()	
