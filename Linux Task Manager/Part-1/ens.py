#for line in open("/proc/net/dev",'r'):

from subprocess import Popen, PIPE
import subprocess

 
f=open("/proc/net/dev",'r')
while 1:
  line=f.readline()
  if not line: break
  print line  
f.close()
#print line


#subprocess.call('ethtool','ens33')	


process = Popen(['ethtool', 'ens33'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()


#subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
 # Run command with arguments and return its output as a byte string.


s = subprocess.check_output(["ethtool", "ens33"])
print("s = " + s)

pid= raw_input("Enter the process number:")
print pid
f=open("/proc/"pid"/stat",'r')
line = f.readline()
print line



 #file="\2091\sample.txt"
  #  path=os.getcwd()+file
   # fp=open(path,'r+');


#----------------to be added to net.py
for cnt in line[4:]:
		spl= cnt.split()
		pre_receiveb=float(spl[1])
		pre_transb= float(spl[9])
		pre_totb=pre_receiveb+pre_transb
		flag_bytes=1
		print "port:",spl[0]
		print "previous receive val:",pre_receiveb

		time.sleep(5)
		f=open("/proc/net/dev","r")
		line=f.readlines()
		spl=line[j].strip().split()
		spl=cnt.split()

		cur_receiveb=float(spl[1])
		cur_transb= float(spl[9])
		cur_totb=cur_receiveb+cur_transb
		print "port:",spl[0]
		print "current receive val:", cur_receiveb
		diff_totb=cur_totb - pre_totb

		print "Change in bytes:", diff_totb
		#print "Change in bytes transmitted:",diff_transb
		flag_bytes=0
#--------------above to be added





