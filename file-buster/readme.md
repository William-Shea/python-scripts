# File Buster
## Description
All you have to do is provide a domain and a wordlist containing directory and filenames you want to be tested.
## SETUP
```bash
Setup: pip install -r requirements.txt
```
## USAGE
```bash
python3 filebuster.py -h
usage: directory-brute.py [-h] -u URL -w WORDLIST

optional arguments:
  -h, --help  show this help message and exit
  -u U        Target
  -w W        Wordlist
  -x X        file extensions
  -o O        File Output
```
Below are the different types of usage
```bash
Basic Usage: filebuster.py -u http://site.com -w wordlist.txt
```
```bash
Output Files: filebuster.py -u http://site.com -w wordlist.txt -o output.txt
```
```bash
Search for Files: filebuster.py -u http://site.com -w wordlist.txt -x txt,html
```
