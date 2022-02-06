import dns.resolver
from colorama import Fore, Style, init
from termcolor import colored
import sys

domain = sys.argv[1]
file = sys.argv[2]
f = open(f'{file}', 'r')
ftest = f.read().splitlines()

def main():
    subdomain_store = []
    for subdoms in ftest:
        try:
            ip_value = dns.resolver.resolve(f'{subdoms}.{domain}', 'A')
            if ip_value:
                if f'{subdoms}.{domain}' in subdomain_store:
                    printcolored((f'[+]{subdoms}.{domain} is Valid!', 'green'))
                else:
                    subdomain_store.append(f'{subdoms}.{domain}')
                    print(colored(f'[+]{subdoms}.{domain} is Valid!', 'green'))
                    pass
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()
        except IndexError:
            print(colored('Syntax: python sub-brute.py <DOMAIN> <WORDLIST>', 'green'))
            quit()



main()