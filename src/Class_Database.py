import os
import random


class Database:
    def __init__(self) -> None:
        return None

    def set_user(self, user):
        self.user = user

    def get_admin_key(self):
        path = os.path.join('assets', 'Admin_Key.txt')
        with open(path, "r") as f:
            res = f.read()
            f.close()
        return res

    def set_admin_key(self):
        path = os.path.join("assets", "Admin_Key.txt")
        if self.is_admin:
            new_admin_key = input(
                "Veuillez rentrer la nouvelle clé administrateur : \n")
            with open(path, "w") as f:
                f.write(new_admin_key)
                print(
                    f"La clé administrateur est désormais : {self.get_admin_key()}")
                f.close()

    def creer_compte(self, conn):
        curs = conn.cursor()
        login = input("Login : \n")
        if not(curs.execute(f"SELECT nom FROM Utilisateur WHERE nom = '{login}'").fetchall()):
            mdp = input("Mot de passe : \n")
            is_Admin = input("Compte administrateur ? o/n : \n")
            if is_Admin == "o":
                admin_key = input("Clé administrateur : \n")
                if admin_key == self.get_admin_key():
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
        pass

    def afficher_questions(self, conn):
        curs = conn.cursor()
        print(curs.execute("SELECT * FROM Question").fetchall())

    def afficher_quizzs(self, conn):
        pass

    def recuperer_sauvegarde(self):
        pass
