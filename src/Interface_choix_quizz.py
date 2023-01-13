from tkinter import *
import sys
sys.path.append("../")
from src import Class_Jeu as JEU
from src import Interface_login as IL
from src import Class_Database as DT
import sqlite3 as SQL
import os



class Interface_Choix_Quizz:
	def __init__(self):
		self.window = Tk()
		self.window.geometry('+300+300')
		self.deconnexion = False

		# personnaliser fenettre
		self.window.title("Menu")
		self.window.geometry("1080x720")
		self.window.resizable(False, False)

		"""window.iconbitmap("ADD LOGO")"""

		self.color = "#6666FF"

		self.window.config(background=self.color)

		# Creation de frame principal
		self.frame = Frame(self.window, bg=self.color)
		self.frame.pack(fill="both", expand=True)

		# Creation login info
		self.logo = Frame(self.frame, bg=self.color)

		label_titre = Label(self.logo, text="ZZuiQ", font=("Courrier", 80), bg=self.color, fg="White")
		label_titre.grid(row=0, column=2, padx=10)
		
		self.logo.place(relx=.5, rely=.1, anchor=CENTER)

		
		self.btns = Frame(self.frame, bg=self.color)
		
		conn = SQL.connect("database.db")
		database = DT.Database()
		cpt = 0
		
		#quizz = database.recuperer_quizz(cpt,conn)
		quizz=["jnsd","hjsd","jhsd","ohsdq"]
		print(quizz)
		
		for i in quizz:
			buttonQuizz = Button(self.btns, text=i, font=(
				"Courrier", 18), bg="#FFCCFF", fg="#FF0080", width=20)
			buttonQuizz.pack()
				
		self.btns.place(relx=.5, rely=.5, anchor=CENTER)
		
		self.revenir = Frame(self.frame, bg=self.color)

		button_revenir = Button (self.revenir, text="REVENIR",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30, command = self.window.destroy)
		button_revenir.grid(row=3,column=2,padx=20,pady=30)
		
		self.revenir.place(relx=.5, rely=.9, anchor=CENTER)

	def jqsldn(self):
		pass
				


	def afficher(self):
		# afficher
		self.window.mainloop()
		
if __name__ == '__main__':
	
	window = Interface_Choix_Quizz()
	window.afficher()
