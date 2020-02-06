import mysql.connector 
from mysql.connector import Error

try: 



    # CONNECT TO DATABASE 
    connection = mysql.connector.connect( 
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='') # ADD PASSWORD 

    # BUILD CURSOR 
    cursor = connection.cursor()

    # CREATE QUERY
    album_hasGenre_query = """INSERT INTO Album_has_Genre(Album_idAlbum, Genre_idGenre)
                           VALUES(%s, %s)"""

    # INSERT ALBUM ID/ GENRE ID
    album_genre_insert = [(1, 1),
                          (2, 1),
                          (3, 2),
                          (4, 3),
                          (5, 2),
                          (6, 4)]

    # QUERY TABLE 
    cursor.executemany(album_hasGenre_query, album_genre_insert)
    connection.commit()
    print(cursor.rowcount, "Albums and Genres have been successfully loaded into Album_has_Genre Table")

# CLEAN UP
except mysql.connector.Error as error: 
    print("Failed to load database and collect Album and genre data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()

