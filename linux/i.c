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
#include <semaphore.h>

sem_t sem_produce;
sem_t sem_consumer;

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

        sem_wait(&sem_produce);
        struct ListNode * new_production;
        new_production = (struct ListNode * )malloc(sizeof(struct ListNode));
        new_production->data = rand();
        new_production->next = head;
        head = new_production;
        printf("produced one !\n");
        sem_post(&sem_consumer);
        sleep(rand() % 3);
   }
    return NULL;
}
void * consumer(void * ptr){
    
    while(1){
        sem_wait(&sem_consumer);
        struct ListNode * pconsumehead = head;
        head = head->next;
        free(pconsumehead);
        printf("consume one !\n");
        sem_post(&sem_produce);
        sleep(rand() % 3);
    }
    return NULL;
}

int main(){
    pthread_t p1,p2;

    sem_init(&sem_produce,0,5);
    sem_init(&sem_consumer,0,0);
    pthread_create(&p1,NULL,produce,NULL);
    pthread_create(&p2,NULL,consumer,NULL);
    
    
    pthread_join(p1,NULL);
    pthread_join(p2,NULL);
    sem_destroy(&sem_produce);
    sem_destroy(&sem_consumer);

}