#ifndef OBJ_H
#define OBJ_H


#include <stdio.h>


typedef struct Node {
    int data;               
    struct Node* next;      
} Node;


Node* create_node(int data);

void insert_at_head(Node** head, int data);

void insert_at_tail(Node** head, int data);


void delete_node(Node** head, int key);


void print_list(Node* head);

void free_list(Node* head);

#endif 
