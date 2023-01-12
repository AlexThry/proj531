import os
import random
import sqlite3 as sql


class Database:
    def __init__(self) -> None:
        return None

    def set_user(self, user) -> None:
        """permet d'établir l'utilisateur

        Args:
                user (string): utilisateur courant
        """
        self.user = user

    def creer_compte(self, conn, game) -> None:
        """permet de créer un compte administrateur ou utilisateur

        Args:
                conn (connexion): connexion à la database
                game (Jeu): relie la fonction à la classe jeu pour obtenir la clé qui identifie un administrateur
        """
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

    def supprimer_compte(self, conn, game) -> None:
        """permet de supprimer un compte administrateur ou utilisateur

        Args:
                conn (connexion): connexion à la database
                game (Jeu): relie la fonction à la classe jeu pour obtenir la clé qui identifie un administrateur
        """
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

    def creer_question(self, conn) -> None:
        """permet de créer une question

        Args:
            conn (connexion): connexion à la database
        """
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

    def creer_quizz(self, conn) -> None:
        """permet de créer un quizz

        Args:
            conn (connexion): connexion à la database
        """
        nom = input("Nom du quizz : \n")
        theme = input("Theme du quizz : \n")
        curs = conn.cursor()
        curs.execute(
            "INSERT INTO Quizz (nom, theme) VALUES (?, ?)", (nom, theme))
        conn.commit()

    def ajouter_questions_quizz(self, conn) -> None:
        """permet d'ajouter une question dans un quizz

        Args:
            conn (connexion): connexion à la database
        """
        curs = conn.cursor()
        ajouter = True

    def afficher_questions(self, conn) -> None:
        """permet d'afficher les questions à l'utilisateur

        Args:
            conn (connexion): connexion à la database
        """
        curs = conn.cursor()
        questions = curs.execute("SELECT * FROM Question").fetchall()
        for item in questions:
            print(item[1])

    def afficher_quizzs(self, conn) -> None:
        """affiche le quizz à l'utilisateur

        Args:
            conn (_type_): _description_
        """
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

    def choix_quizz(self, conn) -> int:
        """Permet à l'utilisateur de choisir un quizz parmis les quizz existants

        Args:
                        conn (connection): permet de se connecter à la base de donnés

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

    def recuperer_quizz(self, id_quizz, conn) -> str:
        """permet de récupérer le quizz correspondant à l'id voulu

        Args:
            id_quizz (int): l'id du quizz dans la base de donnés
            conn (connexion): connexion à la database

        Returns:
            str: le nom du quizz qui correspond à l'id en entré
        """
        curs = conn.cursor()
        quizz = curs.execute(
            f"SELECT * FROM appartient NATURAL JOIN Question WHERE idQuizz = {id_quizz}").fetchall()
        return quizz

    def get_historique(self, login, conn) -> None:
        """Affiche l'historique

        Args:
            login (str): nom de l'utilisateur
            conn (connexion): relie la database
        """
        curs = conn.cursor()
        id_user = (curs.execute(
            f"SELECT idUtilisateur FROM Utilisateur WHERE nom = '{login}'").fetchall())[0][0]
        historique = (curs.execute(
            f"SELECT mode, score FROM Historique WHERE idUtilisateur = '{id_user}'").fetchall())
        for item in range(len(historique)):
            print(
                f"########## HISTORIQUE ##########\nNom du Zziuq : {historique[item][1]}\nScore du joueur : {historique[item][0]}")

    def add_history(self, login, quizz_name, score, conn) -> None:
        """permet de mettre à jour l'historique de l'utilisateur

        Args:
            login (str): nom de l'utilisateur
            quizz_name (str): nom du quizz à mettre à jour
            score (int): score du joueur
            conn (connexion): relie la database
        """
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
