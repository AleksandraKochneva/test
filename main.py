from flask import Flask
from pymongo import MongoClient, errors

app = Flask(__name__)


@app.route('/')
def index():
    try:
        # Attempt to connect to MongoDB
        client = MongoClient("mongodb+srv://saleuzi4:PbKd7gLKT70VK0wD@cluster0.2mmbfbi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", serverSelectionTimeoutMS=1000)
        client.admin.command('ping')  # Check the connection
        message = "Successfully connected to MongoDB!"
    except errors.ServerSelectionTimeoutError:
        message = "Failed to connect to MongoDB."

    return f"<h1>{message}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
