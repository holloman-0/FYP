import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='Gaming55!!', host='127.0.0.1', database='pro_database')

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving single row
sql = '''SELECT * from Persons'''

#Executing the query
cursor.execute(sql)

#Fetching 1st row from the table
# result = cursor.fetchone()
# print(result)

#Fetching 1st row from the table
result = cursor.fetchall()
print(result)

#Closing the connection
conn.close()