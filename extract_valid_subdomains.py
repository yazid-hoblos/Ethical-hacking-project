import urllib.request
import sys
from urllib.error import ContentTooShortError, HTTPError, URLError
import re

from validate_url import *

url = validate_url(sys.argv[1])

subdomains=list()

for line in open('subdomains_dictionary.bat', 'r'):
    subdomains.append(line.strip('\n'))

found_subdomains=list()

sub= open('subdomains_output.bat','w+')
for x in subdomains:
    mutated_url="https://"+x+"."+(re.split(r"(//)",url)[2])
    try:
        v=urllib.request.urlopen(mutated_url).getcode()
        if(v<400):
             found_subdomains.append(x)
             sub.write(x+"\n")
    except (URLError): #ContentTooShortError, ValueError, UnicodeError, HTTPError
        print(mutated_url, " is not accessible")
sub.close()


