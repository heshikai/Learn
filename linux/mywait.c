#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<pwd.h>     // 所有者信息
#include<grp.h>     // 所属组信息
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include <sys/wait.h>

int main(){
	pid_t pid = fork();
	if(pid > 0){wait(NULL);printf("parent\n");}
	if(pid == 0){sleep(5);printf("child\n");}
	return 0;
}
 
