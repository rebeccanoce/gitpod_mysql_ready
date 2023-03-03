import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)
mycursor=mybd.cursor()
sql="INSERT INTO Mammiferi (nome.proprio) VALUES (%s)"
val= [
    ("Capibara"),
    ("Zebra"),
    ("Lince"),
    ("Cervo"),
    ("Coniglio")
]

mycursor.executemany (sql, val)
mybd.commit()