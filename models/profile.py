from db import db, Column, Integer, String, relationship

class Profile(db.Model):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    avatar = Column(String(80))
    address = Column(String(80))
    user_id = Column(Integer)
    user = relationship("User", back_populates="profile")