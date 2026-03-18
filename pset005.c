#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <stdbool.h>

int is_prime(int n){
    // addressing for even numbers
    if(n % 2 == 0){
        if(n == 2){
            return true;
        }
        return false;
    }

    // addresing odd numbers
    for(int i = 3; i < n; i += 2){
        if(n % i == 0){
            return false;
        }
    }
    
    // no mod 0 found, n is prime!
    return true;
}

uint64_t find_lcm(int n){
    uint64_t result = 1;

    // main loop to add primes 
    for(int i = 2; i <= n; i++){
        if(is_prime(i)){
            double exp = 1;
            while(true){
                if(pow((double) i, exp) > (double) n){
                    result *= pow((double) i, exp - 1);
                    break;
                }
                exp++;
            }
        }
    }

    return result;
}

int main(int argc, char *argv[]){
    int n = 10;
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

    printf("%li\n", find_lcm(n));
    return 0;
}
