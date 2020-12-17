from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="dz67"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'

@app.route('/')
@app.route('/raspored')
def prva():
	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	res = mc.fetchall()
	mc.execute("SELECT DISTINCT nastavnik FROM raspored")
	a = mc.fetchall()
	mc.execute("SELECT DISTINCT vreme FROM raspored")
	b = mc.fetchall()


	return render_template("raspored.html",raspored=res,jed=a,jed2=b)

if __name__ == '__main__':
	app.run(debug=True)
