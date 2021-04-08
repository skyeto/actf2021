// CORRECT

#include <stdio.h>

int main(int argc, char **argv) {
    int a, b, c, d;
    puts("Enter bar(a, b, c) = ?");
    scanf("bar(%d, %d, %d) = ?", &a, &b, &c);

    d = (c + 1) * b + a;

    printf("Result %d\n", d);
}