import mysql.connector 
from mysql.connector import Error 

try: 


    # ESTABLISH CONNECTION TO DATABASE 
    connection = mysql.connector.connect(
            host='localhost', 
            database='VincentVinyl', 
            user='root', 
            password='Kentstate8$$') 

    # CREATE CURSOR
    cursor = connection.cursor()

    # CREATE QUERY
    insert_into_genreHasAlbum = """INSERT INTO Genre_has_Album(Genre_idGenre, Album_idAlbum)
                                VALUES(%s, %s) """

    # VALUES TO INSERT
    genresAlbums_to_insert = [(1, 1), 
                              (1, 2), 
                              (2, 3), 
                              (2, 5), 
                              (3, 4), 
                              (4, 6)] 

    # EXECUTE QUERY 
    cursor.executemany(insert_into_genreHasAlbum, genresAlbums_to_insert)
    connection.commit()
    print(cursor.rowcount, "Successfully added albums to genres in Genre_has_Album table")

# CLEAN UP
except mysql.connector.Error as error: 
    print("Failed to connect to database and load Genre_hasAlbum data{}".format(error))
    if(connection.is_connected()): 
        cursor.close()
        connection.close()
