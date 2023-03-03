import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="ANIMALI"
)
mycursor=mydb.cursor()
sql="INSERT INTO Mammiferi (nome_proprio, razza, Peso, Eta) VALUES (%s, %s, %s, %s )"
val= [
    ("Capibara", "RODITORE", 5, 60),
    ("Zebra", "zebra", 80, 10),
    ("Lince", "babbo", 756, 88),
    ("Cervo", "hcfhki", 764, 99),
    ("Coniglio","bnhjj", 64, 77)
]

mycursor.executemany (sql, val)
mydb.commit()