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
	int number=5;
	int pid = 1;
	int i = 1;
	pid = fork();
	printf("i adddress is %p i is %d\n",&i,i);
	if(pid == 0)i+= 500;
	printf("i adddress is %p i is %d\n",&i,i);
	return 0;
}
