import os
import sys
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
# now = datetime.now()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False)
    last_name = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    password = Column(String(200), nullable=False)
    user_name = Column(String(200), nullable=False)
    current_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time =", current_time)


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    climate = Column(String(80))
    description = Column(String(250))
    diameter = Column(Integer)
    name = Column(String(80))
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    terrain = Column(Integer)
    url = Column(String(200), unique=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    gender = Column(String(60))
    mass = Column(Integer)
    name = Column(String(60))
    url = Column(String(200), unique=True)


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))


def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
