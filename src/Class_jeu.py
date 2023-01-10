

class Jeu:
	def __init__(self):
		return None
		self.is_connected = False

	def get_is_connected(self) -> bool:
		return self.is_connected
	
	def set_is_connected(self, bool) -> None:
		self.is_connected = bool

	def connexion(self, database):
		bon_mdp = False
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		try:
			user = database.execute(f"SELECT {login} FROM Utilisateur").fetchall()
			bon_mdp = user[2] == mdp
			if bon_mdp:
				self.is_connected = True
				self.user = login
		except:
			print("Veuillez choisir un nom d'utilisateur correct")

	def creer_compte(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
			if admin_key == "1234":
				database.execute(
					f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "TRUE"))
			else:
				print("Vous ne pouvez pas être administrateur.")
		else:
			database.execute(
				f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "FALSE"))
	

	def recuperer_sauvegarde(self):
		pass
