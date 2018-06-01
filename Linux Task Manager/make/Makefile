obj-m:=my_test.o

all:
	make -C /lib/modules/4.10.0-35-generic/build M=$(PWD) modules
clean: 	
	make -C /lib/modules/4.10.0-35-generic/build M=$(PWD) clean 
