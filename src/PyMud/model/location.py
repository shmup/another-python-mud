'''
Created on Nov 26, 2011

@author: Nich
'''
from sqlalchemy import Column, Integer
from model import Base

class LocalPositionComponent(Base):
    '''
        Stores the local and world positions of the component
    '''
    __tablename__ = "local_position_component"
    comp_data_id = Column(Integer, primarykey=True)
    local_x = Column(Integer)
    local_y = Column(Integer)
    local_z = Column(Integer)
    
