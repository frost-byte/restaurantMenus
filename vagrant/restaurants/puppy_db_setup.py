#!/usr/bin/env python
#
# puppy_db_setup.py -- Problem Set 1
#
import os
import sys
import psycopg2
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Many to Many relationship between Puppy and Adopter
association_table = Table('association', Base.metadata,
                         Column('puppy_id', Integer, ForeignKey('puppy.id')),
                         Column('adopter_id', Integer, ForeignKey('adopter.id'))
                         )


class Shelter(Base):
    __tablename__ = "shelter"

    name = Column(String(80), nullable = False)
    address = Column(String(250), nullable = False)
    city = Column(String(250), nullable = False)
    state = Column(String(50), nullable = False)
    zipCode = Column(String(5), nullable = False)
    website = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key = True)
    puppy_id = Column(Integer, ForeignKey('puppy.id'))
    picture = Column(String)
    description = Column(String)
    specialNeeds = Column(String)
    name = Column(String(250), nullable = False)
    gender = Column(String(6))
    dateOfBirth = Column(Date)
    weight = Column(Numeric(10))


class Puppy(Base):
    __tablename__ = "puppy"
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)
    profile = relationship("Profile", backref="puppy", uselist=False)
    id = Column(Integer, primary_key = True)
    adopters = relationship("Adopter",
                            secondary = association_table,
                            backref = "puppies")


class Adopter(Base):
    __tablename__ = "adopter"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)


engine = create_engine("sqlite:///puppies.db")

Base.metadata.create_all(engine)
