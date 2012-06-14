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
    z = Column('z', Integer, primary_key=True, nullable=False, autoincrement=False)
    value = Column('value', Integer)
    
    
        
def get_stored_value(tile):
    x, y, z = tile
    session = Session()
    try:
        value = session.query(DataMap).filter(and_(DataMap.x==x, DataMap.y==y, DataMap.z==z)).one().value 
        return value
    except:
        return None
    
def set_stored_value(tile, value):
    x, y, z = tile
    session = Session()
    entry = DataMap(x=x, y=y, z=z, value=value)
    session.merge(entry)    
    session.commit()
    
def dump_map_to_db(d_map):
    session = Session()
    
    for t in d_map:
        x, y, z, v = t
        entry = DataMap(x=x, y=y, z=z, value=v)
        session.merge(entry)
        
    
    session.commit()
    
        

Base.metadata.create_all(engine)