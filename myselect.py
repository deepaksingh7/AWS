import mysql.connector

db_host = 'flipbasket.cihbxyzcwmv9.us-west-2.rds.amazonaws.com'
db_username = 'root';
db_password = 'password'
database = 'world'

# simple routine to run a query on a database and print the results

def getCountry():
  print "\n -------------------------- -------------------------- \n "
  conn = mysql.connector.connect(host=db_host, user=db_username, passwd=db_password, db=database)
  cur = conn.cursor()
  cur.execute("select * from country where name='india'")
  myresult = cur.fetchall()
  for x in myresult:
    print(x)
    print "\n -------------------------- -------------------------- \n "
  cur.close()
  conn.close()


 def main():
     getCountry()

main()
