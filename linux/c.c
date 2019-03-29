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

#define MAXLINE 100

int main(int argc,const char * argv[])
{
    int n=1;
    int fd[2];
    pid_t pid;
    char line[MAXLINE];
    int i = 0;
   
    if(pipe(fd) < 0){                 /* 先建立管道得到一对文件描述符 */
        exit(0);
    }

    if((pid = fork()) <  0)            //first fork
        exit(1);
    else if(pid > 0){  
        if((pid = fork())<0)exit(1);    //second fork
        else if(pid > 0){
            //do nothing
            sleep(1);
        }else{
            //second child
            close(fd[0]);
            dup2(fd[1],STDOUT_FILENO);
            execlp("ps","ps","aux",NULL);
        }
    }else{  
        //first child
        close(fd[1]);                /* 关闭写端 */
        dup2(fd[0],STDIN_FILENO);
        write(STDIN_FILENO,"5555\n\n\n",3);
        execlp("grep","grep","bash",NULL);
    }
        
    exit(0);
}
