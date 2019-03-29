#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<pwd.h>
#include<grp.h>
#include<time.h>
#include <sys/time.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <sys/mman.h>

void myfunc(int no){
    
    time_t curtime;
    time(&curtime);
    char * curdatetime = ctime(&curtime);
    //printf("%s\n","ddddd");
    int fd = open("/root/time_temp.txt",O_CREAT |O_WRONLY| O_APPEND);
    write(fd,curdatetime,strlen(curdatetime)+1);
    close(fd);

}

int main(){
    pid_t pid = fork();
    if(pid > 0){
        exit(0);
    }else{
        
        setsid();
        chdir("/tmp");
        umask(0);
        close(STDIN_FILENO);
        //close(STDOUT_FILENO);
        close(STDERR_FILENO);

        

        struct sigaction act;
        act.sa_flags = 0;
        act.sa_handler = myfunc;
        sigemptyset(&act.sa_mask);
        sigaction(SIGALRM,&act,NULL);
        
        struct itimerval val;
        val.it_interval.tv_sec = 1;
        val.it_interval.tv_usec = 0;
        val.it_value.tv_sec = 2;
        val.it_value.tv_usec = 0;
 
        int a = setitimer(ITIMER_REAL,&val,NULL);
        while(1){
            ;
        }
    }
    return 0;
}