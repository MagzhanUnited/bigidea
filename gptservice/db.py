import psycopg2
from app import app
from flask_sqlalchemy import SQLAlchemy
import bcrypt
db = SQLAlchemy(app)
class DB:
    def __init__(self) -> None:
        self.connection = None
    def make_connection(self):
        connection = psycopg2.connect(
            database="bigidea",
            user="postgres",
            password="magzhan2005",
            host="localhost",
            port="5432"
        )
        connection.autocommit = True
        self.connection = connection
        return self
    def get_cursor(self):
        return self.connection.cursor()
    

    
class UserDB(DB):
    def __init__(self, email, password, access_token) -> None:
        self.email = email
        self.password = password
        self.access_token = access_token
        super().__init__()
    def save_user(self):
        if not self.isUserExist():
            self.get_cursor().execute('INSERT INTO "user"(email, password, access_token) VALUES(%s, %s, %s)', (self.email, self.password, self.access_token))
            user = User(password=self.password, email=self.email, access_token=self.access_token)
            db.session.add(user)
            db.session.commit()
        return user

    def isUserExist(self):
        self.get_cursor().execute('SELECT id FROM "user" WHERE email = %s AND password = %s', (self.email, self.password))
        try: 
            return self.get_cursor().fetchone() is not None
        except:
            return False
    #for feature
    def hash_password(self):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), salt)
        return salt, hashed_password
        

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    access_token = db.Column(db.Text, nullable=False)
    # salt = db.Column(db.Text, nullable=False)
    # NOTE: In a real application make sure to properly hash and salt passwords
    # def check_password(self, password):
    #     return compare_digest(password, "password")