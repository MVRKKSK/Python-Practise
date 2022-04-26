import mysql.connector as c

conn = c.connect(host="localhost", user="root" , passwd="Mvrk@4599" , database = "movies")
if conn.is_connected():
    print("database is connected")
else:
    print("unable to connect to the datbase")

mycursor = conn.cursor()
create_db = "  Create table movies(movie_id INT NOT NULL AUTO_INCREMENT , PRIMARY KEY(movie_id) , movie_name VARCHAR(100) NOT NULL)"

insert_into = "INSERT INTO movies (movie_id , movie_name) VALUES(%s , %s)"
val = ("1" , "bahubali")
""" show_db = "show databases" """
mycursor.execute(insert_into , val)

conn.commit()

print(mycursor.rowcount, "record inserted.")
