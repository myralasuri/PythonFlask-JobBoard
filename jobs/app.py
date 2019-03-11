import sqlite3
from flask import Flask,g , render_template

PATH = 'db/jobs.sqlite'

app = Flask(__name__)


def open_connection():
    connection =None
    connection = getattr(g, '_connection', default=None)
    if connection == None :
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values = (), commit =False, single =False):
    connection = open_connection()
    cursor =connection.execute(sql, values)
    results =None
    if commit :
        results = connection.commit()
    else:
        results = cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results
@app.teardown_appcontext
def close_connection(exception ):
    connection = getattr(g, '_connection', None)
    if connection is not None:
        connection.close()








@app.route('/')
@app.route('/jobs',methods = ['get'])
def jobs():
    #return 'Hello World!'
    return render_template('index.html')

# app.run(port='5000')

