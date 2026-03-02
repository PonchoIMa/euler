#include <stdio.h>

long gaussian_sum(long a, long limit){
    long target = limit - 1;
    long k = target / a;  
    return a * (k * (k + 1)) / 2;
}

int main(void){
    printf("%li\n", (gaussian_sum(3, 1000) + gaussian_sum(5, 1000) - gaussian_sum(15, 1000)));
    return 0;
}
