
# importing Flask and other modules
from flask import Flask, request, jsonify
import json

# import the connect library from psycopg2

app = Flask(__name__)


@app.route('/',methods=["GET"])
def test():
	x = {
	"name": "John",
	"age": 30,
	"city": "New York"
	}

	# convert into JSON:
	response = json.dumps(x)
	return response

@app.route('/test',methods=["GET"])
def test2():
	x = {
	"Message": "YAY",
	}

	# convert into JSON:
	response = json.dumps(x)
	return response

@app.route('/',methods=["POST"])
def getvalues():
	data = request.json
	print(data)
	return jsonify(data)
	

if __name__=='__main__':
    app.run(debug=True)


# add
# Add