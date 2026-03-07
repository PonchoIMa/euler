#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>

int palyndrome_check(uint64_t candidate){
    // safety checks to save computational power
    if(candidate % 10 == 0){
        return 0; // no multiples of 10 can be palyndromes. ever. period.
    }

    // change for modular operations (better to check by digit, i knew it beforehand!)
    uint64_t o_candidate = candidate;
    uint64_t r_candidate = 0;

    while(candidate > 0){
        // note to self: r_candidate += (r_candidate * 10) + (candidate % 10) doesn't work.
        r_candidate *= 10;
        r_candidate += (candidate % 10);
        candidate /= 10;
    }
    
    // DEBUG: printf("%li\n", r_candidate);
    if(r_candidate == o_candidate){
        return 1;
    }
    return 0;
}

uint64_t find_palyndrome_by(int n){
    uint64_t last_palyndrome = 0;

    uint64_t lim_d  = (uint64_t) pow((double) 10, (double) (n - 1));
    uint64_t limit  = (lim_d * 9);
    limit          += (lim_d - 1);
    printf("%i\n%li\n%li\n", n, limit, lim_d);

    for(uint64_t i = limit; i > lim_d; i--){
        for(uint64_t j = i; j > lim_d; j--){
            if(i * j > last_palyndrome){
                if(palyndrome_check((uint64_t) (i * j)) == 1){
                    last_palyndrome = (uint64_t) (i * j);
                    break;
                }
            }
        }
    }
    return last_palyndrome;
}

// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99
// Find the largest palindrome made from the product of two 3-digit numbers.
int main(int argc, char *argv[]){
    int n = 3;
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

    printf("%li\n", find_palyndrome_by(n));
    return 0;
}
