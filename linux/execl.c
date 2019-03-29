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
for(int i = 0 ;i < 8;i++){
	printf("parent i is %d\n",i);
}

pid_t pid = fork();

if(pid == 0){
	sleep(5);
	printf("child exit!\n");
	//execl("/bin/ls","ls","666","-lah",NULL);
}
sleep(3);
for(int i = 0 ;i < 8;i++){
	printf("after execl parent i is %d\n",i);
}
return 0;
}
