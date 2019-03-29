#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<pwd.h>
#include<grp.h>
#include<time.h>
#include<sys/time.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <signal.h>

int main(int argc,const char * argv[])
{
    sigset_t myset;
    sigemptyset(&myset);
    sigaddset(&myset,SIGINT);
    sigaddset(&myset,SIGQUIT);
    sigaddset(&myset,SIGKILL);

    sigprocmask(SIG_BLOCK,&myset,NULL);
    while(1){
        sigset_t pendset;
        sigpending(&pendset);
        int i;
        for(i = 1; i < 32 ;i++){
            if(sigismember(&pendset,i)){
                printf("1");
            }else{
                printf("0");
            }
        }
        printf("\n");
        sleep(1);
    }
    /*struct itimerval new_val;
    
    new_val.it_value.tv_sec = 2;
    new_val.it_value.tv_usec = 0;
    //new_val.it_value.tv_usec = 0;
    new_val.it_interval.tv_sec = 1;
    new_val.it_interval.tv_usec = 0;
    setitimer(ITIMER_REAL,&new_val,NULL);
    while(1){
        printf("hello,world\n");
        sleep(1);
    }*/
    exit(0);
}
