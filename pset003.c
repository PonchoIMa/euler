#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
// note to self: apparently booleans do not come as "satandard"
// that's how arcaic this language is... cool!
#include <stdbool.h>

uint64_t factor(uint64_t n){
    // test for evens
    while(true){
        if(n % 2 == 0){
            if(n == 2){
                return 2;
            }
            else{
                n = n / 2;
                continue;
            }
        }
        else{
            break;
        }
    }

    // test for odd numbers
    for(uint64_t i = 3; i * i < n; i += 2){
        if(n % i == 0){
            // found a prime
            if(n / i == 1){
                // i is the largest prime factor
                return i;
            }
            else{
                // i is not the largest prime factor, but there's another swimming by
                n = n / i;
                continue;
            }
        }
    }
    // since i isn't the lpf, n must be (1) a prime and (2) the lpf, returning n
    return n;
}

// The prime factors of 13195 are 5, 7, 13 and 29.
// What is the largest prime factor of the number 600851475143?
int main(int argc, char *argv[]){
    uint64_t n = 600851475143;
    char *p2n;

    for(int i = 0; i < argc; i++){
        if(strcmp(argv[i], "-n") == 0){
            n = (uint64_t) strtol(argv[++i], &p2n, 10);
        }
    }

    printf("%li\n", factor(n));
    return 0;
}
