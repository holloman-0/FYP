import csv
import os
import mysql.connector

def creating_sql_tables_pushing():

    # MAKE SURE TO PUT THE TABLES IN ORDER ALPHABETICALLY OF THE CSV FILES
    TABLES = {}
    TABLES['Crime'] = (
    "create table Crime(report_year int, agency_code varchar(20), agency_jurisdiction varchar(40), population varchar(10), violent_crimes varchar(20), homicides varchar(10), rapes varchar(10), assaults varchar(10), robberies varchar(10), months_reported varchar(10), crimes_percapita varchar(20), homicides_percapita varchar(20), rapes_percapita varchar(10), assualts_percapita varchar(10), robberies_percapita varchar(10)  )")
    TABLES['Alcohol'] = (
    "create table Alcohol(State varchar(20), State_abbrev varchar(30), Year  float, Beer float, Wine  float, Spirits  float, all_beverages float )")

    # Creating a connection with local server running
    connector = mysql.connector.connect(host='localhost',user='root',password='Gaming55!!')

    # Temporary work station for sql
    # Creating the DATABASE
    cursor = connector.cursor()
    cursor.execute('DROP DATABASE IF EXISTS TECH_PROJECT')
    cursor.execute("CREATE DATABASE tech_project")

    # Reconnecting to the newly created database
    # Creating another work station inside the tech_project database
    connector = mysql.connector.connect(host='localhost',user='root',password='Gaming55!!', database= "tech_project", charset='utf8', use_unicode=True)
    cursor = connector.cursor()

    # creating whatever tables that are in TABLES
    for x in TABLES:
        cursor.execute('DROP TABLE IF EXISTS {}'.format(x))
        cursor.execute(TABLES[x])

    pushing(cursor, connector, TABLES)



def pushing(cursor, connector , tables):

    # crime , min_wage
    list_of_csv = []

    # Getting the csv files ALPHABETICALLY
    for x in (os.listdir()):
        if x.endswith(".csv"):
            list_of_csv.append(x)

    # Print to see where the csv files are 
    #print(list_of_csv)

    # # 0,1
    for x in range(len(list_of_csv)):


        # getting the COLUMNS of each csv
        no_columns = len(list(tables.values())[x].split(','))
        
        # Opening the file
        file = open(list_of_csv[x])
        csvReader = csv.reader(file)

        # Skipping the first row as we dont need column headers
        next(csvReader)

        # Each row in csv sheet
        for row in csvReader:

            no_columns_placeholder = "%s" + (",%s" * (no_columns - 1))

            insert_values_sql = "INSERT INTO {} VALUES ({})".format(list(tables.keys())[x],no_columns_placeholder)
            column_values = [row[x] for x in range(len(row))]

            print(insert_values_sql)
            print(column_values)

            cursor.execute(insert_values_sql, column_values)
            connector.commit()

    connector.close()