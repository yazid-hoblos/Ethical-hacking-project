import sys
import re


def validate_url(x):
    if len(sys.argv)>1:
        if re.match(r"^((http|https):\/\/)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\.[a-z]{2,6}(\/([-a-zA-Z0-9@:%._\\+~#?&//=]*))*$",x):
            return x
        elif not re.match(r"http(s)?",x) and re.match(r"[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\.[a-z]{2,6}(\/([-a-zA-Z0-9@:%._\\+~#?&//=]*))*$",x):
            return "https://"+x
        else:
            print ("the entered url is not valid")
    else:
        print("no url is passed")
url = validate_url(sys.argv[1])





