import mysql.connector as c

conn = c.connect(host="localhost", user="root" , passwd="" , database = "movies")
if conn.is_connected():
    print("database is connected")
else:
    print("unable to connect to the datbase")

mycursor = conn.cursor()
create_db = "  Create table movies(id INT NOT NULL AUTO_INCREMENT , PRIMARY KEY(id) , title VARCHAR(100) NOT NULL , release_year VARCHAR(100) NOT NULL , genre VARCHAR(100) NOT NULL , collections VARCHAR(100) NOT NULL , rating_id INT NOT NULL)"
insert_into = "INSERT INTO movies (id , title , release_year , genre , collections , rating_id) VALUES(%s , %s, %s, %s, %s , %s)"
val = ("1" , "RRR" , "2022" , "fiction" , "1100 CR" , "1")

mycursor.execute(insert_into , val)


conn.commit()

print(mycursor.rowcount, "record inserted.")