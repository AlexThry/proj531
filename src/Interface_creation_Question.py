import random
from tkinter import *
import sys
sys.path.append("../")
from src import Class_Jeu as JEU
from src import Class_Database as DT
from src import Interface_menu as IM
import sqlite3
import os

class Interface_creation_Question:
	def __init__(self, login):
		self.window = Tk()
		self.login = login
		
		#personnaliser fenettre
		self.window.title("ZZiuQ")
		self.window.geometry ("1080x720")
		self.window.resizable(False,False)
		
		"""window.iconbitmap("ADD LOGO")""" 
		
		self.color = "#6666FF"
		"""a changer"""

		self.window.config(background = self.color) 
		
		#Creation de frame principal
		self.frame = Frame(self.window,bg =self.color)
		self.frame.pack(fill="both",expand=True)
		
		
		#Creation login info
		self.information = Frame(self.frame,bg =self.color)
		
		label_Question = Label(self.information,text = "Rentrez votre question :",font=("Courrier",18),bg=self.color,fg="White")
		label_Question.grid(row=0,column=0,padx=10, pady=10)
		
		self.label1 = Entry(self.information,bd=2,width=100)
		self.label1.grid(row=1,column=0,padx=10, pady=10)
		
		label_Reponse_correct = Label(self.information,text = "Rentrez la bonne réponse :",font=("Courrier",18),bg=self.color,fg="White")
		label_Reponse_correct.grid(row=2,column=0,padx=10, pady=10)
		
		self.label2 = Entry(self.information,bd=2,width=100)
		self.label2.grid(row=3,column=0,padx=10, pady=10)
		
		label_Reponse_not_correct = Label(self.information,text = "Rentrez la mauvaise réponse :",font=("Courrier",18),bg=self.color,fg="White")
		label_Reponse_not_correct.grid(row=4,column=0,padx=10, pady=10)
		
		self.label3 = Entry(self.information,bd=2,width=100)
		self.label3.grid(row=5,column=0,padx=10, pady=10)
		
		self.information.place(relx=.5,rely=.4,anchor=CENTER)
		
		#Creation btns
		self.boutons  = Frame(self.frame,bg =self.color)
		
		button_create = Button (self.boutons, text="AJOUTER QUESTION",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30,command=self.create_question)
		button_create.grid(row=3,column=1,padx=20,pady=30)
		
		button_revenir = Button (self.boutons, text="REVENIR",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30, command = self.back)
		button_revenir.grid(row=3,column=2,padx=20,pady=30)
		
		self.boutons.place(relx=.5,rely=.8,anchor=CENTER)
		
	def set_image(self,text):
		pass
	
	def get_info (self):
		question = self.label1.get()
		reponse_correct = self.label2.get()
		reponse_not_correct = self.label3.get()
		
		conn = sqlite3.connect( "database.db")
		database = DT.Database()
		database.creer_question_Interface(conn, question, reponse_correct, reponse_not_correct)        
		print("ok")
		self.window.destroy

	def back(self):
		window = IM.Interfac_menu(self.login)
		self.window.destroy()

	def create_question(self):
		conn = sqlite3.connect('database.db')
		curs = conn.cursor()
		question = self.label1.get()
		bonne_reponse = self.label2.get()
		mauvaise_reponse = self.label3.get()
		print(question)
		print(bonne_reponse)
		print(mauvaise_reponse)
		if question and bonne_reponse and mauvaise_reponse:
			values = [question, None, None, bonne_reponse]
			pos = random.randint(1, 2)
			if pos == 1:
				values[1] = bonne_reponse
				values[2] = mauvaise_reponse
			else:
				values[1] = bonne_reponse
				values[2] = mauvaise_reponse
			curs.execute(f"INSERT INTO Question (question, reponse1, reponse2, bonne_reponse) VALUES(?, ?, ?, ?)", tuple(values))
			conn.commit()
			self.popup("Vous avez crée une question")
		else:
			self.popup("veuillez remplir les champs")

	def popup(self, message):
		popup = Tk()
		label = Label(popup, text=message)
		ok = Button(popup, text="ok", command=popup.destroy)
		label.pack()
		ok.pack()
		popup.mainloop()

		
	def afficher(self):
		#afficher
		self.window.mainloop()
		