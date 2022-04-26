insert_into = "INSERT INTO movies (id , title , release_year , genre , collections) VALUES(%s , %s, %s, %s, %s)"
val = ("1" , "RRR" , "2022" , "fiction" , "1100 CR")

mycursor.execute(insert_into , val)

conn.commit()

print(mycursor.rowcount, "record inserted.")