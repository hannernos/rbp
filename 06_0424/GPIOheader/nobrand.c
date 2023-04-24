#include <linux/module.h>
#include <linux/fs.h>
#include <asm/io.h>
#include <linux/gpio.h>

#define NOD_MAJOR 100
#define NOD_NAME "nobrand"

MODULE_LICENSE("GPL");

static volatile uint32_t *BASE;
static volatile uint32_t *GPFSEL1;
static volatile uint32_t *GPSET0;
static volatile uint32_t *GPCLR0;

static volatile uint32_t *GPFSEL0;
static volatile uint32_t *GPIO_PUP_REG0;
static volatile uint32_t *GPLEV0;
int lev;

struct Node{
	int a;
	int b;
	int c;
	int d;
}t;
//int sum;

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
    //*GPSET0 = (1<<18);
    gpio_set_value(18,1);
}
static void ledoff(void){
    printk(KERN_INFO "LED OFF\n");
    //*GPCLR0 = (1<<18);
    gpio_set_value(18,0);
}

int lev;
int ret;

static long nobrand_ioctl(struct file *filp, unsigned int cmd, unsigned long arg){
    switch(cmd){
	case _IO(0,3):
	    ledon();
	    break;
	case _IO(0,4):
	    ledoff();
	    break;
	case _IO(0,5):
	    lev = gpio_get_value(2);
	    printk(KERN_INFO "btn = %d\n", lev);
	    ret = copy_to_user((void*)arg, &lev, sizeof(int));
	    break;
/*
	case _IO(0,6):
	    ret = copy_to_user((void*)arg, &sum, sizeof(sum));
	    printk(KERN_INFO "sum complete\n");
	    break;
	case _IO(0,7):
	    lev = (*GPLEV0 >> 2 ) &1;
	    printk(KERN_ALERT "BTN read : %d\n", lev);
	    ret = copy_to_user((void*)arg, &lev, sizeof(int));
	    break;
*/
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

    printk(KERN_INFO "hi\n");
    /*
    BASE = (uint32_t*)ioremap(0xFE200000, 256);
    GPFSEL1 = BASE + (0x04/4);
    GPSET0 = BASE + (0x1C/4);
    GPCLR0 = BASE + (0x28/4);

    GPFSEL0 = BASE + (0x00/4);
    *GPFSEL0 &= ~(0x7 << 6);
	
    GPIO_PUP_REG0 = BASE + (0xE4/4);
    *GPIO_PUP_REG0 &= ~(0x3<<4);
    *GPIO_PUP_REG0 |= (1<<4);

    GPLEV0 = BASE + (0x34 / 4);
    *GPFSEL1 &= ~(0x7 << 24);
    *GPFSEL1 |= (1<<24);
    */
    gpio_request(18, "LED");
    gpio_direction_output(18,0);

    gpio_request(2,"BTN");
    gpio_direction_input(2);

  
    return 0;
}

static void nobrand_exit(void)
{
    //*GPCLR0 = (1<<18);
    //iounmap(BASE);
    gpio_free(18);
    gpio_free(2);
    unregister_chrdev(NOD_MAJOR, NOD_NAME);
    printk(KERN_INFO "bye\n");
}

module_init(nobrand_init);
module_exit(nobrand_exit);

