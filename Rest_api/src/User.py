from db import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String(128))
    surname=db.Column(db.String(128))
    Dateofbith=db.Column(db.String(50))

    def __init__(self,id,firstname,surname,Dateofbirth):
        self.id=id
        self.firstname=firstname
        self.surname=surname
        self.Dateofbith=Dateofbirth

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.get(_id)

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit() 
    

    @property
    def json(self):
        return{
            "id":self.id,
            "Firstname":self.firstname,
            "Surname":self.surname,
            "Date_of_birth":self.Dateofbith
        }