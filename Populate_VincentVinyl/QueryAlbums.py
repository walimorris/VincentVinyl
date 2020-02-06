import mysql.connector # import MySql connector API
from mysql.connector import Error # used to show connection errors

try:
    """ Using this method to connect to MySQL database. This method accepts four 
    required parameters: Host, Database, User and Password. The connect method 
    establishes a connection to the database and returns a MySQLConnection object
    which allows performance operations on the database. 
    """
    connection = mysql.connector.connect(
            host='localhost',
            database='VincentVinyl',
            user='root',
            password='Kentstate8$$')
    
    # Create cursor 
    cursor = connection.cursor()

    # INSERT QUERY
    albums_insert_query = """INSERT INTO Album(IdAlbum, Title, Studio, Year)
                          VALUES(%s, %s, %s, %s) """
    # RECORDS
    # Abby Road's Album has already been added to database prior to this query
    albums_to_insert = [(2, 'Blonde on Blonde', 'Columbia Records' , 1967), 
                        (3, 'Riding with the King', 'Columbia Records', 2015), 
                        (4, 'Pure Heroine', 'Universal', 2017), 
                        (5, 'Breaking it up, breaking it down', 'Columbia Records', 1983), 
                        (6, 'Glassworks', 'Atlantic', 1994)]

    #EXECUTE QUERY
    cursor.executemany(albums_insert_query, albums_to_insert)
    connection.commit()
    print(cursor.rowcount, "Albums successfully inserted into Albums table")


# CLEAN UP
except mysql.connector.Error as error:
    print("Failed to collect Album data".format(error))
finally:
    if(connection.is_connected()):
        # close cursor
        cursor.close()  
        # close mysql connection 
        connection.close()
        print("MySQL connection is closed")

