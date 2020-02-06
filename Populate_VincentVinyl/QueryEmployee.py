import mysql.connector
from mysql.connector import Error

try: 


    # CREATE CONNECTION TO DATABASE
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='') # ADD PASSWORD

    # CREATE CURSOR 
    cursor = connection.cursor()

    # CREATE QUERY
    employee_insert_query = """INSERT INTO Employee(idEmployee, HireDate, Person_idPerson)
                            VALUES(%s, %s, %s) """

    # INSERT VALUES
    employee_to_insert = [(1, '2019-01-01', 12), # Jennifer Manning
                          (2, '2019-01-01', 13), # Brad Martin
                          (3, '2019-01-01', 14)] # Tina Deverson

    # EXECUTE QUERY 
    cursor.executemany(employee_insert_query, employee_to_insert)
    connection.commit()
    print(cursor.rowcount,"Employees have been successfully loaded into Employee table")

# CLEANUP
except mysql.connector.Error as error: 
    print("Failed to load database and collect Employee data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()

