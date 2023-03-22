import urllib.request
import sys
from urllib.error import ContentTooShortError, HTTPError, URLError
import re

from validate_url import *

url = validate_url(sys.argv[1])

directories=list()

for line in open('dirs_dictionary.bat', 'r'):
    directories.append(line.strip('\n'))

found_directories=list()

dir= open('directories_output.bat','w+')

for x in directories:
    mutated_url="https://"+(re.split(r"(//)",url)[2])+"/"+x+"/"
    try:
        v=urllib.request.urlopen(mutated_url).getcode()
        if(v<400):
             found_directories.append(x)
             dir.write(x+"\n")
    except (URLError): #ContentTooShortError, ValueError, UnicodeError, HTTPError
        print(mutated_url, " is not accessible")
dir.close()