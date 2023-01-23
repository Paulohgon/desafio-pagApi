import sqlite3


connection = sqlite3.connect('transfeera_db')
import psycopg2

# connection = psycopg2.connect(database="transfeera",
#                         host="localhost",
#                         user="jetbov",
#                         password="jetbov",
#                         port="8080")
# connection = psycopg2.connect("dbname=transfeera user=jetbov password=jetbov")


def create_database():
	
    cursor = connection.cursor()

    try:

        cursor.execute("""
			CREATE TABLE IF NOT EXISTS receiver (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				name character varying(255),
				cpf character varying(50),
				bank character varying(100),
				agency character varying(50),
				cc character varying(50),
				validated bool,
				email character varying(100),
				deleted bool
			);"""
		)
        cursor.execute("""	CREATE TABLE IF NOT EXISTS pix (
				id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
				receiver_id int,
				email character varying(250),
				pix character varying(140),
				type character varying(50),
				deleted bool,
			
				foreign key (receiver_id) references receiver(id)
			);""")
        cursor.close()

    except sqlite3.Error as error:
        raise Exception(error)


def get_one(query):

	cursor = connection.cursor()
	cursor.execute(query)
	result = cursor.fetchone()
	return result


def get_all(query):

	cursor = connection.cursor()
	cursor.execute(query)
	result = cursor.fetchall()
	return result

def insert(query):
	cursor = connection.cursor()
	cursor.execute(query)
	connection.commit()


def update(query):
	cursor = connection.cursor()
	cursor.execute(query)
	connection.commit()

def updateMany(query):
	cursor = connection.cursor()
	cursor.executescript(query)
	connection.commit()
	