

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

<<<<<<< HEAD
	def creer_compte(self, database):
		login = input("Login : \n")
		mdp = input("Mot de passe : \n")
		is_Admin = input("Compte administrateur ? o/n : \n")
		if is_Admin == "o":
			admin_key = input("Clé administrateur : \n")
			if admin_key == "1234":
				database.execute(f"INSERT INTO VALUES (?,?,?,?)", (0, login, mdp, True))
			else:
				print("Vous ne pouvez pas être administrateur.")
		else:
			database.execute(f"INSERT INTO Utilisateur VALUES ({login}, {mdp}, false)")

	def recuperer_sauvegarde(self):
		pass
			database.execute(f"INSERT INTO Utilisateur VALUES (?,?,?,?)", (0, login, mdp, False))
=======
        if bon_mdp:
            self.is_connected = True

    def creer_compte(self, database):
        login = input("Login : \n")
        mdp = input("Mot de passe : \n")
        is_Admin = input("Compte administrateur ? o/n : \n")
        if is_Admin == "o":
            admin_key = input("Clé administrateur : \n")
            if admin_key == 1234:
                database.execute(
                    f"INSERT INTO Utilisateur VALUES ({login}, {mdp}, true)")
            else:
                print("Vous ne pouvez pas être administrateur.")
        else:
            database.execute(
                f"INSERT INTO Utilisateur VALUES ({login}, {mdp}, false)")

    def recuperer_sauvegarde(self):
        pass
>>>>>>> 7a47928ea4c71c8ebf5d78a40ffe345cda86e1f4
