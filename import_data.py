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
mycursor.execute("CREATE DATABASE IF NOT EXISTS NETFLIX")

mycursor.execute("DROP TABLE  IF EXISTS NETFLIX.MOVIES_SHOWS ")

#Create the table for the csv data (if not exists)
mycursor.execute("""
  CREATE TABLE IF NOT EXISTS NETFLIX.MOVIES_SHOWS (
    show_id VARCHAR(30) NOT NULL,
    type VARCHAR(30),
    title TEXT,
    director VARCHAR(50),
    cast VARCHAR(10000),
    country TEXT,
    date_added VARCHAR(30),
    release_year INTEGER,
    rating VARCHAR(30),
    duration VARCHAR(30),
    listed_in TEXT,
    description TEXT,
    PRIMARY KEY (show_id)
  );""")

#Delete data from the table Clsh_Unit
mydb.commit()

#Read data from a csv file
netflix_data = pd.read_csv('./cr-unit-attributes.csv', index_col=False, delimiter = ',')
netflix_data = netflix_data.fillna('Null')
print(netflix_data.head(20))

#Fill the table
for i,row in netflix_data.iterrows():
    cursor = mydb.cursor()
    #here %S means string values 
    sql = "INSERT INTO NETFLIX.MOVIES_SHOWS VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, tuple(row))
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()

#Check if the table has been filled
mycursor.execute("SELECT * FROM NETFLIX.MOVIES_SHOWS")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)