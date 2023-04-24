#include <linux/module.h>
#include <linux/fs.h>
#include <asm/io.h>


#define NOD_MAJOR 100
#define NOD_NAME "nobrand"

MODULE_LICENSE("GPL");

static volatile uint32_t *BASE;
static volatile uint32_t *GPFSEL0;
static volatile uint32_t *GPSET_PUP_REG0;
static volatile uint32_t *GPLEV0;
int lev;




static int nobrand_open(struct inode *inode, struct file *filp)
{
    printk(KERN_INFO "welcome\n");
    return 0;
}

static int nobrand_release(struct inode *inode, struct file *filp)
{
    printk(KERN_INFO "release\n");
    return 0;
}

static void ledon(void){
    printk(KERN_INFO "LED ON\n");
    *GPSET0 = (1<<18);
}

static void ledoff(void){
    printk(KERN_INFO "LED OFF\n");
    *GPCLR0 = (1<<18);
}

static long nobrand_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
	switch(cmd){
		case _IO(0,3):
			ledon();
			break;
		case _IO(0,4):
		    ledoff();
		    break;
        case _IO(0,7):
            lev = (*GPLEV0 >> 2) &1;
            printk(KERN_ALERT "BTN read %d", lev);
            ret = copy_to_usr((void*)arg, &lev, sizeof(int));
            break;
	}
	return 0;
}

static struct file_operations fops = {
    .open = nobrand_open,
    .release = nobrand_release,
	.unlocked_ioctl = nobrand_ioctl,
};

static int nobrand_init(void)
{

    if (register_chrdev(NOD_MAJOR, NOD_NAME, &fops) < 0)
    {
        printk("INIT FALE\n");
    }

    BASE = (uint32_t *)ioremap(0xFE200000,256);
    GPFSEL0 = BASE + (0x00 / 4);
    *GPFSEL0 &=~(0x7 << 24);

    GPIO_PUP_REG0 = BASE + (0xe4 / 4);
    *GPIO_PUP_REG0 &=~(0x3 << 4);
    *GPIO_PUP_REG0 = (0x1 << 4);

    GPLEV0 = BASE + (0x34 / 4);
    return 0;
}

static void nobrand_exit(void)
{
    *GPCLR0 = (1<<18);
    iounmap(BASE);

	unregister_chrdev(NOD_MAJOR, NOD_NAME);
    printk(KERN_INFO "bye\n");
}



module_init(nobrand_init);
module_exit(nobrand_exit);

