#include <stdio.h>
#include <stdlib.h>
#include "obj.h"
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (new_node == NULL) {
        fprintf(stderr, "Error: Memory allocation failed.\n");
        return NULL;
    }
    new_node->data = data;
    new_node->next = NULL;
    return new_node;
}
void insert_at_head(Node** head, int data) {
    Node* new_node = create_node(data);
    if (new_node == NULL) return;
    new_node->next = *head; 
    *head = new_node;       
}
void insert_at_tail(Node** head, int data) {
    Node* new_node = create_node(data);
    if (new_node == NULL) return;
    if (*head == NULL) {
        *head = new_node;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = new_node;
}
void delete_node(Node** head, int key) {
    if (*head == NULL) return;
    Node* temp = *head;
    Node* prev = NULL;
    if (temp != NULL && temp->data == key) {
        *head = temp->next; 
        free(temp);         
        return;
    }
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) return;
    prev->next = temp->next;
    free(temp);
}
void print_list(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        printf("%d -> ", temp->data);
        temp = temp->next;
    }
    printf("NULL\n");
}
void free_list(Node* head) {
    Node* temp = head;
    while (temp != NULL) {
        Node* next_node = temp->next; 
        free(temp);                   
        temp = next_node;             
    }
}
