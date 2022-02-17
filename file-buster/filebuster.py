import argparse
from termcolor import colored
import requests
import sys



# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", required=True, help="Target", type=str)
parser.add_argument("-w", required=True, help="Wordlist", type=str)
parser.add_argument("-x", help="file extensions", type=str)
parser.add_argument("-o", help="File Output", type=str)
args = parser.parse_args()


# Opening wordlist into an array
f = open(f'{args.w}', 'r')
wordlist_contents = f.read().splitlines()

# file Extensions
if args.x != None:
	extensions = args.x.split(",")

def main():
	directory_store = []
	directory_store.append(f'{args.u}')
	try:
		for wordlist_entry in wordlist_contents:
			directory_check = requests.get(f'{args.u}/{wordlist_entry}')
			if directory_check:
				if directory_check.status_code == 200:
					if f'{args.u}/{wordlist_entry}' in directory_store:
						pass
					else:
						if args.o == None:
							directory_store.append(f'{args.u}/{wordlist_entry}')
							print(colored(f'[+] {args.u}/{wordlist_entry}', 'green'))
						else:
							directory_store.append(f'{args.u}/{wordlist_entry}\n')
							filewrite = open(f'{args.o}', 'a')
							filewrite.write(f'{args.u}/{wordlist_entry}\n')
							print(colored(f'[+] {args.u}/{wordlist_entry}', 'green'))
				else:
					pass
			else:
				pass
	except requests.exceptions.ConnectionError:
		print(colored('ERROR: python3 directory-brute.py -u http://site.com -w wordlist.txt', 'red'))
		quit()
	except KeyboardInterrupt:
		quit()
	if args.x != None:
		try:
			print(colored('[+] Testing Files now', 'yellow'))
			for extension in extensions:
				for directory in directory_store:
					file_test = requests.get(f'{directory}/{wordlist_entry}.{extension}')
					if file_test:
						if directory_check.status_code == 200:
							if f'{args.u}/{wordlist_entry}.{file_test}' in directory_store:
								pass
							else:
								if args.o == None:
									directory_store.append(f'{args.u}/{wordlist_entry}.{extension}')
									print(colored(f'[+] {directory}/{wordlist_entry}.{extension}', 'green'))
								else:
									directory_store.append(f'{args.u}/{wordlist_entry}.{extension}')
									filewrite = open(f'{args.o}', 'a')
									filewrite.write(f'{directory}/{wordlist_entry}.{extension}\n')
									print(colored(f'[+] {directory}/{wordlist_entry}.{extension}', 'green'))
						else:
							pass
		except requests.exceptions.ConnectionError:
			pass
		except KeyboardInterrupt:
			quit()


main()
print(colored('\nAll Done :)\n', 'blue'))