'''
Created on Jun 12, 2012

@author: Nich
'''

from model import Base, engine, Session
from sqlalchemy import Column, Integer, and_


class DataMap(Base):
    __tablename__ = "data_map"
    x = Column('x', Integer, primary_key=True, nullable=False, autoincrement=False)
    y = Column('y', Integer, primary_key=True, nullable=False, autoincrement=False)
    value = Column('value', Integer)
    
    
    @staticmethod    
    def get_stored_value(tile):
        x, y = tile
        session = Session()
       
        value = session.query(DataMap).filter(and_(DataMap.x==x, DataMap.y==y)).one().value 
        return value
        
    
    @staticmethod
    def get_stored_range(x_min, x_max, y_min, y_max):
        session = Session()
        
        value = session.query(DataMap).filter(and_(DataMap.x >= x_min, DataMap.x <= x_max, \
                                                   DataMap.y >= y_min, DataMap.y <= y_max)).all() 
        ret_val = {}
        for tile in value:
            ret_val[(tile.x, tile.y)] = tile.value
        return ret_val
        
        
    @staticmethod
    def set_stored_value(tile, value):
        x, y = tile
        session = Session()
        entry = DataMap(x=x, y=y, value=value)
        session.merge(entry)    
        session.commit()
    
    @staticmethod
    def dump_map_to_db(d_map):
        session = Session()
        
        for t in d_map:
            x, y, v = t
            entry = DataMap(x=x, y=y, value=v)
            session.merge(entry)
        session.commit()
    
        

#Base.metadata.create_all(engine)