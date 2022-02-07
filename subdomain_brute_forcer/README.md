# This is a SubDomain Brute Force Tool
## Description
All you have to do is provide a domain and a wordlist containing subdomains you want to be tested.
## SETUP
```bash
Setup: pip install -r requirements.txt
```
## USAGE
```
sub-brute.py -h
usage: sub-brute.py [-h] -domain DOMAIN -wordlist WORDLIST [-outfile OUTFILE]

options:
  -h, --help          show this help message and exit
  -domain DOMAIN      Domain
  -wordlist WORDLIST  Path to wordlist
  -outfile OUTFILE    Path to output file
```
```bash
Basic Usage: sub-brute.py -domain DOMAIN.COM -wordlist subdomains.txt
```
