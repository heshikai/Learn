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

pthread_mutex_t mutex;
pthread_cond_t cond;
struct ListNode * head = NULL;
struct ListNode {
    int data;
    struct ListNode * next;
};

void * produce(void * ptr){
    while(1){
        // create one node
        // insert the node
        //send unleash the condition signal

        pthread_mutex_lock(&mutex);
        struct ListNode * new_production;
        new_production = (struct ListNode * )malloc(sizeof(struct ListNode));
        new_production->data = rand();
        new_production->next = head;
        head = new_production;
        
        printf("produced one !\n");
        pthread_mutex_unlock(&mutex);
        pthread_cond_signal(&cond);
        sleep(rand() % 3);
   }
    return NULL;
}
void * consumer(void * ptr){
    
    while(1){
        pthread_mutex_lock(&mutex);
        if(head == NULL){
            pthread_cond_wait(&cond,&mutex);
        }
        
        struct ListNode * pconsumehead = head;
        head = head->next;
        free(pconsumehead);
        
        printf("consume one !\n");
        pthread_mutex_unlock(&mutex);
        sleep(rand() % 3);
    }
    return NULL;
}

int main(){
    pthread_t p1,p2;

    pthread_cond_init(&cond,NULL);
    pthread_mutex_init(&mutex,NULL);
    pthread_create(&p1,NULL,produce,NULL);
    pthread_create(&p2,NULL,consumer,NULL);
    
    
    pthread_join(p1,NULL);
    pthread_join(p2,NULL);
    pthread_cond_destroy(&cond);
    pthread_mutex_destroy(&mutex);

}