from pymongo.mongo_client import MongoClient
from flask import request,Flask,jsonify

uri = "mongodb+srv://auto123:auto123@cluster0.amvg1ng.mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__) 
# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection

client.admin.command('ping')
db = client["students"]
collection = db["std_info"]

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students",methods=["GET"])
def get_all_books():
    data = list(collection.find())
    return jsonify({data})

@app.route("/students/<int>:std_id>" , methods = ["GET"])
def get_students(std_id):
    std_Id = collection.find_one({"_id" : str(std_id) })
    if not std_Id:
        return jsonify({"error" :"Student not found"}),404
    return jsonify({std_Id})

