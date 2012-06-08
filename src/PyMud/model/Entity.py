'''
Created on Nov 25, 2011

@author: Nich
'''
from sqlalchemy import Column, Integer, String
from model import Base



class Entity(Base):
    
    __tablename__ = "entities"
    
    id = Column(Integer, primary_key = True)
    friendly_desc = Column(String)
    
    def __init__(self, friendly_desc):
        self.friendly_desc = friendly_desc
        


        

