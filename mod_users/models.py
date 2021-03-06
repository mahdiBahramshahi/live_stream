from sqlalchemy import Column ,Integer , String
from app import db
from werkzeug.security import generate_password_hash , check_password_hash

class User(db.Model):
    __tablename__='users'
    id = Column(Integer(), primary_key=True)
    showname= Column(String(128),nullable=False, unique=False)
    username = Column(String(128),nullable=False, unique=False)
    password = Column(String(128),nullable=False, unique=False)
    role = Column(Integer(),nullable=False, default=0)
    
    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password ,password)

    def is_admin(self):
        return self.role == 1