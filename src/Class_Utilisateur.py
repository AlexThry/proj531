class Utilisateur:
    def __init__(self, login, isadmin):
        self.login = login
        self.isadmin = isadmin

    def get_historique(self, login):
        id_user = database.execute(
            f'SELECT id_utilisateur FROM Utilisateur WHERE login = {login}')
        historique = database.execute(
            f'SELECT mode, score FROM HISTORIQUE WHERE id_user = {id_user}')
        print(historique)

    def edit_history(self, login, mode, score):
        id_user = database.execute(
            f'SELECT id_utilisateur FROM Utilisateur WHERE login = {login}')
        insert_into_history = database.execute(
            'INSERT INTO HISTORIQUE (idUtilisateur,score,mode) VALUES (?,?,?)', (id_user, mode, score))
