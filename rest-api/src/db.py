from flask import  Flask
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://rest:pass@localhost:5432/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False