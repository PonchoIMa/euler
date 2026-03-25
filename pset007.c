// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
// What is the 10,001st prime number?
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <stdbool.h>

#define DEBUG 0 // Set to 0 to turn off all debug logs

#define log_debug(fmt, ...) \
            do { if (DEBUG) fprintf(stderr, "[DEBUG] %s:%d:%s(): " fmt "\n", \
                                __FILE__, __LINE__, __func__, ##__VA_ARGS__); } while (0)

uint64_t nth_prime_approximation(int n){
    uint64_t logn = (uint64_t) log(n);
    uint64_t llgn = (uint64_t) log(logn);
    uint64_t rslt = (uint64_t) n * (logn + llgn + logn);

    log_debug("Approximation is %li", rslt);

    return rslt;
}

uint64_t nth_prime(int n){
    uint64_t primes[n];
    uint64_t approx     = nth_prime_approximation(n);
    uint64_t prime      = 1;
    bool     is_prime   = false;

    primes[0] = 2;

    for(uint64_t i = 3; i < approx; i += 2){
        is_prime = true; 
        for(int j = 0; primes[j] * primes[j] <= i; j++){
            if(i % primes[j] == 0){
                is_prime = false;
                break; // no need for more iteration here
            }
        }

        if(is_prime){
            // log_debug("Found prime %i: %li", prime + 1, i);
            primes[prime] = i;
            prime++;
            if(prime == n){
                return primes[prime - 1];
            }
        }
    }
    return 1;
}

int main(int argc, char *argv[]){
    int n = 10001;
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

    printf("%li\n", nth_prime(n));
    return 0;
}
