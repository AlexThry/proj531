from src.Class_Database import *

class Menu:
	def __init__(self) -> None:
		return None

	def execute(self, game, conn, database):
		curs = conn.cursor()
		while True:


			print("########## CONNEXION ########## \n")
			print("1. Se Connecter")
			print("2. Créer un compte")
			print("3. Quitter \n4. Afficher les utilisateurs")
			rep = input("Faites votre choix \n")


			if rep == "3":
				conn.commit()
				conn.close()
				break


			elif rep == "2":
				database.creer_compte(conn)


			elif rep == "1":
				game.connexion(conn, database)
				while game.get_is_connected():
					print("########## MENU ########## \n")
					print("1. Jouer \n2. Historique \n3. Deconnecter\n4. Supprimer le compte")
					if game.get_is_admin():
						print("5. Fonctionnalités administrateur")
					rep = input("Faites votre choix \n")

					if rep == "3":
						game.deconnexion()

					elif rep == "4":
						database.supprimer_compte(conn, game)

					elif game.get_is_admin() and rep == "5":
						menu_admin = True
						while menu_admin:
							print("########## ADMINISTRATEUR ##########\n")
							print("1. Créer une question \n2. Créer un Quizz \n3. Ajouter des questions à un quizz \n4. Afficher les questions \n5. Afficher les quizzs\n6. Changer la clé administrateur \n7. Afficher la clé administrateur \n8. Retour")
							rep = input("Faites votre choix \n")

							if rep == "1":
								database.creer_question(conn)

							elif rep == "2":
								database.creer_quizz(conn)
							
							elif rep == "3":
								database.ajouter_questions_quizz(conn)

							elif rep == "4":
								database.afficher_questions(conn)

							elif rep == "5":
								database.afficher_quizzs(conn)

							elif rep == "6":
								database.set_admin_key(conn)

							elif rep == "7":
								print(f"La clé administrateur est : {database.get_admin_key()}\n")
							
							elif rep == "8":
								menu_admin = False

							else:
								print("Veuillez effectuer un choix correct")



					else:
						print("Veuillez effectuer un choix correct")


			elif rep == "4":
				users = curs.execute("SELECT * FROM Utilisateur").fetchall()
				for user in users:
					print(user[1])
			
			else:
				print("Veuillez effecctuer un choix correct")
				
