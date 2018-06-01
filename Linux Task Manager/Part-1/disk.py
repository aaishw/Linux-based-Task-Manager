import time
import os
import re

flag_disk=0
pre_read=0
cur_read=0
diff_disk=0
pre_readb=0
cur_readb=0
pre_write=0
cur_write=0
pre_writeb=0
cur_writeb=0

num=0
while (1):
	#os.system('clear')
	f=open("/proc/diskstats","r")
	line=f.readlines()
	i=0
	while (1): 
		spl=line[i].split()
		m = re.search(r'\d+$', spl[2])
		if re.match('sd',spl[2]) and m is None:
			spl=line[i].split()
			#re.match('sd',spl[2])
			#print spl[2]		
			if flag_disk==0:
				#print "----------------",spl[2]
				pre_read=int(spl[3])
				pre_readb=int(spl[5])
				pre_write=int(spl[7])
				pre_writeb=int(spl[9])				
				flag_disk=1
			else: 
				cur_read=int(spl[3])
				cur_readb=int(spl[5])
				cur_write=int(spl[7])
				cur_writeb=int(spl[9])
				flag_disk=0
				diff_disk=cur_read-pre_read
				os.system('clear')
				print "                      Disk Stats", spl[2]
				print "-----------------------------------------------------------------------"
				print "Increment in Number of Read (since last 5 sec):		 ",diff_disk
				print "Number of Reads (counter since last reboot):	    	 ",cur_read
				print "\n"
				diff_disk=cur_readb-pre_readb
				print "Increment in Number of Blocks Read (since last 5 sec):	 ",diff_disk
				print "Number of Reads (counter since last reboot):	    	 ",cur_readb
				print "\n"
				diff_disk=cur_write-pre_write
				print "Increment in Number of writes (since last 5 sec):	 ",diff_disk
				print "Number of Writes (counter since last reboot):	    	 ",cur_write
				print "\n"
				diff_disk=cur_writeb-pre_writeb
				print "Increment in Number of Blocks written (since last 5 sec): ",diff_disk
				print "Number of Blocks written (counter since last reboot):	 ",cur_writeb
				print "------------------------------------------------------------------------"
				print "\n"
			#print "Number of Blocks read:",spl[5]
			#print "Number of Writes:",spl[7]
			#print "Number of Blocks written:",spl[9]
			break
				
		#else:
		#	break
		i=i+1
	#print "--------------------------------------------------"	
	time.sleep(5)
print "he;;o"

#field 1 = number of read
#field 3 blocks read
#filed 5 = number of writes
#field 7=blocks written


