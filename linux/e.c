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
#include <sys/mman.h>

#define MAXLINE 100
unsigned long long i = 0;
void myfunc(int no){
    printf("i is %uld\n",i);
    printf("catch you signal:%d\n",no);
    sleep(10);
}
int main(int argc,const char * argv[])
{
    struct sigaction act;
    act.sa_flags = 0;
    sigemptyset(&act.sa_mask);
    sigaddset(&act.sa_mask,SIGQUIT);
    act.sa_handler = myfunc; 
    sigaction(SIGINT,&act,NULL);
    while(1){i++;}
    exit(0);
}
