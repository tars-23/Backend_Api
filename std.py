from pymongo.mongo_client import MongoClient
from flask import request,Flask,jsonify
from flask_basicauth import BasicAuth

uri = "mongodb+srv://auto123:auto123@cluster0.amvg1ng.mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__) 
app.config['BASIC_AUTH_USERNAME']='somsri'
app.config['BASIC_AUTH_PASSWORD']='sudsoy'
basic_auth = BasicAuth(app)
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


@app.route("/students",methods=["POST"])
@basic_auth.required
def create_newstudent():
    data = request.get_json()
    id = collection.find_one({"_id" : data.get("_id")})
    if not id:
        return jsonify({"error" :"Cannot create new student"}),500
    collection.insert_one(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)