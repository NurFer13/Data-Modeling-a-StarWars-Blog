import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#TABLA DE PEOPLE,VEHICLES Y PLANETS,QUE PLANETS ESTE RELACIONADO CON PEOPLE,QUE VEHICLES ESTE RELACIONADO CON PEOPLE
# generar tablas
class People(Base): 
    __tablename__ = "people"
    id = Column(Integer, primary_key = True)
    gender = Column(String(6), unique = False, nullable = True)
    eye_color = Column(String(20), unique = False, nullable = True)
    height = Column(Integer, unique = False, nullable = False)
    age = Column (Integer, unique = False, nullable = False)
    name = Column(String(50), unique = True, nullable = False)
    #relacion 
    planet_id = Column(Integer,ForeignKey("planet.id"))
    homeworld = relationship("Planet", back_populates = "people")
    vehicle_id = Column(Integer,ForeignKey("vehicle.id"))
    vehicles = relationship("Vehicle", back_populates = "pilots")





class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key = True)
    terrain = Column (Integer, unique = False, nullable = True)
    name = Column(String(50), unique = True, nullable = False)
    diameter = Column(Integer, unique = False, nullable = True)
    population = Column(Integer, unique = False, nullable = True)
    people = relationship("People", back_populates = "homeworld")
    people_id = Column(Integer,ForeignKey("people.id"))

class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique = True, nullable = False)
    model = Column (String(50), unique = True, nullable = False)
    brand = Column (String(50), unique = False, nullable = False)
    pilots = relationship( "People", back_populates = "vehicles")
    pilot_id = Column(Integer,ForeignKey("people.id"))


#RELACIONES 





    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
