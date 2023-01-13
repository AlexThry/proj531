from src.Interface_login import *
from src.Interface_creation_Question import *
from src.Interface_quizz import *
from src.Interface_menu import *

class Interface:
	def __init__(self):
		self.is_connected = False

	def set_is_connected(self, bool):
		self.set_is_connected = bool

	def get_is_connected(self):
		return self.get_is_connected

if __name__ == '__main__':
	conn = sqlite3.connect(os.path.join("..", "database.db"))
	login_window = Interface_login()
	login_window.afficher()


()