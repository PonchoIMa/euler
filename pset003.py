# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
from math import sqrt
import argparse, logging

def factor(n: int) -> int:
    # finiding the limit for odd numbers
    limit_loop = int(sqrt(n) + 1)
    logging.debug(f'Limit to check is {limit_loop}')

    # test for evens (who does this? Man!)
    while(1):
        if((n % 2) == 0):
            if(n == 2):
                return 2 # bruh!
            else: 
                logging.debug(f"Found factor of 2! Remaining n: {n}")
                n = n // 2 
                continue
        else:
            break

    current_factor = 3 

    # test for odd numbers then
    while(current_factor <= limit_loop):
        # logging.debug(f'Testing with factor: {current_factor}...')
        if((n % current_factor) == 0):
            if((n // current_factor) == 1):
                logging.debug(f"Found largest prime: {current_factor}. Returning to main.")
                return current_factor
            else:
                n = n // current_factor
                logging.debug(f"Found factor: {current_factor}. Remaining n: {n}")
                continue
        else:
            current_factor += 2
            continue
    logging.debug(f'Loop escaped with factor: {current_factor}. Returning {n} to main')
    return n

def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default
    print(factor(n))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset003.py',
            description = 'finds the largest prime factor of any given number n (default = 600,851,475,143)', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 600851475143,
                        help = 'number to factorize')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)
