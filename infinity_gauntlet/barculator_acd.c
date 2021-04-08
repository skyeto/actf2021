#include <stdio.h>

int main(int argc, char **argv) {
    int a, b, c, d;
    puts("Enter bar(a, ?, c) = d");
    scanf("bar(%d, ?, %d) = %d", &a, &c, &d);

    //d = (c + 1) * b + a;

    b = (d - a)/(c + 1);

    printf("Result %d\n", b);
}