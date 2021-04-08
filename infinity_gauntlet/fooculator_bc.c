#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    u_int32_t a, c;
    int32_t b;
    puts("Enter foo(?, b) = c");
    scanf("foo(?, %d) = %u", &b, &c);

    a =  b + 0b1 ^ c ^ 0x539;

    printf("Result %d\n", a);
}

// foo(?, 602) = 7260
// should be 6974

// foo(?, 1004) = 59743
// should be 61323