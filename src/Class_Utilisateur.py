class Utilisateur:
    def __init__(self, login, isadmin):
        self.login = login
        self.isadmin = isadmin

    def historique(self, database, user):
        user = database.execute(f'SELECT id_utilisateur FROM Utilisateur')
