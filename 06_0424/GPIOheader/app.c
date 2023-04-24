#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/ioctl.h>

struct Node{
	int a;
	int b;
	int c;
	int d;
}t;

int main()
{
    int fd = open("/dev/nobrand", O_RDWR);
    if (fd < 0)
    {
        printf("ERROR\n");
		exit(1);
    }
    while(1){
	int btn;
	ioctl(fd, _IO(0,5), &btn);
	printf("BTN : %d\n", btn);
	if( btn==0 ){
	    ioctl(fd, _IO(0,3), 0);
	}
	else{
	    ioctl(fd, _IO(0,4),0);
	}
    }	
    close(fd);
    return 0;
}

