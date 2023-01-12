import src.Class_Database as db
from src.Interface.Class_Interface import *
import random

class Quizz:
	def __init__(self):
		self.score = 0

	def execute(self, conn, database):
		curs = conn.cursor()
		idQuizz = database.choix_quizz(conn)
		quizz = database.recuperer_quizz(idQuizz, conn)
		quizz_melange = self.melange_quizz(quizz)
		self.repondre(quizz_melange)

	def melange_quizz(self, quizz):
		random.shuffle(quizz)
		return quizz

	def repondre(self, quizz):
		self.score = 0
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

	def question_interface(self, conn, database):
		window = Interface_quizz()
		continuer = True
		while continuer:
			window.create
