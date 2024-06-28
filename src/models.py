import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_de_subcripcion = Column(Date, nullable=False)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Login(Base):
    __tablename__ = 'login'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    fecha_login= Column(Date, nullable=False)
    user_id = Column(Integer, ForeignKey('usuario.id'))

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    color_de_ojos = Column(String(250), nullable=False)
    color_de_cabello = Column(String(250), nullable=False)

class Favorito_Personaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
   

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    diametro = Column(String(250), nullable=False)
    poblacion = Column(String(250), nullable=False)

class Favorito_Planeta(Base):
    __tablename__ = 'favorito_planeta'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))

class Vehiculo(Base):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    modelo = Column(String(250), nullable=False)
    capacidad_pasajeros = Column(String(250), nullable=False)

class Favorito_Vehiculo(Base):
    __tablename__ = 'favorito_vehiculo'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuario.id'))
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'))

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
