from src.Class_Database import *
# from src.Interface_login import *
import random
import sqlite3
import time


class Quizz:
    def __init__(self):
        self.score = 0

    def execute(self, conn, database, login) -> None:
        """permet de commencer un quizz

        Args:
                conn (connexion): relie la database
                database (Database): permet de faire des requêtes à la base de donnés
                login (str): nom de l'utilisateur
        """
        curs = conn.cursor()
        idQuizz = database.choix_quizz(conn)
        self.nom = curs.execute(
            f"SELECT nom FROM Quizz WHERE idQuizz = '{idQuizz}'").fetchall()[0][0]
        quizz = database.recuperer_quizz(idQuizz, conn)
        quizz_melange = self.melange_quizz(quizz)
        self.repondre(quizz_melange, login, conn)

    def melange_quizz(self, quizz) -> str:
        """permet de mélanger les questions d'un quizz

        Args:
                quizz (str): le nom du quizz

        Returns:
                str: renvoie le nom du quizz mélangé
        """
        random.shuffle(quizz)
        return quizz

    def repondre(self, quizz, login, conn) -> None:
        """permet de répondre à une question posée

        Args:
                quizz (str): le nom du quizz
                login (str): le nom de l'utilisateur
                conn (connexion): relie à la database
        """
        self.score = 0
        db = Database()
        for i in range(len(quizz)):
            tuple_question = quizz[i]
            question = tuple_question[2]
            print(question)
            print(f"1. {tuple_question[3]}")
            print(f"2. {tuple_question[4]}\n")
            bonne_reponse = tuple_question[5]
            choix = input("Veuillez choisir la bonne réponse.\n")
            if choix == "1" and tuple_question[3] == bonne_reponse:
                print("Bonne réponse !\n")
                self.score = self.score + 1
            elif choix == "2" and tuple_question[4] == bonne_reponse:
                print("Bonne réponse !\n")
                self.score = self.score + 1
            else:
                print("Mauvaise réponse !\n")
        print(f"Votre score est de {self.score}")
        db.add_history(login, self.nom, self.score, conn)

    def question_interface(self, quizz) -> None:
        """Permet de relier l'interface à notre code

        Args:
                quizz (str): nom du quizz
        """
        i = 0
        while i <= len(quizz):
            window = Interface_quizz()
            window.create_question(quizz[i][2])
            window.create_btn(quizz[i][3], 0)
            window.create_btn(quizz[i][4], 1)
            window.afficher()
            i += 1
