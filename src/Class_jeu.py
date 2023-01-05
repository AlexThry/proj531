class Jeu:
	def __init_(self):
		return None

	def connexion(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		list_user = database.execute("""SELECT * FROM Utilisateur""")
		bon_mdp = False
		for user in list_user:
			if user[1] == login:
				bon_mdp = user[2] == mdp
	
		if bon_mdp:
			self.is_connected = True
			print(self.is_connected)

		


	def creer_compte(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
