from flask import Flask, jsonify,request
from db import *
from User import *


#get request.curl -v http://localhost:5000/users
@app.route('/user')
def get_users():
    return jsonify({'users':User_info.get_all_users()})

#posting new userdata to the database
@app.route('/user',methods=['POST'])
def post_user():
    #retrieve user from request body
    request_user=request.json
    User_info.add_user(request_user['Firstname'],request_user['Surname'],request_user['Date-of-birth'])
    return jsonify(request_user)
    

    #return the new user to the client

if __name__=='__main__':
    app.run(debug=True)