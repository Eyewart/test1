import socket
import time

hote = "localhost"
port = 12800

print("Fermeture de la connexion")

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.close()

connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

time.sleep(180)

connexion_avec_serveur.close()


