from src.Interface_login import *
from src.Interface_creation_Question import *
from src.Interface_quizz import *
from src.Interface_menu import *


if __name__ == '__main__':
	conn = sqlite3.connect(os.path.join("..", "database.db"))
	login_window = Interface_login()
	login_window.afficher()
	while login_window.is_connected:
		window_menu = Class_menu()
		window_menu.afficher()

