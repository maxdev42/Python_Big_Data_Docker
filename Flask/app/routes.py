from app import app
from flask import json as fJson

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Maxence"

@app.route('/book')
def book():
    with open('./books.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    print(file_data)
	#return json.dumps(file_data)
