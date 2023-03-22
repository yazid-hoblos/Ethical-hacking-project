# Ethical-hacking-project

Steps/Components:

1. The url is first validated. Function validate_url(url) will make sure a url is passed in the command executing the python file, and will make sure the url is in a right format using regex. It will also add https:// in case no protocol is found at the beginning of the passed url.

2. The command python3 extract_valid_subdomains.py (url) could be used to extract the valid subdomains linked to the passed url. This python file will import the validate_url(url) function and will use the uploaded subdomains file to try all of them using the urllib.request.urlopen python function, so that only when the status_code returned is less < 400, the subdomain will be included in output_subdomains.bat storing all found subdomains.

3. Similarly, the command python3 extract_valid_directories (url) is used to extract all valid directories linked to the passed url.

4. The command python3 extract_valid_files (url) is used to extract all valid files linked to the passed url. Similarly, the url is first validated, then the html page of the passed url is read as string through requests.get(url).text, so that using regex all files in the href attributes within <a tags are read. Also in case the file is a php or html file, the function is runs again on it to extract all the files within it through recursion.

5. The command python3 brute_force_post_trials (url) is used to try all the passwords within the uploaded passwords.txt document on the url page. Similarly tp before, the url is validated first, then the user will be prompted for the username as well as the error to be expected for wrong passwords. All passwords will be tried through requests.post (a dictionary containing the username, password, and login is passed) and if the error is not found the password is printed as valid. It is important to note that some pages will not have the same 'username' and 'password' input names, which requires the inspection of their page and the extraction of the alternative names used for the username and password to be used in the dictionary of values to be passed. 

All the python file commands were tested on several websites for validation.

Challenges:

1. Using urllib.request.urlopen I was not able to read the html page as a string so I used requests.get instead only for the extract_valid_files.py file. For subdomains and directories extraction urllib.request.urlopen was used instead due to more convenience in catching the errors linked to not being able to access some url compared to using requests.get.

2. Finding websites to test my brute force code was particularly challenging as well.


