import sqlite3


connection = sqlite3.connect('pagamentos_db')
import psycopg2



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

        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Paulo Henrique","123.243.432-45","itau","0123","00012345-6",False,"paulo@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Joao Batista","123.333.321-45","bradesco","1123","00012345-7",False,"joao@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Jucapirama da silva","323.243.472-45","banco legal","2345","01032345-6",False,"juca@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Lucas Nunes","673.243.432-45","Nuvank","3323","03312345-7",False,"lucaaas@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Lilia da Silva","224.254.432-45","itau","6123","00012345-6",False,"lilia@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Marilia Mendo","555.243.432-90","santandre","3223","00011145-6",False,"marialili@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Voltair dos Santos","993.789.432-45","itapema bank","5454","03054345-9",False,"volt.santos@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Malena Millnitz","493.564.432-75","c7-bank","3421","32122345-6",False,"male.mil@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Leonardo Porto","654.567.876-43","nubanco","0909","32312455-9",False,"leo.p@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Leandro Turbano","321.123.456-90","c6-bank","5009","3234343-9",False,"leandro.T@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Gustavo Diffs","473.912.543-94","c9-bank","5449","3236767-9",False,"gustav.dif@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Maria da Rosa","321.645.999-90","c6-bank","5934","5345612-4",False,"marry.rose@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Karla Carol","321.123.456-90","caixa","9432","1231239-9",False,"K.carol@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Carolina Joaquina","735.543.213-77","banco do brasil","9090","9090909-9",False,"joaq.carol@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Joao das rosas","432.539.123-77","banco do brasil","9081","8070909-9",False,"rose.john@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Silvana da Silva","342.453.613-37","banco roxo","2323","1231234-4",False,"silvanda.silva@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Bionardo Silveira","123.854.243-29","itaum","1257","93303232-1",False,"biona.sil@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Leon Do Castel","333.564.777-39","banco laranja","3457","42303232-1",False,"leon.castel@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Lionel Martini","395.343.090-69","banco azul","4357","90743232-1",False,"lionel.mart@gmail.com",False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Carlos Oliveira", "999.112.435-50", "c6-bank", "0392", "00614643-1", False, "carlos.oli@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Carol Marques", "213.893.333-60", "c6-bank", "9100", "10103991-8", False, "marquescarol@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Jorge Lacerda", "780.945.164-44", "itau", "0890", "00022532-4", False, "jorge@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Ian Silva", "123.432.123-72", "c6-bank", "0020", "00510012-1", False, "iansilva@outlook.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Plínio Augusto Aquini", "456.800.400-31", "sicredi", "6031", "00009178-9", False, "plinio.aquini@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Rogéria Mascattes", "012.337.005-12", "safra", "7711", "88900060-3", False, "rogeria@mascatte.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Maria Guerreiro", "050.869.555-49", "itau", "1298", "47917300-8", False, "maria.guerreiro@yahoo.com.br", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Jim Anderson", "000.900.348-25", "itau", "9999", "56465711-1", False, "jim@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Zélia Araquara Machado", "211.216.437.86", "nubank", "0101", "17583830-18", False, "machado@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Jacó Galhardo dos Santos", "650.573.210-01", "nubank", "5439", "85911453-9", False, "galhardosantos@gmail.com", False);""")
        cursor.execute("""insert into receiver (name,cpf,bank,agency,cc,validated,email,deleted)
						values ("Gabriel Lee", "749.324.643-99", "nubank", "1231", "75398112-3", False, "lee@gmail.com", False);""")


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
	
