import dns.resolver
from termcolor import colored
import argparse
import sys

## Parsing the different command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-domain", type=str, required=True, help="Domain")
parser.add_argument("-wordlist", type=str, required=True, help="Path to wordlist")
parser.add_argument("-outfile", type=str, help="Path to output file")
args = parser.parse_args()

## Opening the wordlist file
f = open(f'{args.wordlist}', 'r')
ftest = f.read().splitlines()


## Main function of testing each item in the wordlist with the supplied domain
def main():
    subdomain_store = []
    for subdoms in ftest:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{args.domain}', 'A')
            if ip_value:
                    if f'{subdoms}.{args.domain}' in subdomain_store:
                        pass
                    else:
                        if (f'{args.outfile}') != 'None':
                            subdomain_store.append(f'{subdoms}.{args.domain}')
                            filewrite = open(f'{args.outfile}', 'a')
                            filewrite.write(f'{subdoms}.{args.domain}\n')
                            print(colored(f'[+]{subdoms}.{args.domain} is Valid!', 'green'))
                            pass
                        else:
                            subdomain_store.append(f'{subdoms}.{args.domain}')
                            print(colored(f'[+]{subdoms}.{args.domain} is Valid!', 'green'))
                            pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()
        except IndexError:
            quit()



main()