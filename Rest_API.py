# importing Flask and other modules
from flask import Flask, request, jsonify
import json
# importing from the databaseConnection script and modules
from databaseConnection import *  

app = Flask(__name__)


# get method to return user's infomation
@app.route('/', methods=["GET"])
def test():
    x = {
        "Firstname": "xxxx",
        "Surname": "xxxx",
        "Date of birth": "xxxxx"
    }

    # convert into JSON:
    response = json.dumps(x)
    return response


# Posting user infor to the server/database
@app.route('/info', methods=["POST"])
def getvalues():
    data = request.json

    firstname = data["Firstname"]
    surname = data["Surname"]
    dateofbirth = data["Date of birth"]
    # inserting the first name,surname and date of birth into the database
    cursor.execute('INSERT INTO Userinfo (FIRST_NAME,SURNAME,Date_of_birth) values(%s,%s,%s)',
                   (
                       firstname, surname, dateofbirth
                   ))
    conn.commit()
    print("success")
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
