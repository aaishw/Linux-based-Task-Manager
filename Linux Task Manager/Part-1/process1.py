import time
import subprocess
import os

pro_id = raw_input("Please enter process id:")

# userTime[cpu,cpu0,cpu1,cpu2,...] each column will be filled when if cpu in f_stat_lines[i] condition will be true
user_time = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
sys_time = []

# userTime[cpu,cpu0,cpu1,cpu2,...]
idle_time = []

cur_usert_pro = 0.0
pre_usert_pro = 0.0
diff_usert_pro = 0.0

cur_syst_pro = 0.0
pre_syst_pro = 0.0
diff_syst_pro = 0.0

cur_idlet_pro = 0.0
pre_idlet_pro = 0.0
diff_idlet_pro = 0.0

#infinite loop
while(1):

	#open stat file to get cpu user time and cpu system time, interrupts and context swtich 
	f_stat = open("/proc/"+pro_id+"/stat")
	
	#open file meminfo to get total and available memory information
	f_mem  = open("/proc/meminfo")

	# read all the lines in the file and return them in a list
	f_stat_lines = f_stat.readlines()
	f_mem_lines = f_mem.readlines()
	
	spl_stat = f_stat_lines[0].split()
	cur_usert_pro = float(spl_stat[13])
	cur_syst_pro = float(spl_stat[14])
	cur_idlet_pro = float(spl_stat[15]) + float(spl_stat[16])	
			
	if len(user_time)-1 >= 0: 
		pre_usert_pro = user_time.pop(0)
	else:
		pre_usert_pro = 0.0
			
	diff_usert_pro = cur_usert_pro - pre_usert_pro
			
	if len(sys_time)-1 >= 0:
		pre_syst_pro = sys_time.pop(0)
	else:
		pre_syst_pro = 0.0
			
	diff_syst_pro = cur_syst_pro - pre_syst_pro
			
	if len(idle_time)-1 >= 0:
		pre_idlet_pro = idle_time.pop(0)
	else:
		pre_idlet_pro = 0.0
			
	diff_idlet_pro = cur_idlet_pro - pre_idlet_pro
	cur_usert_pro=cur_usert_pro/100
	cur_syst_pro=cur_syst_pro/100
	cur_idlet_pro=cur_idlet_pro/100
	diff_usert_pro=diff_usert_pro/100
	diff_syst_pro=diff_syst_pro/100
	diff_idlet_pro=diff_idlet_pro/100
	###############################################################################################################################
	diff_tot_timel = diff_usert_pro+diff_syst_pro*200
	print "                   Details for Process Id:"+spl_stat[0]
	print "-------------------------------------------------------"
	print "Process time in User mode:	         %0.2f"%cur_usert_pro," Sec"
	print "Process time in System mode:	         %0.2f"%cur_syst_pro," Sec"
	
	print "Change in User mode time:		 %0.2f"%diff_usert_pro," Sec"
	print "Change in System mode time: 		 %0.2f"%diff_syst_pro," Sec"
		
	
	user_time.append(cur_usert_pro)	
	sys_time.append(cur_syst_pro)
	idle_time.append(cur_idlet_pro)
	s=open("/proc/stat","r")
	line=s.readlines()
	if "cpu" in line[0]:
		spl=line[0].split()
		pre_use1=float(spl[1])
		pre_use1=pre_use1/100
		pre_sys1=float(spl[3])
		pre_sys1=pre_sys1/100
		pre_total_cput=pre_use1+pre_sys1
		pre_idle1=float(spl[4])
		pre_idle1=pre_idle1/100
		time.sleep(3)
		s=open("/proc/stat","r")
		line=s.readlines()
	if "cpu" in line[0]:
		spl=line[0].split()
		cur_use1=float(spl[1])
		cur_use1=pre_use1/100
		cur_sys1=float(spl[3])
		cur_sys1=pre_sys1/100
		cur_total_cput=cur_use1+cur_sys1
		cur_idle1=float(spl[4])
		cur_idle1=cur_idle1/100
		diff_tot_time1=cur_total_cput-pre_total_cput
		diff_idlet=cur_idle1-pre_idle1		
				
	overall_util = (((diff_usert_pro + diff_syst_pro) * 100) / (diff_tot_timel + diff_idlet))
	print "Overall CPU Utilization		         %0.3f"%overall_util," %"
	
	################################################## For Virtual Memory #########################################################
	out = open('pro_file.txt','wb')		
	subprocess.call(['uname','-m'],stdout = out,stderr=subprocess.STDOUT)
	f = open('pro_file.txt','r')
	
	arch_type = f.readline()
	#print arch_type
	
	#clear file data
	open('pro_file', 'w').close()
	
	if arch_type == 'i686':
		arch_type = 32
	else:
		arch_type = 64

	print "Architecture type :		        ",arch_type	
	# v_mem is in bytes
	v_mem= float(spl_stat[22])
	v_mem= v_mem/(10**6)
	print "Virtual Memory used by this process:     %0.2f"%v_mem," kB" 
	
	v_mem_util= (v_mem * 100)/(2**arch_type)

	print "Virtual Memory Utilization:              %0.2f"%v_mem_util," %"	
	
	#--------------------------------------------------------- Physical memory 
	phy_mem= spl_stat[23]
	#print "Physical Memory in pages:               ",phy_mem," pages"
	
	out = open('pro_file.txt','wb')		
	subprocess.call(['getconf','PAGESIZE'],stdout = out,stderr=subprocess.STDOUT)
	f = open('pro_file.txt','r')
	
	#page_sizeb = f.readline()
	#print page_sizeb
	
	#clear file data
	open('pro_file', 'w').close()
	page_sizeb = 4
	phy_memb= float(phy_mem)*float(page_sizeb)
	#phy_memb= phy_memb/(10**3)
	print "Physical Memory in bytes:                %0.2f"%phy_memb," kB"
	
	tot_mem= float(f_mem_lines[0].split()[1])
	tot_mem= tot_mem/1000
	print "Total memory:		                 %0.2f"%tot_mem," kB"

	phy_mem_util = (phy_memb/1000)*100 / tot_mem
	print "Physical Memory Utilization:	         %0.3f"%phy_mem_util," %"
	print "-------------------------------------------------------"	
	time.sleep(5)
	os.system("clear")
	#----------------------------------------------------------------end
