#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

int main()
{
    int fd = open("/dev/nobrand", O_RDWR);
    if (fd < 0)
    {
        printf("ERROR\n");
		exit(1);
    }
    //btn
    int lev;
    while(1){
        ioctl(fd, _IO(0,7), &lev);
        printf("tn Read lev : %d\n",lev);
        usleep(300*1000);
    }
    close(fd);
    return 0;

}

