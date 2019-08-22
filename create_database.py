from catalogue import database

if __name__ == '__main__':
	database.drop_all()
	database.create_all()
