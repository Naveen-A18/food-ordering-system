import mysql.connector
from flask import Flask,render_template,request

app =Flask(__name__)
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="food_ordering",
    )
if __name__== "__main__":
    app.run(debug=True)