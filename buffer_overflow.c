
/*
 * BUFFER OVERFLOW SECURITY LAB
 * System Security | Memory Safety
 *
 * Educational laboratory.
 * Demonstrates safe buffer handling.
 *
 * Compile:
 * gcc -Wall -Wextra -O2 buffer_overflow.c -o buffer_lab
 */

#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 16

int main(void) {

    char buffer[BUFFER_SIZE];

    printf("=== BUFFER SECURITY LAB ===\n");

    printf(
        "Enter text (maximum %d characters): ",
        BUFFER_SIZE - 1
    );

    if (fgets(buffer, sizeof(buffer), stdin) == NULL) {

        fprintf(stderr, "Input error.\n");

        return 1;
    }

    buffer[strcspn(buffer, "\n")] = '\0';

    printf("\nStored input: %s\n", buffer);

    if (strlen(buffer) == BUFFER_SIZE - 1) {

        printf(
            "WARNING: Buffer capacity reached.\n"
        );

    } else {

        printf(
            "Input stored within buffer limits.\n"
        );

    }

    printf("\nSecurity check completed.\n");

    return 0;
}
