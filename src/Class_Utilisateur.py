class Utilisateur:
    def __init__(self, login, isadmin):
        self.login = login
        self.isadmin = isadmin

    def historique(self, database, login):
        id_user = database.execute(
            f'SELECT id_utilisateur FROM Utilisateur WHERE login={login}')
        historique = f'SELECT mode,score FROM HISTORIQUE WHERE id_user={id_user}'
        print(historique)
