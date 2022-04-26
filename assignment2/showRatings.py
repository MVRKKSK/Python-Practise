import mysql.connector as c
conn = c.connect(host="localhost", user="root" , passwd="" , database="movies" )

cursor=conn.cursor()

query="SELECT movies.id,movies.title,review.first_name , review.rating FROM movies INNER JOIN review ON movies.rating_id=review.id "
cursor.execute(query)
rows=cursor.fetchall()
for x in rows:
   print(x)

conn.commit()