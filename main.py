import sqlite3 as sql
import src.Class_jeu
import src.Class_Partie
import src.Class_Quizz
import src.Class_sauvegarde
import src.Class_Utilisateur

if __name__ == "__main__":
  while True:
    ########## MENU ##########
    print()
    print("########## MENU ########## \n")
    print("1. Se Connecter")
    print("2. Créer un compte")
    print("3. Quitter \n")
    rep = input("Faites votre choix \n")
    if rep == "3":
      break
    elif rep == 1:
      pass
    elif rep == 2:
      pass


