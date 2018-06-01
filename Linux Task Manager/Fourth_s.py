# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fourth_s.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, os, struct, socket

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

class Ui_Fourth_s(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.setupUi(self) 	

    def setupUi(self, Fourth_s):
        Fourth_s.setObjectName(_fromUtf8("Fourth_s"))
        Fourth_s.setGeometry(100,60,800,500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Fourth_s)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.main_verticalLayout = QtGui.QVBoxLayout()
        self.main_verticalLayout.setObjectName(_fromUtf8("main_verticalLayout"))
        self.horizontalLayout_For_LineEditSearchBox = QtGui.QHBoxLayout()
        self.horizontalLayout_For_LineEditSearchBox.setObjectName(_fromUtf8("horizontalLayout_For_LineEditSearchBox"))
        self.UName_search = QtGui.QLineEdit(Fourth_s)
        self.UName_search.setObjectName(_fromUtf8("UName_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.UName_search)
        self.PName_search = QtGui.QLineEdit(Fourth_s)
        self.PName_search.setObjectName(_fromUtf8("PName_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.PName_search)
        self.LAdd_search = QtGui.QLineEdit(Fourth_s)
        self.LAdd_search.setObjectName(_fromUtf8("LAdd_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.LAdd_search)
        self.RAdd_search = QtGui.QLineEdit(Fourth_s)
        self.RAdd_search.setObjectName(_fromUtf8("RAdd_search"))
        self.horizontalLayout_For_LineEditSearchBox.addWidget(self.RAdd_search)
        self.main_verticalLayout.addLayout(self.horizontalLayout_For_LineEditSearchBox)
        self.main_Stacked_Widget = QtGui.QStackedWidget(Fourth_s)
        self.main_Stacked_Widget.setObjectName(_fromUtf8("main_Stacked_Widget"))
        self.stacked_widget_pageOne = QtGui.QWidget()
        self.stacked_widget_pageOne.setObjectName(_fromUtf8("stacked_widget_pageOne"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.stacked_widget_pageOne)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.stacked_widget_pageOne)
        #self.tableWidget.setWordWrap(True)
	self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tableWidget.setCornerButtonEnabled(True)
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
	self.tableWidget.horizontalHeader().setResizeMode(1)
        self.tableWidget.verticalHeader().hide()
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.main_Stacked_Widget.addWidget(self.stacked_widget_pageOne)
        self.main_verticalLayout.addWidget(self.main_Stacked_Widget)

	self.back_to_first = QtGui.QPushButton(Fourth_s)
	self.back_to_first.setObjectName(_fromUtf8("back_to_first"))
	self.main_verticalLayout.addWidget(self.back_to_first)
	self.back_to_first.setMaximumSize(QtCore.QSize(100, 16777215))

	self.back_to_first.setFocusPolicy(QtCore.Qt.TabFocus)
	self.back_to_first.setFocus()

        self.verticalLayout_2.addLayout(self.main_verticalLayout)

        self.retranslateUi(Fourth_s)
        QtCore.QMetaObject.connectSlotsByName(Fourth_s)

    def retranslateUi(self, Fourth_s):
        Fourth_s.setWindowTitle(_translate("Fourth_s", "Network", None))
        self.UName_search.setPlaceholderText(_translate("Fourth_s", "", None))
        self.PName_search.setPlaceholderText(_translate("Fourth_s","", None))
        self.LAdd_search.setPlaceholderText(_translate("Fourth_s","", None))
        self.RAdd_search.setPlaceholderText(_translate("Fourth_s", "", None))
	self.back_to_first.setText(_translate("Fourth_s", "Back", None))		
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Fourth_s", "User Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Fourth_s", "Process Name", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Fourth_s", "Local Address", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Fourth_s", "Remote Address", None))

    def getFilterResult(self,username,id_to_uname_map):
	
	Net = False
	try:
		if(len(self.UName_search.text()) > 2):
			net_stat = self.ntable(username,id_to_uname_map)
			net_stat = [usern for usern in net_stat if usern[0].startswith(self.UName_search.text())]
			Net = True	
		if(len(self.PName_search.text()) > 2):
			net_stat = self.ntable(username,id_to_uname_map)
			net_stat = [processn for processn in net_stat if processn[1].startswith(self.PName_search.text())]
			Net = True	
		if(len(self.LAdd_search.text()) > 2):
			net_stat = self.ntable(username,id_to_uname_map)
			net_stat = [ladd for ladd in net_stat if ladd[2].startswith(self.LAdd_search.text())]
			Net = True	
		if(len(self.RAdd_search.text()) > 2):
			net_stat = self.ntable(username,id_to_uname_map)
			net_stat = [radd for radd in net_stat if radd[3].startswith(self.RAdd_search.text())]
			Net = True
		if(len(self.UName_search.text()) == 0 and len(self.PName_search.text()) == 0 and len(self.LAdd_search.text()) == 0 and len(self.RAdd_search.text()) == 0):
			net_stat = self.ntable(username,id_to_uname_map)	
			Net = True	
	except TypeError:
		print ""
	if(Net == True):
		self.table(net_stat)

    def table(self,net_stat):
	self.tableWidget.setSortingEnabled(False)
	self.tableWidget.setRowCount(len(net_stat))
	for row in range(len(net_stat)):
       		for column in range(4):
			usernetitem = QtGui.QTableWidgetItem(str(net_stat[row][column]))
			self.tableWidget.setItem(row,column,usernetitem)		
	self.tableWidget.setSortingEnabled(True)
	
    def mapUserIdToUsername(self):
	self.id_to_uname_map = {}
	with open('/etc/passwd','r') as fd:
		for line in fd:
        		data = line.split(":")
			uid = int(data[2])
			uname = data[0] 
			self.id_to_uname_map[uid] = uname
	return self.id_to_uname_map
	
    def ntable(self,username,id_to_uname_map):
	networkData = {}	
	net_stat = []
	i = 0
	with open("/proc/net/tcp") as tcpFile:
		for tcpLine in tcpFile:
			if i != 0:
				tcpData = tcpLine.split()
				
				localAddressTcp = tcpData[1].split(":")[0]	
				localAddressTcpPort = tcpData[1].split(":")[1]
				addrl = int(localAddressTcp,16)
				localAddressTcp = socket.inet_ntoa(struct.pack("<L", addrl))
				#try:
				#	dns = socket.gethostbyaddr(localAddressTcp)
				#	success = True
				#except socket.herror:
				#	success = False;
					
				#if success:
				#	localAddressTcp = dns[0]	 

				localAddressTcpPort = int(localAddressTcpPort,16)				 	

				remoteAddressTcp = tcpData[2].split(":")[0]	
				remoteAddressTcpPort = tcpData[2].split(":")[1]
				addrl = int(remoteAddressTcp,16)
				remoteAddressTcp = socket.inet_ntoa(struct.pack("<L", addrl))
				
				#try:
				#	dns = socket.gethostbyaddr(remoteAddressTcp)
				#	success = True
				#except socket.herror:
				#	success = False;
					
				#if success:
				#	remoteAddressTcp = dns[0]			

				remoteAddressTcpPort = int(remoteAddressTcpPort,16)
	
				networkData[tcpData[9]] = [str(localAddressTcp)+":"+str(localAddressTcpPort),str(remoteAddressTcp)+":"+str(remoteAddressTcpPort)]
			i += 1
	i = 0	
	with open("/proc/net/udp") as udpFile:
		for udpLine in udpFile:
			if i != 0:
				udpData = udpLine.split()
				
				LAddUdp = udpData[1].split(":")[0]	
				LAddUdpPort = udpData[1].split(":")[1]
				addrl = int(LAddUdp,16)
				LAddUdp = socket.inet_ntoa(struct.pack("<L", addrl))

				#try:
				#	dns = socket.gethostbyaddr(LAddUdp)
				#	success = True
				#except socket.herror:
				#	success = False;
				#	
				#if success:
				#	LAddUdp = dns[0]

				LAddUdpPort = int(LAddUdpPort,16)				 	

				RAddUdp = udpData[2].split(":")[0]	
				RAddUdpPort = udpData[2].split(":")[1]
				addrl = int(RAddUdp,16)
				RAddUdp = socket.inet_ntoa(struct.pack("<L", addrl))

				#try:
				#	dns = socket.gethostbyaddr(RAddUdp)
				#	success = True
				#except socket.herror:
				#	success = False;
				#	
				#if success:
				#	RAddUdp = dns[0]

				RAddUdpPort = int(RAddUdpPort,16)
	
				networkData[udpData[9]] = [str(LAddUdp)+":"+str(LAddUdpPort),str(RAddUdp)+":"+str(RAddUdpPort)]
			i += 1
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
					for fds in os.listdir(processPath+"fd"):						
						getInodes = ""
						try:
							getInodes = os.readlink(os.path.join(processPath+"fd",fds))
						except OSError:
							continue;
						if getInodes.startswith("socket:"):
							iNode = getInodes.split(":")[1][1:-1]
							if networkData.get(iNode):
								localAddress = networkData[iNode][0]
								remoteAddress = networkData[iNode][1]
								net_stat.append([id_to_uname_map.get(int(statusData[8].split()[1])),(statusData[0].split()[1]),localAddress,remoteAddress])
							
			except IOError:		
				continue;
	if(len(self.UName_search.text()) == 0 and len(self.PName_search.text()) == 0 and len(self.LAdd_search.text()) == 0 and len(self.RAdd_search.text()) == 0):
		self.table(net_stat)

	return net_stat

if __name__=='__main__':
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Fourth_s()
	ex.show()	
