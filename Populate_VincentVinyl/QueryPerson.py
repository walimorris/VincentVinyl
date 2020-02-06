import mysql.connector
from mysql.connector import Error

try: 



    # CREATE DATABASE CONNECTION 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='') # ADD PASSWORD 

    # CONNECT CURSOR
    cursor = connection.cursor()

    # CREATE QUERY
    person_insert_query = """INSERT INTO Person(idPerson, PersonLastName, PersonFirstName,
                                                PersonEmail, PersonPhone)
                          VALUES(%s, %s, %s, %s, %s) """

    # INSERT VALUES
    # PersonId 1 has been added prior to this program: George Stanley 
    person_to_insert = [(2, 'Lynn', 'Mary', 'marylynn@msn.com', '2065552345'), 
                        (3, 'Seymore', 'John', 'js@seymore.com', '4255551234'),
                        (4, 'Lewis', 'Tom', 'tom.lewis@yahoo.com', '4255552345'),
                        (5, 'Denton', 'Mark', 'markdenton@gmail.com', '2065554321'),
                        (6, 'Kanton', 'Lynn', 'lcanton@version.com', '2065555432'),
                        (7, 'Tyson', 'Andrew', 'atyson34@gmail.com', '2065556767'), 
                        (8, 'Brown', 'Martha', 'queenofsoul@meridian.net', '4255558989'), 
                        (9, 'Nelson', 'Nancy', 'nancyn@hotmail.com', '4255550101'), 
                        (10, 'Jones', 'Carolyn', 'sweetcarolyn@outlook.com', '2065555151'), 
                        (11, 'Frank', 'David', 'davudfrank@gmail.com', '2055558888')] 

    # QUERY TABLE
    cursor.executemany(person_insert_query, person_to_insert)
    connection.commit()
    print(cursor.rowcount, "Persons have been successfully loaded into Person table")

# CLEAN UP
except mysql.connector.Error as error: 
    print("Failed to load database and collect Persons data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()
