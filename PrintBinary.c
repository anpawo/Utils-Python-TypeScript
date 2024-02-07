/*
this function prints the bits of an integer
each byte is space separated
*/

#include <stdio.h>

void print_binary(int x)
{
    int shift = sizeof(x) * 8 - 1;

    do {
        printf("%d", ((x >> shift) & 1));
        if (shift % 8 == 0) { // space at each byte
            printf(" ");
        }
    } while (shift--);
    printf("\n");
}

int main(void)
{
    int x = 5;

    print_binary(x);
}
