import mysql.connector as c

conn = c.connect(host="localhost", user="root" , passwd="" , database="movies" )
if conn.is_connected():
    print("database is connected")
else:
    print("unable to connect to the datbase")

mycursor = conn.cursor()

create_db = "  Create table review(id INT NOT NULL AUTO_INCREMENT , PRIMARY KEY(id) , first_name VARCHAR(100) NOT NULL , last_name VARCHAR(100) NOT NULL , rating VARCHAR(100) NOT NULL)"
insert_into = "INSERT INTO review (id , first_name , last_name , rating) VALUES(%s , %s , %s , %s)"
val = ("1" , "Tejesh" ,  "Sabbavarapu", "5")

mycursor.execute(insert_into , val)

conn.commit()

print(mycursor.rowcount, "record inserted.")