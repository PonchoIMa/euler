# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible, divisible with no remainder by all of the numbers from to 20?
import argparse, logging

def find_primes_up_to(n: int) -> list:
    logging.debug(f'Finding primes up to {n}!')
    primes = []
    
    if(n > 2):
        primes = [2]

        for candidate in range(3, n, 2):
            is_prime = 1 

            for prime in primes:
                if(candidate % prime == 0):
                    is_prime = 0
                    break

            if(is_prime):
                primes.append(candidate)

    logging.debug(f'Primes were: {primes}')
    return primes

def find_lcm(n: int) -> int:
    result = 1
    primes = find_primes_up_to(n)

    logging.debug(f'Beginning process to find the highest prime factor for the primes found')

    for prime in primes:
        highest_prime_factor = 1
        while(1):
            if(prime ** highest_prime_factor > n):
                logging.debug(f'Highest prime factor found {prime} ** {highest_prime_factor - 1} = {prime ** (highest_prime_factor - 1)}')
                result *= (prime ** (highest_prime_factor - 1))
                break
            highest_prime_factor += 1

    return result


def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    # finding the limit to search, which is n!
    logging.debug(f'Search limit has been set to {n}!')
    print(find_lcm(n))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset005.py',
            description = 'finds the smallest positive number that is evenly divisible, divisible with no remainder by all of the numbers from 1 to 20', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 20,
                        help = 'last divisor (default = 20)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)
