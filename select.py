import mysql.connector

mydb = mysql.connector.connect(
  host="flipbasket.cihbxyzcwmv9.us-west-2.rds.amazonaws.com",
  user="root",
  passwd="password",
  database="world"
)

mycursor = mydb.cursor()

mycursor.execute("select * from country where name='india'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
