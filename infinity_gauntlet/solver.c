#include <stdio.h>
#include <stdlib.h>

#define FLAG_BUF_SIZ 2048
unsigned int flag_buf[2048];

FILE *input;
char *line;
size_t len;

unsigned int flag_sequencer[2048];
unsigned int flag[2048];

void compute_flag() {
    char counter = 0;
    for(unsigned int i = 0; i < 190; i++) {
        if(getline(&line, &len, input) == -1) {
            puts(line);
            puts("read too many from txt");
            exit(1);
            break;
        }

        // flag_buffer[b % flag_length_] // (lower 8 bits)
        char c = atoll(line);

        // v = ((b % flag_length_) + current_round) & 0xff // line >> 8 & 0xff bits
        unsigned int v = (atoll(line) >> 8);
        unsigned int b_m_flag_len = (v - (i + 50)) & 0xff;
        
        flag_sequencer[i] = b_m_flag_len;
        flag_buf[i] = c;
    }

    for(int i = 0; i < FLAG_BUF_SIZ; i++) {
        unsigned int index = flag_sequencer[i];
        flag[index] = flag_buf[i];
    }

    counter = 0;
    for(int i = 0; i < FLAG_BUF_SIZ; i++) {
        flag[i] = flag[i] ^ counter;
        counter += 0x11;
    }

    for(int i = 0; i < 26; i++) {
        printf("%c", flag[i]);
    } printf("\n");
}

int main(int argc, char **argv) {
    input = fopen("out.txt", "r");

    compute_flag();

    fclose(input);

    return 0;
}

/*
EAX = rand()
EDX = sign_extend(EAX)
RDX = sign_extend(EDX) 

EAX = EAX / FLAG_LENGTH
EAX = zero_extend(*RSP+RDX+16)

EBX = &mem[RDX + current_round]
EBX = zero_extend(*bl) // Lower 16 bits of EBX
EBX = EBX << 8

EBX = EBX | EAX


a = (b % flag_length_ + current_round & 0xff) << 8 | (uint)flag_buffer[b % flag_length_];
*/