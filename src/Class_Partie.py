class Partie:
    def __init__(self, score, temps):
        self.score = score
        self.temps = temps

    def lancement_partie(self):
        pass

    def choix_quizz(self):
        pass

    def choix_question(self):
        pass

    def chronomètre(self):
        return self.temps

    def get_score(self):
        return self.score

    def question(self):
        pass
