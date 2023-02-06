from sqlalchemy import Column, Integer, String
from .database import Base



class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
 


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)

#     blogs = relationship('Blog', back_populates="creator")
