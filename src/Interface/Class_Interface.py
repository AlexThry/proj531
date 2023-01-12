from tkinter import * 
import time 

class Interface_quizz:
    
    def __init__(self):
        self.window = Tk()
        
        #personnaliser fenettre
        self.window.title("ZZiuQ")
        self.window.geometry ("1080x720")
        self.window.resizable(False,False)
        
        """window.iconbitmap("ADD LOGO")""" 
        
        self.color = "red"
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
        
    def create_btn(self,text,column):
        button = Button (self.answer_frame, text=text,font=("Courrier",18),bg="white",fg=self.color,width=30)
        #button = Button (self.frame, text=text,font=("Courrier",18),bg="white",fg=self.color,command=)
        button.grid(row=0,column=column,padx=20,pady=30)
        self.answer_frame.pack()
        
    def create_question(self,text):
        label_question = Label(self.question_frame,text = text,font=("Courrier",18),bg="white",fg=self.color,height=10)
        label_question.pack(fill="x")
        self.question_frame .pack(fill="x")
        
    def type_jeu(self,text):
        label_type = Label(self.top_frame,text = text,font=("Courrier",18),bg="white",fg=self.color)
        label_type.place(anchor = CENTER, relx = .5, rely = .5)
        self.top_frame.pack(fill="x",pady=10)
        
    def score (self,score):
        label_score = Label(self.top_frame,text = f"Score: {score}",font=("Courrier",16),bg="white",fg=self.color)
        label_score.place(anchor = W, relx = .8, rely = .25)
        self.top_frame.pack(fill="x",pady=10)
    
    def nombre_question(self,nombre,nombre_total=None):
        if nombre_total != None:
            text = f"Question {nombre}/{nombre_total}"
            label_nombre_question = Label(self.top_frame,text = text,font=("Courrier",16),bg="white",fg=self.color)
            label_nombre_question.place(anchor = W, relx = .8, rely = .75)
            self.top_frame.pack(fill="x",pady=10)
        else:
            text = f"Question {nombre}"
            label_nombre_question = Label(self.top_frame,text = text,font=("Courrier",16),bg="white",fg=self.color)
            label_nombre_question.place(anchor = W, relx = .8, rely = .75)
            self.top_frame.pack(fill="x",pady=10)
        
    def time (self,time):
        label_score = Label(self.top_frame,text = time,font=("Courrier",16),bg="white",fg=self.color)
        label_score.place(anchor = W, relx = .15, rely = .5)
        self.top_frame.pack(fill="x",pady=10)
        
        
if __name__ =="__main__":
    window = Interface_quizz()
    window.create_question("Question long")
    window.create_btn("Reponse 1",0)
    window.create_btn("Reponse 2",1)
    window.type_jeu("Contre le temp")
    window.score("1200")
    window.nombre_question(1,10)
    window.time("10:35")
    window.afficher()