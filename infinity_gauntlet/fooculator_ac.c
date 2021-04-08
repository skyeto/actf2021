#include <stdio.h>

int main(int argc, char **argv) {
    unsigned int a, c;
    int b;
    puts("Enter foo(a, ?) = c");
    scanf("foo(%u, ?) = %u", &a, &c);

    b = ((c ^ 0x539) ^ a) - 0b1;

    printf("Result %d\n", b);
}

// foo(6974, ?) = 7260
// should be 602

// foo(61323, ?) = 59743
// should be 1004

// foo(37706, ?) = 37557
// 1221

// foo(, 214) = 8203
// 9701