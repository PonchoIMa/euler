# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?
from os.path import isfile
from subprocess import CalledProcessError
import argparse, logging, subprocess

GREEN   = "\033[92m"
RED     = "\033[91m"
YELLOW  = "\033[93m"
BLUE    = "\033[96m"
END     = "\033[00m"

def normailze_filename(f: str) -> str:
    if(f[-3:] == '.py'):
        return f[:-3]
    elif('pset' in f):
        return f
    else:
        try:
            f = 'pset' + str(int(f) + 1000)[1:]
            return f
        except ValueError as e:
            logging.warning(RED + f'Error while handling filename {f}! Raising...' + END)
            raise ValueError(RED + f'ERROR: "{f}" is not a valid filename!' + END)
    return None 

def main(f: str, test: list, verbose: bool):
    if(verbose):
        logging.basicConfig(level=logging.DEBUG, format='%(message)s')
    else:
        logging.basicConfig(level=logging.WARNING) # Only show errors by default

    try:
        # Normalize file convention (3, 003, pset003, pset003.py) and check if they exist
        n_filename  = normailze_filename(f)
        py_file     = n_filename + ".py"
        c_file      = n_filename + ".c"
        
        logging.debug(BLUE + f'Trying to fetch files {py_file} and {c_file}' + END)
        if(not isfile(py_file) or not isfile(c_file)):
            raise FileNotFoundError(f'ERROR: Files {py_file} and/or {c_file} not found!') 
        else:
            logging.debug(BLUE + f'Files {py_file} and {c_file} found!' + END)

        # Compile file.c, continue if no errors
        logging.warning(YELLOW + f'Compiling {c_file}!' + END)
        out = subprocess.run(f'gcc -o {n_filename} {c_file}', shell = True, check = True, capture_output = True)
        # TODO: Analyze completed process

        # Run python script (python pset003.py [--flags})
        logging.warning(YELLOW + f'Executing {py_file}!' + END)
        py_out = subprocess.run(f'python {py_file}', shell = True, check = True, capture_output = True)
        py_out = py_out.stdout[:-1].decode('UTF-8')
        logging.debug(BLUE + f'Results are in! Python script returned: {py_out}!' + END)

        # Run C script (./file)
        logging.warning(YELLOW + f'Executing {c_file}!' + END)
        c_out = subprocess.run(f'./{n_filename}', shell = True, check = True, capture_output = True)
        c_out = c_out.stdout[:-1].decode('UTF-8')
        logging.debug(BLUE + f'Results are in! C script returned: {c_out}!' + END)

        # Compare results
        if(py_out == c_out):
            print(GREEN + f'Success! C successfully solved {n_filename} with an output of {c_out}' + END)
        else:
            print(RED + f'Failure! Python prompted {py_out} while C prompted {c_out}. Go fix your code!' + END)

    except ValueError as e:
        logging.error(RED + str(e) + END)
    except FileNotFoundError as e:
        logging.error(RED + str(e) + END)
    except CalledProcessError as e:
        logging.error(RED + str(e) + END)

    return 0

if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
            prog        = 'eulercheck.py',
            description = 'pytests psets in C against the results in previously written Python solutions.',
            usage       = 'python %(prog)s [--verbose] -f [file] [--test *]',
            epilog      = 'made with <3 by ponchoima')

    parser.add_argument('-f', type = str, required = True,
                        help = 'file or problem set to reach (if no extension is provided, it defaults to psetXYZ.py)')
    parser.add_argument('--test', nargs = '*', type = list, required = False,
                        help = 'custom input to test {may be inconsistent depending on cases)')
    parser.add_argument('-v', '--verbose', action = 'store_true',
                        help = 'outputs the steps it follows')
    args = parser.parse_args()

    main(args.f, args.test, args.verbose)
