# SubDomain Brute Force Tool
## Description
All you have to do is provide a domain and a wordlist containing subdomains you want to be tested.
## SETUP
```bash
Setup: pip install -r requirements.txt
```
## USAGE
Note:
When using this tool and you opt to use the files searcher, it can be prone to stop due to too many requests to google. I have lowered the speed to make sure that happens less, but feel free to change that to go faster. The faster/more results you want the more likely it is to stop.
```
sub-brute.py -h
usage: sub-brute.py [-h] -d DOMAIN -w WORDLIST

options:
  -h, --help  show this help message and exit     
  -d D        Domain
  -w W        Path to wordlist
  -o O        Path to output file
  -files      Find potentially important files
```
Below are the different types of usage
```bash
Basic Usage: sub-brute.py -d DOMAIN.COM -w subdomains.txt
```
```bash
Output Files: sub-brute.py -d DOMAIN.COM -w subdomains.txt -o output.txt
```
```bash
Search for Files: sub-brute.py -domain DOMAIN.COM -wordlist subdomains.txt -files
```
