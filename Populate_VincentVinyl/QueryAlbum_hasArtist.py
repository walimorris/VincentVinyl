import mysql.connector 
from mysql.connector import Error

try: 


    # ESTABLISH A CONNECTION 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root',
            password='') # Insert password 

    # CREATE CURSOR
    cursor = connection.cursor()

    # CREATE QUERY 
    albumHasArtist_insert_query = """INSERT INTO Album_has_Artist(Album_idAlbum, Artist_idArtist)
                             VALUES(%s, %s) """

    # Values for this table include Album id to Artist id
    albumid_artistid = [(1, 1), 
                        (2, 2), 
                        (3, 3), 
                        (4, 4), 
                        (5, 5), 
                        (6, 6)]

    # EXECUTE QUERY
    cursor.executemany(albumHasArtist_insert_query, albumid_artistid)
    connection.commit()
    print(cursor.rowcount,"albumId and artistId successfully updated into Album_has_artist table")

# CLEAN UP
except mysql.connector.Error as error: 
    print("Failed to load data for ablumId and artistId{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()


