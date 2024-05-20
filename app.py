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

@app.route('/mons', methods=['GET'])
def get_mons():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM mons''')
    row_headers=[x[0] for x in cur.description]
    sql_data = cur.fetchall()
    cur.close()
    json_data = []
    for result in sql_data:
        json_data.append(dict(zip(row_headers,result)))
    return mons_table(json_data)

def mons_table(mons):
    heads = list(mons[0].keys())[1:]
    table = '<table><thead><tr>'
    for head in heads:
        table += f'<th>{head}</th>'
    table += '</tr></thead><tbody>'
    for mon in mons:
        table += '<tr>'
        for head in heads:
            table += f'<td>{mon[head]}</td>'
        table += '</tr>'
    table += '</tbody></table>'

    return table
    

if __name__ == '__main__':
    app.run(port=5001, debug=True)