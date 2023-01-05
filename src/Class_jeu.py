class Jeu:
	def __init_(self):
		return None

	def connexion(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		list_user = database.execute("""SELECT * FROM Utilisateur""")
		for user in list_user:
			if user[1] == login:
				bon_mdp = user[2] == mdp
		if bon_mdp:
			self.is_connected = True

		


	def creer_compte(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
