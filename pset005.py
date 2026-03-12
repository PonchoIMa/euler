# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible, divisible with no remainder by all of the numbers from to 20?
import argparse, logging

def least_common_multiple(candidate: int, n: int) -> int:
    # if a number is not even, return 0
    if(candidate % 2 != 0):
        return 0

    # check for all cases until n
    for i in range(3, n):
        if(candidate % i != 0):
            return 0

    # a last test, in case n % 2 == 0
    if(candidate % n != 0):
        return 0

    logging.debug(f'A new candidate has been found: {candidate}!')
    return 1

def factorial(n: int) -> int:
    if n != 1:
        return n * factorial(n - 1)
    return 1

def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    # finding the limit to search, which is n!
    current_find = factorial(n)
    logging.debug(f'Search limit has been set to {current_find}!')

    for candidate in range(n ** 2, current_find, 2):
        if(least_common_multiple(candidate, n)):
            logging.debug(f'Replacing {current_find} -> {candidate}!')
            current_find = candidate
            break

    # apparently, this is the one?
    logging.debug(f'Least common multiple is {current_find}!')
    print(current_find)
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset005.py',
            description = 'finds the smallest positive number that is evenly divisible, divisible with no remainder by all of the numbers from 1 to 20', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 10,
                        help = 'last divisor (default = 20)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)
