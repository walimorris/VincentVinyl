import mysql.connector
from mysql.connector import Error

try: 


    # CREATE DATABASE CONNECTION 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='Kentstate8$$') 

    # BUILD CURSOR
    cursor = connection.cursor()

    # CREATE QUERY 
    genre_insert_query = """INSERT INTO Genre(idGenre, GenreName)
                         VALUES(%s, %s) """

    #INSERT ID VALUES/GENRES
    genre_to_insert = [(1, 'Rock/Pop'), 
                       (2, 'Blues'), 
                       (3, 'Pop/HipHop'), 
                       (4, 'Classical')]

    # EXECUTE QUERY
    cursor.executemany(genre_insert_query, genre_to_insert)
    connection.commit()
    print(cursor.rowcount, "Genres have been successfully loaded into Genre table")

# CLEAN UP
except mysql.connector.Error as error: 
    print("Failed to load database and collect genre data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()




