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
	curs.execute("CREATE TABLE IF NOT EXISTS Utilisateur (idUser INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR, mdp VARCHAR, isAdmin INTEGER(1))")
	curs.execute("CREATE TABLE IF NOT EXISTS Quizz (idQuizz INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR, theme VARCHAR)")
	curs.execute("CREATE TABLE IF NOT EXISTS Question (idQuestion INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, reponse1 TEXT, reponse2 TEXT bonne_reponse TEXT)")
	curs.execute("CREATE TABLE IF NOT EXISTS HISTORIQUE (idHisto INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER, mode INTEGER)")
	curs.execute("CREATE TABLE IF NOT EXISTS appartient (idQuizz INTEGER REFERENCES Quizz (idQuizz), idQuestion INTEGER REFERENCES Question (idQuestion), idQuizz PRIMARY KEY, idQuestion PRIMARY kEY)")
	print(curs.execute("SELECT *  FROM appartient").fetchall())

	########## Création du Jeu ##########

	# game = Jeu()

	# ########## MENU ##########

	# while True:
	# 	print(curs.execute("SELECT * FROM Utilisateur").fetchall())
	# 	print()
	# 	print("########## CONNEXION ########## \n")
	# 	print("1. Se Connecter")
	# 	print("2. Créer un compte")
	# 	print("3. Quitter \n")
	# 	rep = input("Faites votre choix \n")
	# 	if rep == "3":
	# 		curs.close()
	# 		break
	# 	elif rep == "2":
	# 		game.creer_compte(curs)
	# 	elif rep == "1":
	# 		game.connexion(curs)
	# 		if game.is_connected:
	# 			print("########## MENU ########## \n")
	# 			print("1. Jouer \n2. Historique \n")
	# 			rep = input("Faites votre choix \n")