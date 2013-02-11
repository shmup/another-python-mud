'''
Created on Nov 27, 2011

@author: Nich
'''
from model import Base, engine, Session, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

#TODO - Make inventory persistent 
class MBotData(Base):
    __tablename__ = "mbot_data"
    
    mbot_data_id = Column(Integer, primary_key=True)
    name = Column(String)
    location_x = Column(Integer)
    location_y = Column(Integer)
    account = Column(Integer, ForeignKey('accounts.account_id'))
    mbot_inventory = Column(Integer, ForeignKey('inventory.inventory_id'))
    #mbot_upgrades = relationship("PlayerUpgrades")
    
    
    
    
        



    
