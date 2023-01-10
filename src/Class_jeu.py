

class Jeu:
    def __init__(self):
        return None

    def connexion(self, database):
        login = input("Login : \n")
        mdp = input("Mot de passe : \n")
        list_user = database.execute("""SELECT * FROM Utilisateur""")
        bon_mdp = False
        for user in list_user:
            if user[1] == login:
                bon_mdp = user[2] == mdp

    def creer_compte(self, database):
        login = input("Login : \n")
        mdp = input("Mot de passe : \n")
        is_Admin = input("Compte administrateur ? o/n : \n")
        if is_Admin == "o":
            admin_key = input("Clé administrateur : \n")
            if admin_key == 1234:
                database.execute(
                    f"INSERT INTO Utilisateur (nom,mdp,isadmin) VALUES ({login}, {mdp}, True)")
            else:
                print("Vous ne pouvez pas être administrateur.")
        else:
            database.execute(
                f"INSERT INTO Utilisateur (nom,mdp,isadmin) VALUES ({login}, {mdp}, False)")

    def recuperer_sauvegarde(self):
        pass
