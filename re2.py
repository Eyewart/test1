import re

plate = input ("License plate: ")
plate=plate.rstrip('\r\n')

if re.search(r"^[A-Z]{2}-[0-9]{3}-[A-Z]{2}$", plate):
    print("This please is correct")
else:
    print("This plate is not correct")