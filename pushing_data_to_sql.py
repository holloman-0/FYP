import csv
import mysql.connector

# PIP install

# Creating a connection with local server running 
connector = mysql.connector.connect(host='localhost',user='root',password='Gaming55!!')

# Temporary work station for sql
# Creating the database
cursor = connector.cursor()
cursor.execute('DROP DATABASE IF EXISTS TECH_PROJECT')
cursor.execute("CREATE DATABASE tech_project")

# Reconnecting to the newly created database
# Creating another work station inside the tech_project database
connector = mysql.connector.connect(host='localhost',user='root',password='Gaming55!!', database= "tech_project")
cursor = connector.cursor()

TABLES = {}
TABLES['students'] = ("create table students(name varchar(30) primary key, age int, address varchar(20))")

for x in TABLES:
    cursor.execute('DROP TABLE IF EXISTS {}'.format(x))
    cursor.execute(TABLES[x])


# INSERTING THE DATA
infilestudents = open("practice.csv") 

# PIP3 INSTALL READER
csvReader = csv.reader(infilestudents)

# Skip first column in csv document as in database
next(csvReader)

for row in csvReader:
    cursor.execute("INSERT INTO students VALUES (%s,%s,%s)", [row[0],row[1],row[2]])
    connector.commit()

# Closing the connection
connector.close()
