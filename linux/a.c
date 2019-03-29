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
    int fd = open("/tmp/myfifo",O_WRONLY);
    while(1){
        sleep(5);
        write(fd,"hello,world\n",12);
        printf("hello,world,a.c!\n");
    }
    
    close(fd);
    exit(0);
}
