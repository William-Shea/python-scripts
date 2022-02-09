import dns.resolver
from termcolor import colored
import argparse
import sys
from googlesearch import search
from os.path import exists
import os
import random

## Parsing the different command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-d", required=True, help="Domain")
parser.add_argument("-w", required=True, help="Path to wordlist")
parser.add_argument("-o", type=str, help="Path to output file")
parser.add_argument("-files", action="store_true", help="Find potentially important files")
args = parser.parse_args()

## Opening the wordlist file
f = open(f'{args.w}', 'r')
ftest = f.read().splitlines()
ftest.append(f'\n')


## Files Finder Options
word = ['doc', 'docx']
powerpoint = ['ppt', 'pptx']
excel = ['csv', 'xlsx']
misc = ['xml', 'pdf']

## User Agents
user_agent_list = ['Mozilla/4.0 (compatible; ms-office; MSOffice 16)', 'WeatherReport/1.0.2 CFNetwork/485.13.9 Darwin/11.0.0', 'curl/7.54.0', 'Microsoft Office/16.0 (Windows NT 10.0; Microsoft Outlook 16.0.14228; Pro)', 'Microsoft Office PowerPoint 2014', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', 'Roku/DVP-9.10 (519.10E04111A)']

## Main function of testing each item in the wordlist with the supplied domain
def main():
    subdomain_store = []
    for subdoms in ftest:
        try:
            value_found = dns.resolver.resolve(f'{subdoms}.{args.d}', 'A')
            if value_found:
                if f'{args.d}' in subdomain_store:
                        if f'{subdoms}.{args.d}' in subdomain_store:
                            pass
                        else:
                            if (f'{args.o}') != 'None':
                                subdomain_store.append(f'{subdoms}.{args.d}')
                                filewrite = open(f'{args.o}', 'a')
                                filewrite.write(f'{subdoms}.{args.d}\n')
                                print(colored(f'[+] {subdoms}.{args.d} is Valid!', 'green'))
                                pass
                            else:
                                subdomain_store.append(f'{subdoms}.{args.d}')
                                print(colored(f'[+] {subdoms}.{args.d} is Valid!', 'green'))
                                pass
                else:
                    if f'{subdoms}.{args.d}' in subdomain_store:
                        pass
                    else:
                        if (f'{args.o}') != 'None':
                            subdomain_store.append(f'{args.d}')
                            subdomain_store.append(f'{subdoms}.{args.d}')
                            filewrite = open(f'{args.o}', 'a')
                            filewrite.write(f'{args.d}\n')
                            filewrite.write(f'{subdoms}.{args.d}\n')
                            print(colored(f'[+] {subdoms}.{args.d} is Valid!', 'green'))
                            pass
                        else:
                            subdomain_store.append(f'{subdoms}.{args.d}')
                            print(colored(f'[+] {subdoms}.{args.d} is Valid!', 'green'))
                            pass

        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass
        except KeyboardInterrupt:
            quit()
        except IndexError:
            quit()
    if args.files:
        try:
            print(colored("[+] Testing for Word Documents Now", 'yellow'))
            for wordfiles in word:
                try:
                    for sub_round2 in subdomain_store:
                        user_agent = random.choice(user_agent_list)
                        for w in search(f"site:{sub_round2} filetype:{wordfiles}", tld='com', num=10, start=0, stop=None, pause=10, user_agent=f'{user_agent}'):
                            file_exists = os.path.exists('.google-cookie')
                            if file_exists:
                                print(file_exists)
                                os.remove('.google-cookie')
                            print(colored(f'{w}', 'green'))
                except KeyboardInterrupt:
                    file_exists = exists('.google-cookie')
                    if file_exists:
                            os.remove('.google-cookie')
                    quit()
            print(colored("[+] Testing for PowerPoint Documents Now", 'yellow'))
            for ppfiles in powerpoint:
                try:
                    for sub_round2 in subdomain_store:
                        user_agent = random.choice(user_agent_list)
                        for p in search(f"site:{sub_round2} filetype:{ppfiles}", tld='com', num=10, start=0, stop=None, pause=10, user_agent=f'{user_agent}'):
                            file_exists = os.path.exists('.google-cookie')
                            if file_exists:
                                os.remove('.google-cookie')
                            print(f'{p}', 'green')
                except KeyboardInterrupt:
                    file_exists = exists('.google-cookie')
                    if file_exists:
                        os.remove('.google-cookie')
                    quit()
            print(colored("[+] Testing for Excel Documents Now", 'yellow'))
            for excelfiles in excel:
                try:
                    for sub_round2 in subdomain_store:
                        user_agent = random.choice(user_agent_list)
                        for e in search(f"site:{sub_round2} filetype:{excelfiles}", tld='com', num=10, start=0, stop=None, pause=10, user_agent=f'{user_agent}'):
                            file_exists = os.path.exists('.google-cookie')
                            if file_exists:
                                os.remove('.google-cookie')
                            print(f'{e}', 'green')
                except KeyboardInterrupt:
                    file_exists = exists('.google-cookie')
                    if file_exists:
                        os.remove('.google-cookie')
                    quit()
            print(colored("[+] Testing for Miscellaneous Documents Now", 'yellow'))
            for miscfiles in misc:
                try:
                    for sub_round2 in subdomain_store:
                        user_agent = random.choice(user_agent_list)
                        for m in search(f"site:{sub_round2} filetype:{miscfiles}", tld='com', num=10, start=0, stop=None, pause=10, user_agent=f'{user_agent}'):
                            file_exists = os.path.exists('.google-cookie')
                            if file_exists:
                                os.remove('.google-cookie')
                            print(f'{m}', 'green')            
                except KeyboardInterrupt:
                    file_exists = exists('.google-cookie')
                    if file_exists:
                        os.remove('.google-cookie')
                    quit()
        except KeyboardInterrupt:
            file_exists = exists('.google-cookie')
            if file_exists:
                os.remove('.google-cookie')
            quit()

main()

print(colored("\nAll done :) \n", 'blue'))
