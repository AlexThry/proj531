from tkinter import *

class Class_login_interface:
    def __init__(self):
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
        
        
        #Creation login info
        self.information = Frame(self.frame,bg =self.color)
        
        label_Question = Label(self.information,text = "Rentrez votre question :",font=("Courrier",18),bg=self.color,fg="White")
        label_Question.grid(row=0,column=0,padx=10, pady=10)
        
        self.label1 = Entry(self.information,bd=2,width=150)
        self.label1.grid(row=1,column=0,padx=10, pady=10)
        
        label_Reponse_correct = Label(self.information,text = "Rentrez la bonne réponse :",font=("Courrier",18),bg=self.color,fg="White")
        label_Reponse_correct.grid(row=2,column=0,padx=10, pady=10)
        
        self.label2 = Entry(self.information,bd=2,width=100)
        self.label2.grid(row=3,column=0,padx=10, pady=10)
        
        label_Reponse_not_correct = Label(self.information,text = "rentrez une mauvaise réponse :",font=("Courrier",18),bg=self.color,fg="White")
        label_Reponse_not_correct.grid(row=4,column=0,padx=10, pady=10)
        
        self.label3 = Entry(self.information,bd=2,width=100)
        self.label3.grid(row=5,column=0,padx=10, pady=10)
        
        self.information.place(relx=.5,rely=.4,anchor=CENTER)
        
        #Creation btns
        self.boutons  = Frame(self.frame,bg =self.color)
        
        button_create = Button (self.boutons, text="AJOUTER QUESTION",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30,command=self.login())
        button_create.grid(row=3,column=1,padx=20,pady=30)
        
        button_revenir = Button (self.boutons, text="REVENIR",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30)
        button_revenir.grid(row=3,column=2,padx=20,pady=30)
        
        self.boutons.place(relx=.5,rely=.8,anchor=CENTER)
        
    def set_image(self,text):
        pass
    
    def login (self):
        '''username = label1.get()
        password = label2.get()
        
        if password == " " and username == " ":
            messagebox.showinfo( "", "Espace vide non accepté")
        elif password != " " and username != " ":
            messagebox.showinfo( "", "login suces")'''
        pass
    
    def afficher(self):
        #afficher
        self.window.mainloop()
        
        
if __name__ =="__main__":
    window = Class_login_interface()
    window.afficher()