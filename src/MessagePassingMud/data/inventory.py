'''
Created on Jul 8, 2012

@author: Nich
'''

from model import Base, engine, Session, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Inventory(Base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True, nullable=False,)
    mbot_id = Column(Integer, ForeignKey('mbot_data.id'))
    item_id = Column(Integer)