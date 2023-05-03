import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
now = datetime.now()

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    current_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    """ current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time) """
 
 
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(80))
    description = Column(String(250))
    name = Column(String(200), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    url = Column(String(200), unique=True, nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    gender = Column(String(60))
    url = Column(String(200), unique=True, nullable=False)
 
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id') )
    characters_id = Column(Integer, ForeignKey('characters.id'))



def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
