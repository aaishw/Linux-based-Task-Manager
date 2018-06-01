import subprocess
import time
import re
import os
flag_act=0
cur_act=0
pre_ct=0
diff_act=0
flag_b=0
avg_est=0
est=0
j=0
#diff_totb=0
#net_util=0.0
#num=0
while (1):
	f=open("/proc/net/dev","r")
	#reg1=re.compile('l')
	line=f.readlines()
	spl=line[j].strip().split()
	for cnt in line[4:]:
		spl= cnt.split()
		pre_receiveb=float(spl[1])
		pre_transb= float(spl[9])
		pre_totb=pre_receiveb+pre_transb
		flag_bytes=1
		#print "port:",spl[0]
		#print "previous receive val:",pre_receiveb
		f.close()
	
	f=open("/proc/net/snmp","r")
	line=f.readlines()
	i=0
	while (1): 
		if "Tcp" in line[i]:
			spl=line[i+1].split()
			if flag_act==0:
				pre_act=int(spl[5])
				flag_act=1
			else: 
				cur_act=int(spl[5])
				flag_act=0
				diff_act=cur_act-pre_act
				#print "Change in Active open connections:",diff_act
				#print "Tcp Active open connections (since last reboot):",cur_act
				est=int(spl[9])
				#print "Tcp Current Estblished connections (since last reboot):",est
				#print "\n"
			
			break
		#else:
			#break
		i=i+1	
	print "--------------------------------------------------"	
	#time.sleep(5)
	j=3
	flag_bytes=0
	f=open("/proc/net/dev","r")
	#reg1=re.compile('l')
	line=f.readlines()
	spl=line[j].strip().split()
#	print spl[0]
#	if re.match(reg1,str(spl[0])):
#		print"------------------------",spl[0]
#		print spl[0],"(total bytes recieved):",spl[1]
#		print spl[0],"total bytes transmitted:",spl[9]
#		j=j+1
#		spl=line[j+3].strip().split()
		#break
#       -------------------starts-------------------
	#for cnt in line[2:]:
	if "lo"not in spl[0] or "bridge0" not in spl[0]:
		spl=line[j].strip().split()
		#spl= cnt.split()
		pre_receiveb=float(spl[1])
		pre_transb= float(spl[9])
		pre_totb=pre_receiveb+pre_transb
		flag_bytes=1
		#print "previous receive val:",pre_receiveb
		f.close()
		time.sleep(5)
		f=open("/proc/net/dev","r")
		line=f.readlines()
		spl=line[3].strip().split()
		#spl=cnt.split()

		cur_receiveb=float(spl[1])
		cur_transb= float(spl[9])
		cur_totb=cur_receiveb+cur_transb
		#print "port:",spl[0]
		#print "current receive val:", cur_receiveb
		diff_totb=cur_totb - pre_totb

		#print "Change in bytes:", diff_totb
		#print "Change in bytes transmitted:",diff_transb
		flag_bytes=0

		
		 	


#               ----------------ends here--------------------------------
		open_obj=open('eth_file.txt','wb')
		f=open('eth_file.txt','r')			
		subprocess.call(['ethtool',spl[0][:-1]], stdout = open_obj,stderr=subprocess.STDOUT)

		for lines in f:
			#open_obj=open('eth_file.txt','wb')
			
			
			values = lines.split()
			for i in values:
				if "Speed" in i:
					#print "Bandwidth:", values[1]
					band_string= str(values[1])
					#string_split = band_string.split()
					string_join=int(band_string[0]+band_string[1]+band_string[2]+band_string[3])

					net_util=float((diff_totb*8)/(string_join*1000000))*100
					#print "Net Util: ",net_util,str("%")
					#time.sleep(5)
					os.system('clear')
					print "Network Details"
					print "------------------------------------------------"
					print "Increment in Active open connections (since last 5 sec):       ",diff_act
					print "Tcp Active open connections (counter since last reboot):       ",cur_act
					print "Tcp Current Estblished connections (gauge):		       ",est			
					print "------------------------------------------------",spl[0]
					print "Change in bytes	for last 5 second:		               ", diff_totb
					print "Bandwidth:                            			       ", values[1]
					print "Net Utilization:                               	                %0.3f"%net_util,str("%")
		#for line in f:
		
			
			
	j=j+1
	#print "end of bytes"
print "he;;o"

#Field 5=tcp active open
#Field 9= current Established Connections



