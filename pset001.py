# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# EXTRA: Find a way to flag them (-a 3, -b 5) so that you can check both of them.
import argparse

def gaussian_sum(a: int, lim: int, verbose: bool = False) -> int:
    limit = lim - 1
    result = int(((limit // a) * (((limit // a) * a) + a))/2)
    if(verbose):
        print(f'Result of the Gaussian sum of {a} up to {lim} is {result}')
    return result

def main(a: int, b: int, lim: int, verbose: bool):
    if(verbose):
        print(f'Calculating the Gaussian sum between {a} and {b} up to {lim}')
    print(gaussian_sum(a, lim, verbose) +
          gaussian_sum(b, lim, verbose) - 
          gaussian_sum(a * b, lim, verbose))

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset001.py',
            description = 'finds the sum of all the multiples of X or Y below any Z limit',
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-a', type = int, default = 3,
                        help = 'first multiple X')
    parser.add_argument('-b', type = int, default = 5,
                        help = 'second multiple Y')
    parser.add_argument('-l', '--limit', type = int, default = 1000,
                        help = 'limit to which perform the sum')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.a, args.b, args.limit, args.verbose)
