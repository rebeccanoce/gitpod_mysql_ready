import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id VARCHAR(255), nome_proprio VARCHAR(255), razza VARCHART(255), Peso(255), Età(255))")
