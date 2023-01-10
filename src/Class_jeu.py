import os
import random


class Jeu:
	def __init__(self):
		self.is_connected = False
		self.is_admin = False
		self.user = None


	def get_is_admin(self):
		return self.is_admin

	def get_is_connected(self) -> bool:
		return self.is_connected
	
	def set_is_connected(self, bool) -> None:
		self.is_connected = bool

	def connexion(self, curs, database):
		bon_mdp = False
		login = input("Login : \n")
		if curs.execute(f"SELECT * FROM Utilisateur WHERE nom = '{login}'").fetchall():
			mdp = input("Mot de passe : \n")
			users = curs.execute(f"SELECT nom, mdp, isAdmin FROM Utilisateur WHERE nom = '{login}'").fetchall()
			user = users[0]
			bon_mdp = user[1] == mdp
			if bon_mdp:
				self.is_connected = True
				self.user = login
				database.set_user(login)
				if user[2] == "TRUE":
					self.is_admin = True
			else:
				print("Mauvais mot de passe")
		else:
			print("Cet utilisatuer n'éxiste pas. Tapez 4 pour voir la liste des utilisateurs.")
	
	def deconnexion(self):
		self.is_connected = False
		self.user = None
		self.is_admin = False
