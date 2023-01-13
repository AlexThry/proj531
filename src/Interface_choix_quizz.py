from tkinter import *
from src import Interface_login as IL
from src import Class_Database as DT


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
        
        #Connexion BdD et recuperation
        
        conn=sqlite3.connect("database.db")
        database = DT.Database()
        cpt = 0
        
        while (database.recuperer_quizz(cpt,conn) != None):
            text = database.recuperer_quizz(cpt,conn)

    		buttonTheme = Button(self.btns, text=text, font=(
    			"Courrier", 18), bg="#FFCCFF", fg="#FF0080", width=30, command=self.login())
    		buttonQuestion.grid(row=cpt+1, column=2, padx=10, pady=10)
            
            cpt +=1
            
		self.btns.place(relx=.5, rely=.5, anchor=CENTER)
        
        


	def afficher(self):
		# afficher
		self.window.mainloop()
        
if __name__ == '__main__':
    
    window = Interface_Choix_Quizz()
    window.afficher()
