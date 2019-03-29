#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<pwd.h>
#include<grp.h>
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include <sys/wait.h>
#include <fcntl.h>

#define MAXLINE 100

int main(int argc,const char * argv[])
{
    char buf[512];
   int fd = open("/tmp/myfifo",O_RDONLY);
    while(1){
        sleep(2);
        read(fd,buf,13);
        printf("%s",buf);
    }
    
    close(fd);
    exit(0);
}
