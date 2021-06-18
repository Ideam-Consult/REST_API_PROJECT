
# importing Flask and other modules
from flask import Flask, request, render_template

# import the connect library from psycopg2

app = Flask(__name__)


@app.route('/')
def Info():
	return render_template("User_info.html")

@app.route('/',methods=["POST"])
def getvalues():
	name=request.form['FirstName']
	surname=request.form['Surname']
	db=request.form['Dateofbirth']
	print(name)
	
# Flask constructor 
	return render_template('User_output.html',n=name,s=surname,d=db)
		


if __name__=='__main__':
    app.run(debug=True)
