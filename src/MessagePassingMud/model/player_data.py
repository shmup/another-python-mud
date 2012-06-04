'''
Created on Nov 27, 2011

@author: Nich
'''
from model import Base, engine, Session
from sqlalchemy import Column, String, Integer


class PlayerData(Base):
    __tablename__ = "player_data"
    
    player_data_id = Column(Integer, primary_key=True)
    name = Column(String)
    location_x = Column(Integer)
    location_y = Column(Integer)
    location_z = Column(Integer)
    
    def __init__(self, name, password):
        self.name = name
        


def print_all():
    session = Session()
    for instance in session.query(PlayerData).order_by(PlayerData.player_id): 
        print(instance.name)
        
def get(username):
    session = Session()
    try:
        return session.query(PlayerData).filter(PlayerData.name==username).one()
    except:
        return None
    
Base.metadata.create_all(engine)