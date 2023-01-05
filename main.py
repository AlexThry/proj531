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
#     curs.execute("""
#     CREATE TABLE Historique (
#     idHisto int(11) NOT NULL,
#     score int(11) DEFAULT NULL,
#     mode int(11) DEFAULT NULL
#     )
#     """)
#     curs.execute("""
#     CREATE TABLE Question (
#     idQuestion int(11) NOT NULL,
#     question text DEFAULT NULL,
#     reponse1 text DEFAULT NULL,
#     reponse2 text DEFAULT NULL,
#     bonneReponse text DEFAULT NULL
#     ) ;
#     """)
#     curs.execute("""
#     CREATE TABLE quizz (
#     idQuizz int(11) NOT NULL,
#     nom varchar(50) DEFAULT NULL,
#     theme varchar(50) DEFAULT NULL
# ) ;
#     """)
#     curs.execute("""
#     CREATE TABLE Utilisateur (
#   idUtilisateur int(11) NOT NULL,
#   nom varchar(50) DEFAULT NULL,
#   mdp varchar(50) DEFAULT NULL,
#   isAdmin tinyint(1) DEFAULT NULL
# ) ;
#     """)

#     curs.execute("""
#     INSERT INTO Utilisateur (idUtilisateur, nom, mdp, isAdmin) VALUES
# (1, 'Alexis', '1234', 1),
# (2, 'Arthur', '1234', 1),
# (3, 'Andres', '1234', 1),
# (4, 'Carlyne', '1234', 1);
#     """)
#     curs.execute("""
#     ALTER TABLE Historique
#   ADD PRIMARY KEY (idHisto);
#     """)
#     curs.execute("""
#     ALTER TABLE Question
#   ADD PRIMARY KEY (idQuestion);
#     """)
#     curs.execute("""
#     ALTER TABLE quizz
#   ADD PRIMARY KEY (idQuizz);
#     """)
#     curs.execute("""
#     ALTER TABLE Utilisateur
#   ADD PRIMARY KEY (idUtilisateur);
#     """)
#     curs.execute("""
#     ALTER TABLE Historique
#   MODIFY idHisto int(11) NOT NULL AUTO_INCREMENT;
#     """)
#     curs.execute("""
#     ALTER TABLE Question
#   MODIFY idQuestion int(11) NOT NULL AUTO_INCREMENT;
#     """)
#     curs.execute("""
#     ALTER TABLE quizz
#   MODIFY idQuizz int(11) NOT NULL AUTO_INCREMENT;
#     """)
#     curs.execute("""
#     ALTER TABLE Utilisateur
#   MODIFY idUtilisateur int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
#     """)
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