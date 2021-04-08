// CORRECT

#include <stdio.h>

int main(int argc, char **argv) {
    int a, b, c, d;
    puts("Enter bar(?, b, c) = d");
    scanf("bar(?, %d, %d) = %d", &b, &c, &d);

    //d = (c + 1) * b + a;

    a = d - (c + 1) * b;

    printf("Result %d\n", a);
}