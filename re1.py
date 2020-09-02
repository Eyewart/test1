#script which verifies if a number is comprised of digits

import re

string = input("Please enter a number: ")

if re.search(r"^[0-9]+$", string):
    print("The string entered is a number")
else:
    print("The string entered is not a number...")
