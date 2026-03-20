# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?
import argparse, logging, math

def nth_prime(n: int) -> int:
    approx = int(n * (math.log(n, math.e) + math.log(math.log(n, math.e), math.e)))
    return approx 

def nth_prime_improved(n: int) -> int:
    found_primes   = [2, 3, 5, 7, 11, 13]
    next_candidate = 17
    
    while(len(found_primes) < n):
        is_prime = True

        for prime in found_primes[:len(found_primes)//2]:
            if(next_candidate % prime == 0):
                is_prime = False
                break

        if(is_prime):
            found_primes.append(next_candidate)
        next_candidate += 2

    # safeguard for not throwing a different integer
    if(found_primes[-1] > nth_prime(n)):
        raise LookupError("Logarithmic approach didn't work, please refactor formula!")
    return found_primes[-1]

def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    print(nth_prime_improved(n))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset007.py',
            description = 'finds the nth prime (default = 10001)', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 10001,
                        help = 'nth prime to find (default = 10001)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)

