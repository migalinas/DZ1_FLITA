#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ELEMENTS 1000

struct Set {
    char* elements[MAX_ELEMENTS];
    int num_elements;
};

void init_set(struct Set* s) {
    s->num_elements = 0;
}

void print_set(struct Set* s) {
    printf("Set: { ");
    for (int i = 0; i < s->num_elements; i++) {
        printf("%s ", s->elements[i]);
    }
    printf("}\n");
}

void add_element(struct Set* s) {
    if (s->num_elements == MAX_ELEMENTS) {
        printf("Set is already full.\n");
        return;
    }
    char* element = malloc(1000 * sizeof(char));
    printf("Enter the element to be added: ");
    scanf("%s", element);
    for (int i = 0; i < s->num_elements; i++) {
        if (strcmp(element, s->elements[i]) == 0) {
            printf("Element %s is already in the set.\n", element);
            free(element);
            return;
        }
    }
    s->elements[s->num_elements] = element;
    s->num_elements++;
    printf("Element %s added to the set.\n", element);
}

void remove_element(struct Set* s) {
    char* element = malloc(100 * sizeof(char));
    printf("Enter the element to be removed: ");
    scanf("%s", element);
    for (int i = 0; i < s->num_elements; i++) {
        if (strcmp(element, s->elements[i]) == 0) {
            free(s->elements[i]);
            for (int j = i + 1; j < s->num_elements; j++) {
                s->elements[j - 1] = s->elements[j];
            }
            s->num_elements--;
            printf("Element %s removed from the set.\n", element);
            free(element);
            return;
        }
    }
    printf("Element %s not found in the set.\n", element);
    free(element);
}

int main() {
    struct Set s;
    struct Set s1;
    init_set(&s);
    init_set(&s1);
    int choice;
    while (1) {
        printf("Select an option:\n");
        printf("1. Print set\n");
        printf("2. Add element to set\n");
        printf("3. Remove element from set\n");
        printf("4. Print set1\n");
        printf("5 Add element to set1\n");
        printf("6. Remove element from set1\n");
        printf("7. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
        case 1:
            print_set(&s);
            break;
        case 2:
            add_element(&s);
            break;
        case 3:
            remove_element(&s);
            break;
        case 4:
            print_set(&s1);
            break;
        case 5:
            add_element(&s1);
            break;
        case 6:
            remove_element(&s1);
            break;
        case 7:
            exit(0);
        default:
            printf("Invalid choice!\n");
        }
    }
    return 0;
}
