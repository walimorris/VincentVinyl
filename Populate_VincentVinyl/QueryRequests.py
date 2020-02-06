import mysql.connector 
from mysql.connector import Error 

try: 


    # ESTABLISH CONNECTION 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='') 

    # CREATE CURSOR
    cursor = connection.cursor()

    # CREATE QUERY 
    requests_insert_query = """INSERT INTO Request(idRequest, RequestDate, Person_idPerson, Employee_idEmployee, 
                                                   RequestDescription, Album_idAlbum)
                            VALUES(%s, %s, %s, %s, %s, %s) """

    # INSERT VALUES: SHOP DOESN'T CURRENTLY OWN REQUESTED ALBUM, THIS IS NULL
    albumValue = None
    requests_to_insert = (1, '2019-07-03', 10, 1, 'Dark Side of the Moon', albumValue)

    # EXECUTE QUERY 
    cursor.execute(requests_insert_query, requests_to_insert)
    connection.commit()
    print(cursor.rowcount, "Successfully loaded requests into Request table")

# CLEANUP
except mysql.connector.Error as error: 
    print("Failed to establish connection with database and load requests data{} ".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()


