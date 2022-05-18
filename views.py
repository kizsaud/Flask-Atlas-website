import pymongo
from bson.json_util import dumps
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://root:toor@cluster0.cx5wq.mongodb.net/?retryWrites=true&w=majority")
db =cluster["HTML"]
collection = db["NAME/PHONENUMBER/EMAIL"]
db=cluster["logs"]
collection2 = db["logs for data"]
from codecs import namereplace_errors
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def setdata():
    

    return render_template("index.html")


@app.route("/", methods=['POST'])
def getdata():
    name=request.form["Name"]
    email=request.form["email"]
    phone=request.form["phone"]
    passdata(name,email,phone)
    return render_template("pass.html", n=name, e=email,p= phone)

      
@app.route("/", methods=['POST','GET'])
def passdata(name,email,phone):
    post = { "name": name, "email": email, "phone": phone}
    collection.insert_one(post)
    file=open("logs.txt", 'w')
    x=collection.find()
    for data in x:
        print(data, file=file)
        print(data)



if __name__ =='__main__':
    app.run(debug=True)
    
