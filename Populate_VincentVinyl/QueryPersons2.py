import mysql.connector 
from mysql.connector import Error 

""" This file includes the three Employees from sample data into 
the Persons Table
"""

try: 



    # CONNECT TO DATABASE
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='') # ADD PASSWORD

    # CONNECT CURSOR
    cursor = connection.cursor()

    # CREATE QUERY 
    insert_into_person = """INSERT INTO Person(idPerson, PersonLastName, PersonFirstName, 
                                               PersonEmail, PersonPhone)
                         VALUES(%s, %s, %s, %s, %s) """ 

    # INSERT VALUES: THREE EMPLOYEES
    person_to_insert = [(12, 'Manning', 'Jennifer', 'jmanning@msn.com', '4255551111'), 
                        (13, 'Martin', 'Brad', 'bradmartin34@gmail.com', '4255552222'), 
                        (14, 'Deverson', 'Tina', 'tinad@newcity.com', '4255553333')]

    # EXECUTE QUERY 
    cursor.executemany(insert_into_person, person_to_insert)
    connection.commit()
    print(cursor.rowcount, "Persons have been successfully loaded into Persons table")

# CLEANUP 
except mysql.connector.Error as error: 
    print("Failed to load database and collect Persons data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()
