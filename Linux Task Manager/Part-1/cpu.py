import time

#last_worktime=0
#last_idletime=0
pre_user=0
pre_sys=0
pre_idle=0
cur_user=0
cur_sys=0
cur_idle=0
#def get_cpu():
#last_worktime=0, last_idletime=0


num=0
while (1):
	f=open("/proc/stat","r")
	line=f.readlines()
	i=0
	flag=0
	use1=0
	sys1=0
	idle1=0
	while (1): 
		f=open("/proc/stat","r")
		line=f.readlines()
		if "cpu" in line[i]:
			spl=line[i].split()
			use1=float(spl[1])
			use1=use1/100
			print"------------------------------",spl[0]
			print "User:",spl[0],use1, str("sec")
			sys1=float(spl[3])
			sys1=sys1/100
			#use1= map(int,spl[1])
			print "System Mode:",spl[0],sys1, str("sec")
			#sys1= map(int,spl[3])
			idle1=float(spl[4])
			idle1=idle1/100	
			if flag==0:
				pre_user=use1
				#rdprint"user in if",pre_user
				pre_sys=sys1
				pre_idle=idle1
				time.sleep(5)		
				flag=1
			else:
				cur_user=use1
				cur_sys=sys1
				cur_idle=idle1
				temp1=0	
				print "pre_user",pre_user
				print "cur_user", cur_user
				print "pre_sys", pre_sys
				print "cur_sys", cur_sys
				print "pre_idle", pre_idle
				print "cur_idle", cur_idle				
				temp1=(cur_user+cur_sys)-(pre_user+pre_sys)
				cpu1=temp1*100/(temp1+(cur_idle-pre_idle))
				print "CPU utilization:", cpu1, str("%")  
				flag=0
				i=i+1
	#----------------------------------------------------------------------------
#, "System:"spl[2], "Total:"spl[4]	
				
		
		elif "intr" in line[i]:
			spl=line[i].split()
			print "Interrupts:",spl[1]
		elif "ctxt" in line[i]:
			spl=line[i].split()
			print "Context Switch:",spl[1]
		else:
			break
		i=i+1	
	num=num+1		
	
	f=open("/proc/meminfo","r")
	line=f.readlines()
	if "MemTotal" in line[0]:
		spl=line[0].split()
		mb=int(spl[1])/1024
		print "Total Memory:",mb,str("MB")


	if "MemFree" in line[1]:
		spl=line[1].split()
		mb=int(spl[1])/1024
		#n=1024
		print "Memory Free:",mb,str("MB")
		print "--------------------------------------------------"
	time.sleep(2)
print "he;;o"


