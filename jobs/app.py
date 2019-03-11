from flask import Flask
import sys
from flask import render_template
app = Flask(__name__)

@app.route('/')
@app.route('/jobs',methods = ['get'])
def jobs():
    #return 'Hello World!'
    return render_template('index.html')

# app.run(port='5000')

