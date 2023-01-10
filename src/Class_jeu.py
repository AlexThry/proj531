import os

class Jeu:
	def __init__(self):
		self.is_connected = False
		self.is_admin = False
		self.user = None

	def get_admin_key(self):
		path = os.path.join('assets', 'Admin_Key.txt')
		with open(path, "r") as f:
			res = f.read()
			f.close()
		return res

	def set_admin_key(self):
		path = os.path.join("assets", "Admin_Key.txt")
		if self.is_admin:
			new_admin_key = input("Veuillez rentrer la nouvelle clé administrateur : \n")
			with open(path, "w") as f:
				f.write(new_admin_key)

	def get_is_admin(self):
		return self.is_admin

	def get_is_connected(self) -> bool:
		return self.is_connected
	
	def set_is_connected(self, bool) -> None:
		self.is_connected = bool

	def connexion(self, database):
		bon_mdp = False
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		users = database.execute(f"SELECT nom, mdp, isAdmin FROM Utilisateur WHERE nom = '{login}'").fetchall()
		user = users[0]
		bon_mdp = user[1] == mdp
		if bon_mdp:
			self.is_connected = True
			self.user = login
			if user[2]:
				self.is_admin = True
	
	def deconnexion(self):
		self.is_connected = False
		self.user = None
		self.is_admin = False

	def creer_compte(self, conn):
		database = conn.cursor()
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
			if admin_key == self.get_admin_key():
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
		print(database.execute(f"SELECT mdp FROM Utilisateur WHERE nom = '{self.user}'").fetchall()[0][0])
		if mdp == database.execute(f"SELECT mdp FROM Utilisateur WHERE nom = '{self.user}'").fetchall()[0][0]:
			database.execute(f"DELETE FROM Utilisateur WHERE nom = '{self.user}'")
			conn.commit()
			print("Vous avez supprimé votre compte")
			self.deconnexion()
		else:
			print("Vous n'avez pas donné le bon mot de passe")

	def recuperer_sauvegarde(self):
		pass
