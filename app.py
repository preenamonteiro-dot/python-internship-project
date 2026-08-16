from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
MONGO_URI ="mongodb+srv://portfolio_flask:WqGTfL3HHAXixXCu@cluster0.lemdfw8.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["portfolio"]
messages = db["messages"]

print("MongoDB connected successfully!")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    messages.insert_one({
        "name": name,
        "email": email,
        "message": message
    })

    return "Message received successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
