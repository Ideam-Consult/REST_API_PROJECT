from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from db import app
db = SQLAlchemy(app)

class User_info(db.Model):
    __tablename__='users'
    firstname=db.Column(db.String(128),primary_key=True)
    surname=db.Column(db.String(128))
    Dateofbirth=db.Column(db.String(50))

    
    def add_user(_firstname,_surname,_Dateofbirth):
        new_user=User_info(firstname=_firstname,surname=_surname,Dateofbirth=_Dateofbirth)
        db.session.add(new_user)
        db.session.commit()
    def json(self):
        return {
            "Firstname":self.firstname,
            "Surname":self.surname,
            "Date_of_birth":self.Dateofbirth
        }

    def get_all_users():
        return [User_info.json(user) for user in User_info.query.all()] 

    def __repr__(self):
        User_object={
            "Firstname":self.firstname,
            "Surname":self.surname,
            "Date_of_birth":self.Dateofbirth
        }
        return json.dumps(User_object)
