from tkinter import *

class Class_menu:
    def __init__(self):
        self.window = Tk()
        
        #personnaliser fenettre
        self.window.title("Menu")
        self.window.geometry ("1080x720")
        self.window.resizable(False,False)
        
        """window.iconbitmap("ADD LOGO")""" 
        
        self.color = "#6666FF"

        self.window.config(background = self.color) 
        
        #Creation de frame principal
        self.frame = Frame(self.window,bg =self.color)
        self.frame.pack(fill="both",expand=True)
        
        #Creation user image
        '''self.image_logo= Frame(self.frame,bg =self.color)
        logo = PhotoImage(file="loginIcon.png")
        label_logo = Label(self.image_logo,image=logo)
        label_logo.pack()
        self.image_logo.pack(fill="x",pady=10)'''
        
        #Creation login info
        self.information = Frame(self.frame,bg =self.color)
        
        label_titre = Label(self.information,text = "ZZuiQ",font=("Courrier",80),bg=self.color,fg="White")
        label_titre.grid(row=0,column=2,padx=10)

        buttonQuestion = Button(self.information, text= "Ajouter une question",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30,command=self.login())
        buttonQuestion.grid(row=1,column=2,padx=10, pady=10)

        buttonQuestion = Button(self.information, text= "Quizz",font=("Courrier",18),bg="#FFCCFF",fg="#FF0080",width=30,command=self.login())
        buttonQuestion.grid(row=2,column=2,padx=10, pady=10)

        label_histo = Label(self.information,text = "Historique:",font=("Courrier",18),bg=self.color,fg="White")
        label_histo.grid(row=6,column=1,padx=10, pady=10)
        liste_Histo = Listbox(self.information,background=self.color,foreground="White",bd=0)
        liste_Histo.insert(1, "01/01/23 16:34")
        liste_Histo.insert(2, "03/01/23 10:11")
        liste_Histo.insert(3, "14/01/23 20:32")
        liste_Histo.grid(row=7,column=2,padx=10, pady=10)

        label_MJ = Label(self.information,text = "Modes de Jeu:",font=("Courrier",18),bg=self.color,fg="White")
        label_MJ.grid(row=3,column=1,padx=10, pady=10)
        choix1 = Checkbutton(self.information,text="Mode 1",background=self.color,foreground="White")
        choix1.grid(row=3,column=2,padx=10, pady=10)
        choix2 = Checkbutton(self.information,text="Mode 2",background=self.color,foreground="White")
        choix2.grid(row=4,column=2,padx=10, pady=10)
        choix3 = Checkbutton(self.information,text="Mode 3",background=self.color,foreground="White")
        choix3.grid(row=5,column=2,padx=10, pady=10)

        self.information.place(relx=.45,rely=.5,anchor=CENTER)

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
    window = Class_menu()
    window.afficher()


        

        
        
        