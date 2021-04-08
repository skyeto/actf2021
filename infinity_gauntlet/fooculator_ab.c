// CORRECT

#include <stdio.h>

int main(int argc, char **argv) {
    unsigned int a, c;
    int b;
    puts("Enter foo(a, b) = ?");
    scanf("foo(%u, %d) = ?", &a, &b);

    c = b + 0b1 ^ a ^ 0x539;
    printf("Result %u\n", c);
}