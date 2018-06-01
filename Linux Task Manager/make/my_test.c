//File Name my_test.c
#include<linux/module.h> /* Needed by all modules */
#include<linux/kernel.h> /* Needed for KERN_INFO */
int my_variable =1;
int my_init(void)
{
 	printk(KERN_INFO"How Are You? 1.\n");
 // A non 0 return means init_module failed; module can't be loaded.
 	return 0;
}
void my_cleanup(void)
{
 	printk(KERN_INFO"Goodbye end of the world 1.\n");
} 
EXPORT_SYMBOL_GPL(my_variable);
module_init(my_init);
module_exit(my_cleanup);
