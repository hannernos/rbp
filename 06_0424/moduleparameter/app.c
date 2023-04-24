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
	
	printf("LED ON!\n");
	ioctl(fd, _IO(0,3), 0);
	usleep(500*1000);

	printf("LED OFF\n");
	ioctl(fd, _IO(0,4), 0);

	close(fd);
    return 0;
}

