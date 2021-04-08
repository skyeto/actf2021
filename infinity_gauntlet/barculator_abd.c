// CORRECT

#include <stdio.h>

int main(int argc, char **argv) {
    int a, b, c, d;
    puts("Enter bar(a, b, ?) = d");
    scanf("bar(%d, %d, ?) = %d", &a, &b, &d);

    //d = (c + 1) * b + a;

    c = ((d - a) / b) - 1;

    printf("Result %d\n", c);
}