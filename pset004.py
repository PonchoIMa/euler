# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 times 99
# Find the largest palindrome made from the product of two 3-digit numbers.
import argparse, logging

def palyndrome_check(product: int) -> bool:
    string_number = str(product) 
    if(string_number[-1] == '0'):
        return False
    if(string_number != string_number[::-1]):
        return False
    return True

def find_palyndrome_by(digits: int) -> int:
    last_palyndrome = 0

    limit = int('9' * digits) 
    lim_d = (limit + 1) // 10
    logging.debug(f'Setting limit to {limit}... Beginning looping')

    for i in range(limit, lim_d, -1):
        for j in range(i, lim_d, -1):
            if(i*j < last_palyndrome):
                break
            if(palyndrome_check(i * j)):
                logging.debug(f'Found candidate: {i * j}!')
                last_palyndrome = i * j
                break
    return last_palyndrome

def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    print(find_palyndrome_by(n))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset004.py',
            description = 'finds the largest palyndrome from the product of two n-digit numbers (default = 3)', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 3,
                        help = 'number of digits (eg. 3 = 999, 7 = 9,999,999)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)
