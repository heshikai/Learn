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
#include <pthread.h>

#define MAX  100

int number = 0;
pthread_mutex_t mutex;
pthread_mutex_t mutex2;
void * funcA_num(void * arg){
    int i;
    sleep(1);
    for(i = 0 ; i < MAX; i++){
        while(1){
            int a,b;
            b = pthread_mutex_trylock(&mutex2);
            usleep(100);
            a = pthread_mutex_trylock(&mutex);
            if(a == 0 && b == 0)break;
            if(a == 0 && b != 0)pthread_mutex_unlock(&mutex);
            if(b == 0 && a != 0)pthread_mutex_unlock(&mutex2);
        }
            int cur = number;
            cur++;
            usleep(100);
            number = cur;
        pthread_mutex_unlock(&mutex);
        pthread_mutex_unlock(&mutex2);
        printf("thread a ,number is %d\n",number);
    }
}

void * funcB_num(void * arg){
    int i;
    for(i = 0 ; i < MAX; i++){
        while(1){
            int a,b;
            b = pthread_mutex_trylock(&mutex2);
            usleep(100);
            a = pthread_mutex_trylock(&mutex);
            if(a == 0 && b == 0)break;
            if(a == 0 && b != 0)pthread_mutex_unlock(&mutex);
            if(b == 0 && a != 0)pthread_mutex_unlock(&mutex2);
        }
            int cur = number;
            cur++;
            usleep(100);
            number = cur;
        pthread_mutex_unlock(&mutex);
        pthread_mutex_unlock(&mutex2);
        printf("thread b ,number is %d\n",number);
    }
}

int main(){
    pthread_t a,b;
    pthread_mutex_init(&mutex,NULL);

    pthread_create(&a,NULL,funcA_num,NULL);
    pthread_create(&b,NULL,funcB_num,NULL);
    
    pthread_join(a,NULL);
    pthread_join(b,NULL);
    pthread_mutex_destroy(&mutex);
    
}