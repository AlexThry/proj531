

class Jeu:
	def __init__(self):
		self.is_connected = False

	def get_is_connected(self) -> bool:
		return self.is_connected
	
	def set_is_connected(self, bool) -> None:
		self.is_connected = bool

	def connexion(self, database):
		bon_mdp = False
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		users = database.execute(f"SELECT nom, mdp FROM Utilisateur WHERE nom = '{login}'").fetchall()
		user = users[0]
		bon_mdp = user[1] == mdp
		if bon_mdp:
			self.is_connected = True
			self.user = login
	
	def deconnexion(self):
		self.is_connected = False
		self.user = None

	def creer_compte(self, conn):
		database = conn.cursor()
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
			if admin_key == "1234":
				database.execute(
					f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "TRUE"))
				conn.commit()
			else:
				print("Vous ne pouvez pas être administrateur.")
		else:
			database.execute(
				f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "FALSE"))
			conn.commit()

	def supprimer_compte(self, conn):
		database = conn.cursor()
		mdp = input("Veuillez taper votre mot de passe : \n")
		if mdp == database.execute(f"SELECT mdp FROM Utilisateur WHERE login = '{self.user}'"):
			database.execute(f"DELETE FROM Utilisateur WHERE nom = '{self.user}'")
		else:
			print("Vous n'avez pas donné le bon mot de passe")

	def recuperer_sauvegarde(self):
		pass
