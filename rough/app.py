from flask import Flask, jsonify, request, Response, session
from flask_cors import CORS
import os
import time
import base64
from pymongo import MongoClient


app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

client = MongoClient('localhost', 27017)
db = client['rough']

def event_stream():
	while(request.cookies.get("id") == ""):
		print("*")
	print(request.cookies.get("id"))


@app.route('/')
def hello():
	# resp = Response()
	# resp.set_cookie("name", "")
	# resp.set_cookie("id", "")
	# resp.set_data("Hello")
	# return resp
	event_stream()
	return "Hello"

@app.route('/login1')
def login1():

	# time.sleep(10)
	# session['userId'] = 123 
	# return "Shahid Ikram logged in"

	resp = Response()
	resp.set_cookie("name", "Shahid Ikram")
	resp.set_cookie("id", "1")
	resp.set_data("Shahid Ikram logged in")
	return resp

	

@app.route('/login2')
def login2():

	# time.sleep(5)
	# session['userId'] = 789 
	# return "Tayeb Mohamed logged in"

	resp = Response()
	resp.set_cookie("name", "Tayeb Mohamed")
	resp.set_cookie("id", "2")
	resp.set_data("Tayeb Mohamed logged in")
	return resp

@app.route("/logout")
def logout():

	resp = Response()
	resp.set_cookie("name", "")
	resp.set_cookie("id", "")
	resp.set_data("Logged out")
	return resp

@app.route('/login3')
def login3():

	# time.sleep(5)
	# session['userId'] = 789 
	# return "Tayeb Mohamed logged in"

	resp = Response()
	resp.set_cookie("name", "Frodo Baggins")
	resp.set_cookie("id", "3")
	resp.set_data("Frodo Baggins logged in")
	return resp

@app.route('/login4')
def login4():

	# time.sleep(5)
	# session['userId'] = 789 
	# return "Tayeb Mohamed logged in"

	resp = Response()
	resp.set_cookie("name", "Samwise Billings")
	resp.set_cookie("id", "4")
	resp.set_data("Samwise Billings logged in")
	return resp

@app.route("/dosmth")
def dosmth():
	_name = request.cookies.get("name")
	_id = request.cookies.get("id")
	try:
		return _name + " " + _id
	except:
		return "First Log in"

	# return str(session['userId'])

@app.route("/save", methods=["POST"])
def save():
	# print(list(request.form.keys()))
	image = request.form['imgBase64'].split(",")[1]
	imgdata = base64.b64decode(image)
	
	# print(image.split(","))
	with open("imageToSave.png", "wb") as fh:
		fh.write(imgdata)
	return ""

@app.route("/mongo")
def mongo():
	collection = db['users']
	# s = "abcdefgh"
	# x = collection.find_one({'name': s.encode()})
	
	# print(x['name'].decode())
	'''
	s = "abcdefgh"
	d = {'name': s.encode(), 'age': 25}

	collection.insert_one(d)
	print("inserted: ", d)
	'''
	'''
	s = "qwertyuiop"
	d = {'name': s, 'flag': False}
	collection.insert_one(d)
	print("inserted: ", d)
	'''
	s = "qwertyuiop"
	x = collection.find_one({'name': s})
	
	print(x['flag'] == False)
	return ""

@app.route("/update")
def update():
	collection = db['users']

	updated_dict = { "11/05/2018" : { "15:30" : "patient01", "18:00" : "patient02" } }

	collection.update_one(
		{"_id": "doc1"}, 
		{"$set": {'appointments': updated_dict}}, 
		upsert=False)

	return "update mofo!"	

if __name__ == '__main__':
	app.run(host="0.0.0.0", port = 5001, debug = True, threaded = True)
