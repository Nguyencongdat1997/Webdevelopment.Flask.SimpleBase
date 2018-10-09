import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# class MenuItem(Base):
#     __tablename__ = 'menu_item'

#     name = Column(String(80), nullable=False)
#     id = Column(Integer, primary_key=True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)


class Account(Base):
    __tablename__ = 'account'

    account = Column(String(80), nullable=False, primary_key=True)
    password = Column(String(80), nullable=False)
    role = Column(String(80))
    

engine = create_engine('sqlite:///flaskserverbase.db')


Base.metadata.create_all(engine)
