import os

from flask import Flask
from pymongo import MongoClient, errors

app = Flask(__name__)

app.secret_key = 'supersecretkey'

m_string = os.getenv('m_string')
# m_string = "mongodb+srv://saleuzi4:PbKd7gLKT70VK0wD@cluster0.2mmbfbi.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
@app.route('/')
def index():
    try:
        print(f"MongoDB Connection String: {m_string}")  # Debug output
        client = MongoClient(m_string, serverSelectionTimeoutMS=1000)
        client.admin.command('ping')  # Check the connection
        message = f"Successfully connected to MongoDB with {m_string}!"
    except errors.ServerSelectionTimeoutError:
        message = f"Failed to connect to MongoDB with {m_string}."

    return f"<h1>{message}</h1>"



if __name__ == '__main__':
    app.run(debug=True)
