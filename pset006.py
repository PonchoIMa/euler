# The sum of the squares of the first ten natural numbers is 1² + 2² + ... + 10² = 385.
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)² = 55² = 3025.
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import argparse, logging

def main(n: int, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    sum_of_squares = (n * (n + 1) * ((2 * n) + 1))/6
    square_of_sum  = ((n * (n + 1)) / 2) ** 2
    print(int(square_of_sum - sum_of_squares))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset006.py',
            description = 'finds the difference between the sum of the squares and the sqare of the sum of a given natural series starting from one (default = 100)', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-n', type = int, default = 100,
                        help = 'last divisor (default = 100)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.n, args.verbose)
