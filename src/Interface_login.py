from tkinter import *
import sys
sys.path.append("../")
from src import Class_Jeu as JEU
import sqlite3
import os

class Class_login_interface:
	def __init__(self):
		self.game = JEU.Jeu()
		self.window = Tk()
		
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
		
		#Creation user image
		self.image_logo= Frame(self.frame,bg =self.color)
		logo = PhotoImage(file=os.path.join("src", "Interface", "loginIcon.jpg"))
		label_logo = Label(self.image_logo,image=logo,height=300,width=300)
		label_logo.pack()
		self.image_logo.pack(fill="x",pady=10)
		
		#Creation login info
		self.information = Frame(self.frame,bg =self.color)
		
		label_utilisateur = Label(self.information,text = "Nom d'utilisateur :",font=("Courrier",18),bg=self.color,fg="White")
		label_utilisateur.grid(row=0,column=2,padx=10, pady=10)
		
		self.label1 = Entry(self.information,bd=2)
		self.label1.grid(row=0,column=3,padx=10, pady=10)
		
		label_MP = Label(self.information,text = "Mot de Passe :",font=("Courrier",18),bg=self.color,fg="White")
		label_MP.grid(row=1,column=2,padx=10, pady=10)
		
		self.label2 = Entry(self.information,bd=2)
		self.label2.grid(row=1,column=3,padx=10, pady=10)
		
		label_admin = Label(self.information,text = "Mot de passe administrateur :",font=("Courrier",18),bg=self.color,fg="White")
		label_admin.grid(row=2,column=2,padx=10, pady=10)
		
		self.label3 = Entry(self.information,bd=2)
		self.label3.grid(row=2,column=3,padx=10, pady=10)
		
		self.information.place(relx=.45,rely=.6,anchor=CENTER)
		
		#Creation btns
		self.boutons  = Frame(self.frame,bg =self.color)
		
		button_connexion = Button (self.boutons, text="CONNEXION",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30,command=self.login(self.game, conn))
		button_connexion.grid(row=3,column=1,padx=20,pady=30)
		
		button_inscription = Button (self.boutons, text="INSCRIPTION",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30)
		button_inscription.grid(row=3,column=2,padx=20,pady=30)
		
		self.boutons.place(relx=.5,rely=.8,anchor=CENTER)
		
	def set_image(self,text):
		pass
	
	def login (self, game, conn):
		username = self.label1.get()
		password = self.label2.get()
		'''
		if password == " " and username == " ":
			messagebox.showinfo( "", "Espace vide non accepté")
		elif password != " " and username != " ":
			messagebox.showinfo( "", "login suces")'''
		game.connexion



		
	
	def afficher(self):
		#afficher
		self.window.mainloop()
		
		
if __name__ =="__main__":
	conn = sqlite3.connect(os.path.join("..", "..", "database.db"))
	window = Class_login_interface()
	window.afficher()