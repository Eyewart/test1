"""this little script allows to validate the format of an email address"""

import re

#anyletters@anyletters.com
email=input("Please enter the email address: ")

if re.search(r"^(([0-9A-Za-z])*)\@(([0-9A-Za-z]){1,})\.(([a-z]){1,3})$", email):
    print("This is a valid email")
else:
    print("This is not a correct address email")
