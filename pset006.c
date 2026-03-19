// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible, divisible with no remainder by all of the numbers from to 20?
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <stdbool.h>

int main(int argc, char *argv[]){
    int n = 100;
    char *p2n;

    for(int i = 0; i < argc; i++){
        if(strcmp(argv[i], "-n") == 0){
            n = (int) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
    }

    uint64_t sum_of_squares = (uint64_t) (n * (n + 1) * ((2 * n) + 1))/6;
    uint64_t square_of_sum  = (uint64_t) ((n * (n + 1)) / 2) *((n * (n + 1)) / 2);

    printf("%li\n", (square_of_sum - sum_of_squares));
    return 0;
}
