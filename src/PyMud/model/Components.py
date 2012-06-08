'''
Created on Nov 25, 2011

@author: Nich
'''
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey
from model import Base




class Components(Base):
    __tablename__ = "components"
    component_id = Column(Integer, primarykey=True)
    official_name = Column(String)
    friendly_desc = Column(String)
    table = Column(String)
    

class EntityComponent(Base):
    __tablename__ = "entity_components"
    entity_id = Column(Integer, ForeignKey("entities.id"))
    component_id = Column(Integer, ForeignKey("component.id"))
    component_data_id = Column(Integer)
    updated = Column(Boolean)
    
    

    
