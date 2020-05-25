import sqlite3
import Roulette
import os
from datetime import datetime

#ici on gere la connexion a la base de donnée local

connection = sqlite3.connect("jeux.db")
cursor = connection.cursor()


class joueur():
    id_joueur = int()
    pseudo = str()
    portefeuille = int()
    age = int()
    mdp = str()

def nouveau_joueur():
    age = int(input("quel est ton ages ? :"))
    pseudo = input("quel est ton pseudo ? :")
    mdp = input("quel est ton mot de passe?")
    new_user = (cursor.lastrowid,pseudo,age,1000,mdp)
    cursor.execute('INSERT INTO utilisateurs VALUES(?,?,?,?,?)',new_user)
    connection.commit()
    print("utilisateurs ajouter avec succes")
    print("En tant que nouvelle utilisateur tu as recu 150 € ")

# on créer la variable pour sotcker son nom

joueurSession = joueur


def menu():
 menu = ("Connexion", "Inscription","Banque", "quittez")

 count = 0
 #On affiche le menu
 for i in menu:
    count += 1
    print(f"{count}){i}")

 choix = input(":")

 #par rapport au choix on choisie la fonction
 if choix == "1" :
     if connexion():
         os.system('clear')
         print(f"Bonjour {joueurSession.pseudo}")
         print(f"Montant de votre porte-feuille: {joueurSession.portefeuille} €")
         play()
 elif choix == "2":
    nouveau_joueur()
 elif choix == "3":
    if connexion():
     print(f"Montant du porteFeuille: {joueurSession.portefeuille} €")
     banque()
 else :print("on quite !") 
 exit   

def solvabiliteJoueur(totalMiser:int(),portefeuille:int()):
    if portefeuille >= totalMiser :
        return True
    else: return False 

def recupeInfoJoueur(pseudo:str()):

 reqSession = cursor.execute(f'SELECT * FROM utilisateurs WHERE pseudo="{pseudo}"')
 reponseSession = reqSession.fetchone()
 joueurSession.id_joueur = reponseSession[0]
 joueurSession.pseudo = reponseSession[1]
 joueurSession.age = reponseSession[2]
 joueurSession.portefeuille = reponseSession[3]
 joueurSession.mdp = reponseSession[4]

def miseAjoursPorteFeuille(id:int(),montant:int()):

    cursor.execute(f'UPDATE utilisateurs SET portefeuille={montant} WHERE id={id} ')
    connection.commit()
    print("portefeuille Mis a jour")

def banque():
    print("quel montant souhaitez vous crediter ? :")
    montant = int(input(":"))
    montant += joueurSession.portefeuille
    miseAjoursPorteFeuille(joueurSession.id_joueur, montant)

def connexion():
    os.system('clear')
    login = input("login:")
    mdp = input("mdp:")
    rep1 = cursor.execute(f'SELECT * FROM utilisateurs WHERE pseudo="{login}"')
    reponse = rep1.fetchall()
    password = reponse[0]
    if mdp == str(password[4]):
        recupeInfoJoueur(login)
        return True
    else:
        return False

def replay():
 print("Souhaitez vous rejouer ? o/n")
 choix = input(":")
 if choix == "o" or choix == "O":
     play()

def play() :
 roulette = Roulette.jeuxRoulette
 Roulette.LancerRoulette(roulette)
 os.system('clear')
 nombre = Roulette.gameNumero()
 os.system('clear')
 couleur = Roulette.gameCouleur()
 os.system('clear')
 tierTier = Roulette.gameTier()
 os.system('clear')
 demi = Roulette.gameDemi()
 os.system('clear')
 
 totalMise = Roulette.totalMiser(nombre) + Roulette.totalMiser(couleur) + Roulette.totalMiser(tierTier) + Roulette.totalMiser(demi)

 if solvabiliteJoueur(totalMise,joueurSession.portefeuille) :
     gain = Roulette.comparaisonDesGains(roulette,nombre,couleur,tierTier,demi)
     dif = gain - totalMise

     print(f"Total de votre mise :{totalMise} € ")
     print(f"Total de vos gains :{gain} €")
     print("")
     connection.commit()
     now = datetime.now()
     dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
     requetteAddResultat = (roulette.nombre,roulette.couleur,roulette.tier,roulette.moitier,joueurSession.pseudo,dt_string)
     cursor.execute('INSERT INTO lancer VALUES(?,?,?,?,?,?)',requetteAddResultat)
     connection.commit()

     # on Re value la valeur du porte feuille
     NouveauMontant = joueurSession.portefeuille + dif
     # on met la valeur a jour
     miseAjoursPorteFeuille(joueurSession.id_joueur,NouveauMontant)
     connection.commit()

     if dif != 0:
         if dif > 0:
          print(f"Vous avez gagner {dif} € ")
          print(f"Votre nouveau solde est de {NouveauMontant} € ")
          replay()
         else:
             print(f"Vous avez perdu {dif} € ")
             print(f"Votre nouveau solde est de {NouveauMontant} € ")
             replay()
     else:
         print("Vous n'avez rien perdu (mais rien gagner non plus :p)")
 else: print("vous n'avez pas assez de fond ! ")
 

# c'est ici que le programme commenceras a lire

os.system('clear')

menu()


# on coupe la connexion a la base de donnée a la fin du programme
connection.close()
