import urllib.request
import pip._vendor.requests as requests
import sys
from urllib.error import ContentTooShortError, HTTPError, URLError
import re

from validate_url import *

url = validate_url(sys.argv[1])

def get_files(x):
    html = requests.get(x)
    content=html.text
    x=re.findall(r"(?:<a.*?href=\")(.*?)(?:\")",content)
    files= open('files_output.bat','w+')
    for line in x:
        files.write(line+"\n")
        if re.match(r".+.html",line) or re.match(r".+.php",line):
            if not re.match(r"https",line) and not re.match(r"http",line):
                line="https:"+line
            get_files(line)
    files.close()
    
get_files(url)      