from flask import Flask, jsonify, request, Response, session
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_DB'] = 'pokemon'
app.config['MYSQL_USER'] = 'poke'
app.config['MYSQL_PASSWORD'] = 'man'
app.secret_key = 'verysecret'

mysql = MySQL(app)

@app.route('/')
def home():
    if not ('types' in list(session.keys())):
        session['types'] = get_types()
    type_options = create_type_options(session.get('types', None))
    with open('./templates/home.html', encoding="utf-8  ") as f:
        data = f.read()
    return data.format(type_options=type_options)

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

@app.route('/mons', methods=['POST'])
def create_mon():
    name = request.form.get('name')
    hp = request.form.get('hp')
    attack = request.form.get('attack')
    defense = request.form.get('defense')
    s_attack = request.form.get('s_attack')
    s_defense = request.form.get('s_defense')
    speed = request.form.get('speed')
    type1 = request.form.get('type1')
    type2 = request.form.get('type2')
    if type2 == '':
        type2 = None
    
    cur = mysql.connection.cursor()
    cur.execute('''INSERT INTO mons (name, hp, attack, defense, s_attack, s_defense, speed, type1, type2) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)''', (name, hp, attack, defense, s_attack, s_defense, speed, type1, type2))
    mysql.connection.commit()
    cur.close()
    return Response(status=200)

def mons_table(mons):
    heads = list(mons[0].keys())[1:]
    types = session.get('types', None)
    table = '<table><thead><tr>'
    for head in heads:
        table += f'<th>{head}</th>'
    table += '</tr></thead><tbody>'
    for mon in mons:
        table += '<tr>'
        for head in heads:
            if head[:-1] == 'type':
                type_name = next((type['name'] for type in types if type['id'] == mon[head]), None)
                table += f'<td>{type_name}</td>'
            else:
                table += f'<td>{mon[head]}</td>'
        table += '</tr>'
    table += '</tbody></table>'

    return table

def create_type_options(types):
    options = ''
    for type in types:
        options += f'<option value="{type["id"]}">{type["name"]}</option>'
    return options

def get_types():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM types''')
    row_headers=[x[0] for x in cur.description]
    sql_data = cur.fetchall()
    cur.close()

    json_data = []
    for result in sql_data:
        json_data.append(dict(zip(row_headers, result)))

    return json_data


if __name__ == '__main__':
    app.run(port=5001, debug=True)