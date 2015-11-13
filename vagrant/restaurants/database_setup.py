#!/usr/bin/env python
#
# database_setup.py -- Initial configuration for the Restaurant Menus database.
#
import os
import sys
import psycopg2
from sqlalchemy import Column, ForeignKey, ForeignKeyConstraint, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)


class MenuItem(Base):
    __tablename__ = "menu_item"

    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    restaurant_id = Column(
        Integer,
        ForeignKey('restaurant.id', ondelete="CASCADE")
    )

    restaurant = relationship(
        Restaurant,
        cascade="all"
    )



engine = create_engine("postgresql+psycopg2:///restaurantmenus")

Base.metadata.create_all(engine)
