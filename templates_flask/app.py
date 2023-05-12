from flask import render_template
from flask import Flask

import mysql.connector



#Connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="NETFLIX"
)
mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/shows')
def showList():
   mycursor.execute("SELECT * FROM NETFLIX.MOVIES_SHOWS")
   myresult = mycursor.fetchall()
   return render_template('netflix_shows.html', shows=myresult)
