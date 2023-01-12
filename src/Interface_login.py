from tkinter import *
import sys
from src.Class_Jeu import *
from src.Class_Database import *
from src.Interface_menu import *
import sqlite3
import os
import time


class Interface_login:
	def __init__(self):
		self.game = Jeu()
		self.window = Tk()
		self.window.geometry('+150+150')
		self.is_connected = False

		# personnaliser fenettre
		self.window.title("ZZiuQ")
		self.window.geometry("1080x720")
		self.window.resizable(False, False)

		"""window.iconbitmap("ADD LOGO")"""

		self.color = "#6666FF"
		"""a changer"""

		self.window.config(background=self.color)

		# Creation de frame principal
		self.frame = Frame(self.window, bg=self.color)
		self.frame.pack(fill="both", expand=True)

		# # Creation user image
		# self.image_logo = Frame(self.frame, bg=self.color)
		# logo = PhotoImage(file=os.path.join("src", "loginIcon.jpg"))
		# label_logo = Label(self.image_logo, image=logo, height=300, width=300)
		# label_logo.pack()
		# self.image_logo.pack(fill="x", pady=10)

		# Creation login info
		self.information = Frame(self.frame, bg=self.color)

		label_utilisateur = Label(self.information, text="Nom d'utilisateur :", font=(
			"Courrier", 18), bg=self.color, fg="White")
		label_utilisateur.grid(row=0, column=2, padx=10, pady=10)

		self.label1 = Entry(self.information, bd=2)
		self.label1.grid(row=0, column=3, padx=10, pady=10)

		label_MP = Label(self.information, text="Mot de Passe :", font=(
			"Courrier", 18), bg=self.color, fg="White")
		label_MP.grid(row=1, column=2, padx=10, pady=10)

		self.label2 = Entry(self.information, bd=2)
		self.label2.grid(row=1, column=3, padx=10, pady=10)

		label_admin = Label(self.information, text="Mot de passe administrateur :", font=(
			"Courrier", 18), bg=self.color, fg="White")
		label_admin.grid(row=2, column=2, padx=10, pady=10)

		self.label3 = Entry(self.information, bd=2)
		self.label3.grid(row=2, column=3, padx=10, pady=10)

		self.information.place(relx=.45, rely=.6, anchor=CENTER)

		# Creation btns
		self.boutons = Frame(self.frame, bg=self.color)

		button_connexion = Button(self.boutons, text="CONNEXION", font=(
			"Courrier", 18), bg="#FFCCFF", fg="#FF0080", width=30, command=self.login)
		button_connexion.grid(row=3, column=1, padx=20, pady=30)

		button_inscription = Button(self.boutons, text="INSCRIPTION", font=(
			"Courrier", 18), bg="#FFCCFF", fg="#FF0080", width=30, command=self.sign_up)
		button_inscription.grid(row=3, column=2, padx=20, pady=30)

		self.boutons.place(relx=.5, rely=.8, anchor=CENTER)



	def login(self, conn=sqlite3.connect("database.db")):
		username = self.label1.get()
		password = self.label2.get()
		self.label1.delete(0, END)
		self.label2.delete(0, END)
		self.label3.delete(0, END)
		database = Database()
		curs = conn.cursor()
		bon_mdp = False
		self.is_admin = False
		if curs.execute(f"SELECT * FROM Utilisateur WHERE nom = '{username}'").fetchall():
			user = curs.execute(f"SELECT * FROM Utilisateur WHERE nom = '{username}'").fetchall()[0]
			print(user)
			bon_mdp = password == user[2]

			if bon_mdp:
				self.is_connected = True
				self.user = username
				database.set_user(username)

				self.window.destroy()
				window_menu = Class_menu()
				window_menu.afficher()
				
				if user[3] == "TRUE":
					self.is_admin = True
			else:
				self.color = "#F93106"
				time.sleep(0.5)
				self.color = "#6666FF"


			
			
	def sign_up(self):
		game = Jeu()
		conn=sqlite3.connect("database.db")
		curs = conn.cursor()
		login = self.label1.get()
		if not (curs.execute(f"SELECT nom FROM Utilisateur WHERE nom = '{login}'").fetchall()):
			mdp = self.label2.get()
			admin_key = self.label3.get()
			if admin_key:
				if admin_key == game.get_admin_key():
					curs.execute(
						f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "TRUE"))
					conn.commit()
			else:
				curs.execute(
					f"INSERT INTO Utilisateur(nom, mdp, isadmin) VALUES(?, ?, ?)", (login, mdp, "FALSE"))
				conn.commit()
		else:
			print("Cet utilisateur est déjà existant")


		

	def afficher(self):
		# afficher
		self.window.mainloop()

