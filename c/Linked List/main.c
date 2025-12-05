#include <stdio.h>
#include <stdlib.h>
#include "obj.h"

void print_menu() {
    printf("\n--- Linked List Menu ---\n");
    printf("1. Insert at Head\n");
    printf("2. Insert at Tail\n");
    printf("3. Delete a Node\n");
    printf("4. Print List\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

int main() {
    Node* head = NULL;
    int choice, value;

    while (1) {
        print_menu();
        
        // Read user input. If scanf fails (e.g. user enters text), clear buffer.
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input. Please enter a number.\n");
            while(getchar() != '\n'); // clear input buffer
            continue;
        }

        switch (choice) {
            case 1:
                printf("Enter integer to insert at head: ");
                scanf("%d", &value);
                insert_at_head(&head, value);
                printf("Inserted %d at head.\n", value);
                break;

            case 2:
                printf("Enter integer to insert at tail: ");
                scanf("%d", &value);
                insert_at_tail(&head, value);
                printf("Inserted %d at tail.\n", value);
                break;

            case 3:
                printf("Enter integer to delete: ");
                scanf("%d", &value);
                delete_node(&head, value);
                printf("Delete operation completed for value %d.\n", value);
                break;

            case 4:
                printf("Current List: ");
                print_list(head);
                break;

            case 5:
                printf("Cleaning up memory...\n");
                free_list(head);
                printf("Exiting program.\n");
                return 0;

            default:
                printf("Invalid choice (1-5). Try again.\n");
        }
    }

    return 0;
}
