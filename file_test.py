import os
import pickle

os.chdir("C:/test")
mon_fichier=open("file.txt","r")
content=mon_fichier.read()

print(mon_fichier)
print(content)
print(type(content))
print(type(mon_fichier))

score={"j1":5,"j2":9,"j3":2}

with open('donnees', 'wb') as fichier:
    my_pickler=pickle.Pickler(fichier)
    my_pickler.dump(score)

with open('donnees2','rb') as fichier2:
    my_unpickler=pickle.Unpickler(fichier2)
    score=my_unpickler.load()
    print(score)