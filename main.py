import sqlite3 as sql
from src.Class_Jeu import *
from src.Class_Partie import *
from src.Class_Quizz import *
from src.Class_Sauvegarde import *
from src.Class_Utilisateur import *

if __name__ == "__main__":
    ########## Ouverture database #########
    conn = sql.connect("database.db")
    curs = conn.cursor()
    print(curs.execute("""SELECT * FROM UTILISATEUR""").fetchall())
    ########## Création du Jeu ##########

    game = Jeu()

    ########## MENU ##########

    while True:
        print()
        print("########## CONNEXION ########## \n")
        print("1. Se Connecter")
        print("2. Créer un compte")
        print("3. Quitter \n")
        rep = input("Faites votre choix \n")
        if rep == "3":
            break
        elif rep == "2":
            game.creer_compte(database)
        elif rep == "1":
            game.connexion(database)
            if game.is_connected:
                print("########## MENU ########## \n")
                print("1. Jouer \n2. Historique \n")

        database.close()