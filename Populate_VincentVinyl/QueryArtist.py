import mysql.connector
from mysql.connector import Error

try: 

    # ESTABLISH A Connection 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root',
            password='Kentstate8$$')

    # CREATE CURSOR
    cursor = connection.cursor()

    # CREATE QUERY
    artist_insert_query = """INSERT INTO Artist(idArtist, ArtistName)
                          VALUES(%s, %s) """

    # Insert artist
    # ArtistId 1: Beatles has already been inserted into table
    artist_to_insert = [(2, 'Bob Dylan'),
                        (3, 'BB King'), 
                        (4, 'Lorde'), 
                        (5, 'Johnny Winter'), 
                        (6, 'Phillip Glass')]

    #Execute Query
    cursor.executemany(artist_insert_query, artist_to_insert)
    connection.commit()
    print(cursor.rowcount, "Artists successfully updated into Artist table")

# CLEAN UP 
except mysql.connector.Error as error:
    print("Failed to load database and collect Artist data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()




    


