import os
import random
import sqlite3 as sql


class Database:
	def __init__(self) -> None:
		return None

	def set_user(self, user):
		self.user = user

	def creer_compte(self, conn, game):
		curs = conn.cursor()
		login = input("Login : \n")
		if not (curs.execute(f"SELECT nom FROM Utilisateur WHERE nom = '{login}'").fetchall()):
			mdp = input("Mot de passe : \n")
			is_Admin = input("Compte administrateur ? o/n : \n")
			if is_Admin == "o":
				admin_key = input("Clé administrateur : \n")
				if admin_key == game.get_admin_key():
					curs.execute(
						f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "TRUE"))
					conn.commit()
				else:
					print("Vous ne pouvez pas être administrateur.")
			else:
				curs.execute(
					f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "FALSE"))
				conn.commit()
		else:
			print("Cet utilisateur est déjà existant")

	def supprimer_compte(self, conn, game):
		curs = conn.cursor()
		mdp = input("Veuillez taper votre mot de passe : \n")
		print(curs.execute(
			f"SELECT mdp FROM Utilisateur WHERE nom = '{self.user}'").fetchall()[0][0])
		if mdp == curs.execute(f"SELECT mdp FROM Utilisateur WHERE nom = '{self.user}'").fetchall()[0][0]:
			curs.execute(f"DELETE FROM Utilisateur WHERE nom = '{self.user}'")
			conn.commit()
			print("Vous avez supprimé votre compte")
			game.deconnexion()
		else:
			print("Vous n'avez pas donné le bon mot de passe")

	def creer_question(self, conn):
		question = input("Rentrez votre question :\n")
		reponse = input("Rentrez la bonne réponse : \n")
		reponse2 = input("rentrez une mauvaise réponse : \n")
		values = [question, None, None, reponse]
		pos = random.randint(1, 2)
		if pos == 1:
			values[1] = reponse
			values[2] = reponse2
		else:
			values[1] = reponse2
			values[2] = reponse
		curs = conn.cursor()
		curs.execute(
			f"INSERT INTO Question(question, reponse1, reponse2, bonne_reponse) VALUES(?, ?, ?, ?)", tuple(values))
		conn.commit()

	def creer_quizz(self, conn):
		nom = input("Nom du quizz : \n")
		theme = input("Theme du quizz : \n")
		curs = conn.cursor()
		curs.execute(
			"INSERT INTO Quizz (nom, theme) VALUES (?, ?)", (nom, theme))
		conn.commit()

	def ajouter_questions_quizz(self, conn):
		curs = conn.cursor()
		ajouter = True

		list_quizz = curs.execute("SELECT * FROM Quizz").fetchall()
		for i in range(len(list_quizz)):
			print(f"{i+1}.{list_quizz[i][1]}")
		quizz = int(
			input("Choissiez le Quizz auquel ajouter des quetions ou 'q' pour quitter\n"))-1

		print(len(list_quizz))
		if quizz == "q":
			ajouter = False
		elif quizz not in range(len(list_quizz)):
			print("Vous n'avez pas choisis un quizz valide")
			ajouter = False
		list_question = curs.execute("SELECT * FROM Question").fetchall()

		while ajouter:
			for i in range(len(list_question)):
				print(f"{i+1}.{list_question[i][1]}")
			question = input(
				"Choississez la question à ajouter ou tapez 'q' pour quitter\n")
			if question == "q":
				ajouter = False
			elif int(question)-1 in range(len(list_question)):
				idQuizz = list_quizz[quizz][0]
				idQuestion = list_question[int(question)-1][0]
				curs.execute(
					"INSERT INTO appartient (idQuizz, idQuestion) VALUES (?, ?)", (idQuizz, idQuestion))
			else:
				print("Veuillez choisir une question valide")

		conn.commit()

	def afficher_questions(self, conn):
		curs = conn.cursor()
		questions = curs.execute("SELECT * FROM Question").fetchall()
		for item in questions:
			print(item[1])

	def afficher_quizzs(self, conn):
		curs = conn.cursor()
		quizzs = curs.execute("SELECT * FROM Quizz").fetchall()
		if len(quizzs) > 0:
			for i in range(len(quizzs)):
				print(f"{i+1}. {quizzs[i][1]}, theme : {quizzs[i][2]}")
			choix = input("choississez le quizz que vous souhaitez voir\n")
			if int(choix)-1 in range(len(quizzs)):
				idQuizz = quizzs[int(choix)-1][0]
				questions = curs.execute(
					f"SELECT question FROM appartient NATURAL JOIN Question WHERE idQuizz = {idQuizz}").fetchall()
				for item in questions:
					print(item[0])
			else:
				print("Ce n'est pas un choix correct")

	def choix_quizz(self, conn):
		"""Permet à l'utilisateur de choisir un quizz parmis les quizz existants

		Args:
				conn (conection):

		Returns:
				int: id du quizz choisis (bdd)
		"""
		curs = conn.cursor()
		quizzs = curs.execute("SELECT * FROM Quizz").fetchall()
		if len(quizzs) > 0:
			for i in range(len(quizzs)):
				print(f"{i+1}. {quizzs[i][1]}")
			choix = input("choississez le quizz auquel vous souhaitez jouer\n")
		if int(choix)-1 in range(len(quizzs)):
			idQuizz = quizzs[int(choix)-1][0]
			return idQuizz

	def recuperer_quizz(self, id_quizz, conn):
		curs = conn.cursor()
		quizz = curs.execute(
			f"SELECT * FROM appartient NATURAL JOIN Question WHERE idQuizz = {id_quizz}").fetchall()
		return quizz

	def recuperer_sauvegarde(self):
		pass

	def get_historique(self, login, conn):
		curs = conn.cursor()
		id_user = (curs.execute(
			f"SELECT idUtilisateur FROM Utilisateur WHERE nom = '{login}'").fetchall())[0][0]
		historique = (curs.execute(
			f"SELECT mode, score FROM Historique WHERE idUtilisateur = '{id_user}'").fetchall())
		for item in range(len(historique)):
			print(f"########## HISTORIQUE ##########\nNom du Zziuq : {historique[item][1]}\nScore du joueur : {historique[item][0]}")

	def add_history(self, login, quizz_name, score, conn):
		curs = conn.cursor()
		id_user = curs.execute(
			f"SELECT idUtilisateur FROM Utilisateur WHERE nom = '{login}'").fetchall()[0][0]
		curs.execute(
			"INSERT INTO Historique (idUtilisateur, score, mode) VALUES (?,?,?)", (id_user, quizz_name, score))
		conn.commit()


# if __name__ == '__main__':
#     Baba = Database()
#     user = str(input('un user please'))
#     Baba.get_historique(user, sql.connect("database.db"))
