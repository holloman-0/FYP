import mysql.connector

# Creating a running instance for mysql
instance = mysql.connector.connect(host='localhost',
                                     # Enter the Name of your database (schema) here
                                     database='',
                                     # Root is set as default unless changed
                                     user='root',
                                     # My password set to TechGroup, yours will be different
                                     password='TechGroup')


# Manipulating the running instance to get what we want
def pulling_data(instance):

    if instance.is_connected():
        db_info = instance.get_server_info()
        print("Connected to MySQL Server version ", db_info)

        #cursor = connection.cursor()
        # Returning the connected object, so we can close it later
        return instance


# Disconnecting from the database by passing the running instance
def disconnect_to_database(instance):

    instance.close()
    print("MySQL connection is closed")



running_instance = pulling_data(instance)

# Passing the running instance in the disconnect function so we can close it
disconnect_to_database(instance)