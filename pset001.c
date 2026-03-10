#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

long gaussian_sum(long a, long limit){
    long target = limit - 1;
    long k = target / a;  
    return a * (k * (k + 1)) / 2;
}

int main(int argc, char *argv[]){
    long a = 3;
    long b = 5;
    long l = 1000;

    char *p2n;

    for(int i = 0; i < argc; i++){
        if(strcmp(argv[i], "-a") == 0){
            a = (long) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
        if(strcmp(argv[i], "-b") == 0){
            b = (long) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
        if(strcmp(argv[i], "-l") == 0){
            l = (long) strtol(argv[++i], &p2n, 10);
            
            if ((p2n == argv[i]) || (*p2n != '\0')) {
                printf ("'%s' is not valid. Make sure to input only integers!\n", argv[i]);
                return 1;
            }
        }
    }

    printf("%li\n", (gaussian_sum(a, l) + gaussian_sum(b, l) - gaussian_sum((a * b), l)));
    return 0;
}
