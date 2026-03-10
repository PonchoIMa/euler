#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

uint32_t fibonacci(uint32_t a, uint32_t b, uint32_t limit, int n){
    uint32_t result = 0;

    // loop to iterate the fibonacci
    while(b < limit){

        // add the even number to the chain
        if(n == 2){
            n = -1;
            result += b;
        }

        // move the list
        uint32_t next = a + b;
        a = b;
        b = next;
        n++;
    }
    return result;
}

int main(int argc, char *argv[]){
    uint32_t a = 0;
    uint32_t b = 1;
    uint32_t limit = 4000000;

    char *p2n;

    for(int i = 0; i < argc; i++){
        if(strcmp(argv[i], "-a") == 0){
            a = (uint32_t) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
        if(strcmp(argv[i], "-b") == 0){
            b = (uint32_t) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
        if(strcmp(argv[i], "-l") == 0){
            limit = (uint32_t) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
    }
    // n needs to remain as 0 in order to preserve the n+2 structure, though a more
    // sophisticated algorithm would be necessary to sum the pairs in such serieses.
    printf("%li\n", fibonacci(a, b, limit, 0));
    return 0;
}
