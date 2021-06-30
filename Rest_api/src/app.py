from flask import Flask, jsonify,request
from db import db
from User import *
app =Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://root:password@db/users"
db.init_app(app
)
#get request.curl -v http://localhost:5000/users
@app.route('/user')
def get_users():
    users=[user.json for user in User.find_all()]
    return jsonify(users)

#get userinfortion by id
#curl http://localhost:5000/users/1
@app.route('/user/<int:id>')
def get_user(id):
    user=User.find_by_id(id)
    if user:
        return jsonify(user.json)
    return f'User with {id} not found',404


#posting new userdata to the database
@app.route('/user',methods=['POST'])
def post_user():
    #retrieve user from request body
    request_user=request.json
    print(request_user['firstname'])

    #new_id=max([user['id'] for user in users])+1

    name=User.save_to_db(request_user['Firstname'])
    Surname=User.save_to_db(request_user['Surname'])
    Date_of_birth=User.save_to_db(request_user['Date-of-birth'])
    new_user = {
        {
            "Firstname": name,
            "Surname": Surname,
            "Date-of-birth": Date_of_birth
        }
    }


    return jsonify(new_user.json), 201
    

    #return the new user to the client

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")