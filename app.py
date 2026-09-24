import mysql.connector
from flask import Flask,render_template,request

app =Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Naveen@5559",
    database="food_ordering"
)

@app.route("/")
def food():
    cursor =db.cursor()
    cursor.execute("SELECT* FROM foods")
    data = cursor.fetchall()
    cursor.close()
    return render_template("foods.html",foods=data)

@app.route("/add")
def add():
    pass

@app.route("/edit")
def edit_food():
    pass

@app.route("/delete")
def delete_food():
    pass

if __name__== "__main__":
    app.run(debug=True)