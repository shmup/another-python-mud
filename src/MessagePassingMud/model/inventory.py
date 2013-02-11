'''
Created on 2013-02-10

@author: Nich
'''
from model import Base, engine, Session, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

#TODO - Make inventory persistent 
class Inventory(Base):
    __tablename__ = "inventory"
    inventory_id = Column(Integer, primary_key=True)
    mbot_data = relationship("MBotData")
    
    
class InventoryItem(Base):
    __tablename__ = "inventory_item"
    inventory_id = Column(Integer, primary_key=True)
    item_id = Column(Integer, primary_key=True)
    count = Column(Integer)
    
class Item(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True)
    item_name = Column(String)