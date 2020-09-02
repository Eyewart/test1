import re

# Chaîne de caractères sur laquelle on va travailler
S = 'Bugger all down here on earth!'

print ("\nCas 1\n-----\n")

# Expression régulière visant à matcher le texte
patt = re.compile('Bugger all\s*(.*)here on (.*)!')

# Match
mobj = patt.match(S)

# Affichage du résultat dans le cas où un pattern correspond
if mobj:
    print (mobj.group(1))
    print (mobj.group(2))
else:
    print ("Not find")