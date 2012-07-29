'''
Created on Nov 27, 2011

@author: Nich
'''
from model import Base, engine, Session, ForeignKey
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class MBotData(Base):
    __tablename__ = "mbot_data"
    
    mbot_data_id = Column(Integer, primary_key=True)
    name = Column(String)
    location_x = Column(Integer)
    location_y = Column(Integer)
    account = Column(Integer, ForeignKey('account.id'))
    mbot_inventory = relationship("Inventory")
    #mbot_upgrades = relationship("PlayerUpgrades")
    
    
    
    
        



    
