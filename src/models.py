import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Usuario
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    
    # Relacion favoritos
    favorites = relationship('Favorite', back_populates='user')

# Planeta
class Planet(Base):
    __tablename__ = 'planets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='planets')

# Personaje
class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='characters')

# Categoría
class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    
    planets = relationship('Planet', back_populates='category')
    characters = relationship('Character', back_populates='category')

# Favoritos
class Favorite(Base):
    __tablename__ = 'favorites'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
    
    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet')
    character = relationship('Character')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
