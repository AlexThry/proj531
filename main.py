import sqlite3 as sql
from src.Class_Jeu import *
from src.Class_Partie import *
from src.Class_Quizz import *
from src.Class_Sauvegarde import *
from src.Class_Utilisateur import *
from src.Class_Menu import *
from src.Class_Database import *

if __name__ == "__main__":
	########## INITIALISATION #########
	conn = sql.connect("database.db")
	curs = conn.cursor()
	curs.execute("CREATE TABLE IF NOT EXISTS Utilisateur (idUtilisateur INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR, mdp VARCHAR, isAdmin INTEGER(1), idHisto INTEGER REFERENCES Historique (idHisto))")
	curs.execute(
		"CREATE TABLE IF NOT EXISTS Quizz (idQuizz INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR, theme VARCHAR)")
	curs.execute("CREATE TABLE IF NOT EXISTS Question (idQuestion INTEGER PRIMARY KEY AUTOINCREMENT, question TEXT, reponse1 TEXT, reponse2 TEXT, bonne_reponse TEXT)")
	curs.execute("CREATE TABLE IF NOT EXISTS Historique(idHisto INTEGER PRIMARY KEY AUTOINCREMENT, score INTEGER, mode INTEGER, idUtilisateur INTEGER REFERENCES Utilisateur (idUtilisateur))")
	curs.execute("CREATE TABLE IF NOT EXISTS appartient (idQuizz INTEGER REFERENCES Quizz (idQuizz), idQuestion INTEGER REFERENCES Question (idQuestion), PRIMARY KEY(idQuizz, idQuestion))")

	########## Création du Jeu ##########

	game = Jeu()
	menu = Menu()
	database = Database()

	########## MENU ##########

	menu.execute(game, conn, database)

	# q = Quizz()
	# quizz = q.melange_quizz(database.recuperer_quizz(database.choix_quizz(conn), conn))
	# print(quizz)
	# q.question_interface(quizz)

	