# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# import pdb; pdb.set_trace()
import argparse

def fibonacci(a: int = 0, b: int = 1, limit: int = 4000000, n: int = 0, result: int = 0):
    # if the limit has been reached, return the sum
    if(b > limit):
        return result

    # if it is the n-th element, sum it up
    if(n == 2):
        # DEBUG - print(f'adding {b} to {result}!')
        result += b

    # recursion logic
    return fibonacci(b, a + b, limit, n + 1, result)

def better_fibonacci(a: int = 0, b: int = 1, limit: int = 4000000, n: int = 0, result: int = 0):
    result: int = 0
    while(b < limit):
        if(n == 2):
            # DEBUG - print(f'adding {b} to {result}!')
            n = -1 
            result += b 

        # ensuring next iteration
        a, b = b, a + b
        n += 1
    return result

def main(a: int, b: int, limit: int, verbose: bool):
    print(better_fibonacci(a, b, limit))
    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'pset002.py',
            description = 'finds the sum of the fibonacci series\' even numbers up to a given limit \'l\' (default = 4,000,000)', 
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-a', type = int, default = 0,
                        help = 'first number from the series')
    parser.add_argument('-b', type = int, default = 1,
                        help = 'second number from the series')
    parser.add_argument('-l', '--limit', type = int, default = 4000000,
                        help = 'limit to which perform the sum')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.a, args.b, args.limit, args.verbose)
