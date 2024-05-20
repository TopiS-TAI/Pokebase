from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'pokemon'
app.config['MYSQL_USER'] = 'poke'
app.config['MYSQL_PASSWORD'] = 'man'

mysql = MySQL(app)

@app.route('/')
def home():
    with open('./templates/home.html') as f:
        data = f.read()
    return data

if __name__ == '__main__':
    app.run(port=5001, debug=True)