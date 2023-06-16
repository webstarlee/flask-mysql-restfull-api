from db import db, Column, Integer, String, relationship

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(80))
    last_name = Column(String(80))
    username = Column(String(80), unique=True)
    password = Column(String(250))
    profile = relationship("Profile", back_populates="user")