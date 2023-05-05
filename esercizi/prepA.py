import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id INT AUTO_INCREMENT PRIMARY KEY, nome_proprio VARCHAR(255), razza VARCHAR(255), Peso INT, Eta INT)")
