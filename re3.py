import re

ipv4=input("Entrez une adresse IP:")

if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$",ipv4):
    print("This IP is correct!")
else:
    print("This IP isn't correct")