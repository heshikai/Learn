#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<pwd.h>     // 所有者信息
#include<grp.h>     // 所属组信息
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<stdio.h>

int main(){
	pid_t pid;
	char * messages;
	int n;
	pid = fork();
	if(pid < 0 ){
		perror("fork failed");
		exit(1);
	}
	if(pid == 0){
		messages = "this is child\n";
		n = 6;
	}else {
		messages = "this is parent\n";
		n = 9;
	}
	printf("%d %d \n",getpid(),getppid());
	while(n--){
		printf(messages);
		sleep(1);
	}	
	return 0;
}
