from flask import render_template
from flask import Flask


app = Flask(__name__)


@app.route('/shows')
def showList():
   mycursor.execute("SELECT * FROM netflix_shows")
   myresult = mycursor.fetchall()
    return render_template('netflix_shows.html', shows=myresult)
