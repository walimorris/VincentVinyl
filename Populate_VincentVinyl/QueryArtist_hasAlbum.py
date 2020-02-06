import mysql.connector
from mysql.connector import Error

try:


    # ESTABLISH A CONNECTION 
    connection = mysql.connector.connect(
            host='localhost',
            database='VincentVinyl',
            user='root',
            password='')

    # CREATE CURSOR
    cursor = connection.cursor()

    # CREATE QUERY 
    artistHasAlbum_insert_query = """INSERT INTO Artist_has_Album(Artist_idArtist, Album_idAlbum)
                             VALUES(%s, %s) """

    # Values for this table include Artist id to Album id
    # Artist - Album Id: (1, 1) have been added prior to this script
    artistid_albumid = [(2, 2),
                        (3, 3),
                        (4, 4),
                        (5, 5),
                        (6, 6)]

    # EXECUTE QUERY
    cursor.executemany(artistHasAlbum_insert_query, artistid_albumid)
    connection.commit()
    print(cursor.rowcount,"artist Id and album Id successfully updated into Artist_has_Album table")

# CLEAN UP
except mysql.connector.Error as error:
    print("Failed to load data for artistId and albumId{}".format(error))
    if(connection.is_connected()):
        cursor.close()
        connection.close()


