import sqlite3
##############

def start(): #Prepare the Database
    conection = sqlite3.connect("Customers_DB") 
    c = conection.cursor()
    try:
        c.execute("SELECT rowid,* FROM clientes")
    except:
        c.execute("""CREATE TABLE clientes(
            	name text,
            	surname text,
        	    DNI text,
    	        correo text,
            	telefono integer )""")
    finally:
        conection.commit()

def show_clients():
    conection = sqlite3.connect("Customers_DB") 
    c = conection.cursor()
    c.execute("SELECT rowid,* FROM clientes")
    items = c.fetchall()
    #for item in items:#See all customers in terminal
        #print(item)
    return items

def add_customer(name="?", surname="?", dni="?", email="?", phone="?"):
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	try:
		c.execute("""INSERT INTO  clientes VALUES (?,?,?,?,?)""",(name.upper(), surname.upper(), dni.upper(), email, phone))
		conection.commit()
		#print(f"Customer {name} added successfully")
	except:
		#print("Something went wrong, try again")
		pass
	
def delete_by_ID(id):
	id = str(id)
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	try:	
		c.execute("""DELETE FROM clientes WHERE rowid = ({}) """.format(id))
		#print(f"Customer {id} deleted successfully")
	except:
		#print(f"Error while deleting customer nº{id}")
		pass
	conection.commit()

def find_by_name(name):
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	c.execute("SELECT rowid,* FROM clientes")
	items = c.fetchall()
	db_list=[]
	for item in items:
		if item[1].startswith(name.upper()):
			db_list.append(item)
	return db_list
	conection.commit()

def find_by_DNI(dni):
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	c.execute("SELECT rowid,* FROM clientes")
	items = c.fetchall()
	db_list=[]
	for item in items:
		if item[3].count(dni.upper()) != 0:
			db_list.append(item)
		else:
			pass
	return db_list
	conection.commit()

def sort_by_ID():
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	c.execute("SELECT rowid,* FROM clientes")
	items = c.fetchall()
	#for item in items:
	#	print(item)
	#	pass
	return items
	conection.commit()

def sort_by_name():
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	c.execute("SELECT rowid,* FROM clientes")
	items = c.fetchall()
	db_list = []
	x = 0
	for item in items:
		db_list.append(item[1])
		x += 1
	db_list.sort()
	n = 0
	y = 0
	while y < x: 
		if n >= x:
			break
		if items[y][1] == db_list[n]:
			db_list[n] = items[y]
			n = -1
			y += 1
		n +=1

	return db_list
	conection.commit()

def find_by_ID(id=0):
	conection = sqlite3.connect("Customers_DB") 
	c = conection.cursor()
	c.execute("SELECT rowid,* FROM clientes")
	items = c.fetchall()
	customer = []
	for item in items:
		if item[0] == int(id):
			customer = item
	conection.commit()
	return customer

start()