from tkinter import *
from tkinter import messagebox

class Class_login_interface:
    def __init__(self):
        self.window = Tk()
        
        #personnaliser fenettre
        self.window.title("ZZiuQ")
        self.window.geometry ("1080x720")
        self.window.resizable(False,False)
        
        """window.iconbitmap("ADD LOGO")""" 
        
        self.color = "White"
        """a changer"""

        self.window.config(background = self.color) 
        
        #Creation de frame principal
        self.frame = Frame(self.window,bg =self.color)
        self.frame.pack(fill="both",expand=False)
        
        #Creation user image
        self.image_utilisateur = Frame(self.frame,bg =self.color)
        
        #Creation login info
        self.information = Frame(self.frame,bg =self.color)
        
        label_type = Label(self.information,text = "Utilisateur",font=("Courrier",18),bg="Black",fg=self.color)
        label_type.place(anchor = CENTER, relx = .5, rely = .5)
        self.information.pack(fill="x",pady=10)
        
        #Creation btns
        self.boutons  = Frame(self.frame,bg =self.color)
        button_create = Button (self.boutons, text="Create Utilisateur",font=("Courrier",18),bg="Black",fg=self.color,width=30,command=self.login())
        button_create.grid(row=3,column=1,padx=20,pady=30)
        
        button_revenir = Button (self.boutons, text="Revenir",font=("Courrier",18),bg="Black",fg=self.color,width=30)
        #button_revenir = Button (self.frame, text=text,font=("Courrier",18),bg="white",fg=self.color,command=)
        button_revenir.grid(row=3,column=2,padx=20,pady=30)
        
        self.boutons.pack()
        
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