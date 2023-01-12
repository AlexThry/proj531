from tkinter import * 
#from ..Class_Quizz import *
#from ..Class_Database import *
#from ..Class_Jeu import *
import time 

class Interface_quizz:
    
    def __init__(self):
        self.window = Tk()
        
        #personnaliser fenettre
        self.window.title("ZZiuQ")
        self.window.geometry ("1080x720")
        self.window.resizable(False,False)
        
        #window.iconbitmap("ADD LOGO)
        
        self.color = "#6666FF"
        self.color_text = "#FF0080"
        """a changer"""

        self.window.config(background = self.color) 
        
        #Creation de frame principal
        self.frame = Frame(self.window,bg =self.color)
        self.frame.pack(fill="both",expand=False)

        
        #Creation top frame
        self.top_frame = Frame(self.frame,bg =self.color)
        
        #Creation question frame
        self.question_frame = Frame(self.frame,bg =self.color)
        
        #Creation answer frame
        self.answer_frame = Frame(self.frame,bg =self.color)
        
        btn_pause = Button(self.top_frame, text = "...", height= 1, width=2, command = self.window.destroy)
        btn_pause.grid(row=0,column=0,padx=10, pady=10)
        self.top_frame.pack(fill="x",pady=10)
        
    def afficher(self):
        #afficher
        self.window.mainloop()
        
    def create_btn(self,text1,text2):
        self.button1 = Button (self.answer_frame, text=text1,font=("Courrier",18),bg="white",fg=self.color_text ,width=30)
        self.button1.grid(row=0,column=0,padx=20,pady=30)
        self.answer_frame.pack()
        
        self.button2 = Button (self.answer_frame, text=text2,font=("Courrier",18),bg="white",fg=self.color_text ,width=30)
        self.button2.grid(row=0,column=1,padx=20,pady=30)
        self.answer_frame.pack()
        
        self.button1.configure(command=lambda btn=self.button1: self.OnClick(btn))
        self.button2.configure(command=lambda btn=self.button2: self.OnClick(btn))
        
        self.click=False        
    def create_question(self,text):
        label_question = Label(self.question_frame,text = text,font=("Courrier",18),bg="white",fg=self.color_text ,height=10)
        label_question.pack(fill="x")
        self.question_frame .pack(fill="x")
        
    def type_jeu(self,text):
        label_type = Label(self.top_frame,text = text,font=("Courrier",18),bg=self.color,fg="white")
        label_type.place(anchor = CENTER, relx = .5, rely = .5)
        self.top_frame.pack(fill="x",pady=10)
        
    def score (self,score):
        label_score = Label(self.top_frame,text = f"Score: {score}",font=("Courrier",16),bg=self.color,fg="white")
        label_score.place(anchor = W, relx = .8, rely = .25)
        self.top_frame.pack(fill="x",pady=10)
    
    def nombre_question(self,nombre,nombre_total=None):
        if nombre_total != None:
            text = f"Question {nombre}/{nombre_total}"
            label_nombre_question = Label(self.top_frame,text = text,font=("Courrier",16),bg=self.color,fg="white")
            label_nombre_question.place(anchor = W, relx = .8, rely = .75)
            self.top_frame.pack(fill="x",pady=10)
        else:
            text = f"Question {nombre}"
            label_nombre_question = Label(self.top_frame,text = text,font=("Courrier",16),bg="white",fg=self.color)
            label_nombre_question.place(anchor = W, relx = .8, rely = .75)
            self.top_frame.pack(fill="x",pady=10)
        
    def time (self,time):
        label_score = Label(self.top_frame,text = time,font=("Courrier",16),bg=self.color,fg="white")
        label_score.place(anchor = W, relx = .15, rely = .5)
        self.top_frame.pack(fill="x",pady=10)
        
    def OnClick(self, btn):
        self.text = btn.cget("text")
        self.click = True

    def recu_reponse(self):
        if self.click:
            return self.text
            self.text=None
        else:
            return None
        
    def execute(qelf, quizz):
        continuer = True
        window = Interface_quizz()
        while continuer:
            
            window.create_question("Question long")
            window.create_btn("Reponse 1","Reponse 2")
            window.type_jeu("Contre le temlighblhbp")
            window.score("1200")
            window.nombre_question(1,10)
            window.time("10:35")
            window.afficher()
            
            print(window.recu_reponse()) #None s'il n'y a pas de reponse 
            
if __name__ == "__main__":
    window = Interface_quizz()
    window.create_question("Question long")
    window.create_btn("Reponse 1","Reponse 2")
    window.type_jeu("Contre le temps")
    window.score("1200")
    window.nombre_question(1,10)
    window.time("10:35")
    window.afficher()