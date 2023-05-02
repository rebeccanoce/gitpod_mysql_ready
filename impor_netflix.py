# save this as app.py
import mysql.connector
import pandas as pd

#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#Create the DB (if not already exists)
mycursor.execute("CREATE DATABASE IF NOT EXISTS NETFLIX_movies")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS NETFLIX_movies.show_id (
    show_id VARCHAR(30) NOT NULL,
    type VARCHAR(30),
    title VARCHAR(50),
    director VARCHAR(50),
    cast VARCHAR(1000),
    county VARCHAR(30),
    date VARCHAR(30),
    release_year VARCHAR(30),
    rating VARCHAR(30),
    duration VARCHAR(30),
    listed_in VARCHAR(30),
    PRIMARY KEY (show_id)
  );""")

#Delete data from the table Clsh_Unit
mycursor.execute("DELETE FROM NETFLIX_movies.show_id")
mydb.commit()

#Read data from a csv file
netflix_db = pd.read_csv('./Netflix.csv', index_col=False, delimiter = ',')
netflix_db = netflix_db.fillna('Null')
print(netflix_db.head(28))

#Fill the table
for i,row in netflix_db.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO NETFLIX_movies.show_id VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM NETFLIX_movies.show_id")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)