import os

from flask import Flask
from pymongo import MongoClient, errors

app = Flask(__name__)

app.secret_key = 'supersecretkey'

m_string = os.getenv('m_string')

@app.route('/')
def index():
    try:
        # Attempt to connect to MongoDB
        client = MongoClient(m_string, serverSelectionTimeoutMS=1000)
        client.admin.command('ping')  # Check the connection
        message = "Successfully connected to MongoDB!"
    except errors.ServerSelectionTimeoutError:
        message = "Failed to connect to MongoDB."

    return f"<h1>{message}</h1>"


if __name__ == '__main__':
    app.run(debug=True)
