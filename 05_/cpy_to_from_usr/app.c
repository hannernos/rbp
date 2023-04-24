#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/ioctl.h>

char buf[30];
int main(){
	int fd = open("/dev/nobrand", O_RDWR);
	if ( fd<0 ){
		printf("ERROR\n");
		exit(1);
	}

	int cmd;
	while(1){
		printf("SSAFY>>");
		scanf("%d", &cmd);
		if( cmd == 3 ){
			printf("input msg : ");
			scanf("%s", buf);
			ioctl(fd, _IO(0,cmd),buf);
		}
		else if( cmd==4){ 
			ioctl(fd, _IO(0,cmd),buf);
			printf("%s\n", buf);
		}
		else {
			int ret = ioctl(fd, _IO(0,cmd), buf);
			if( ret<0 ){
				printf("command error\n");
				break;
			}
		}
	}
	close(fd);
	return 0;
}

