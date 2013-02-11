'''
Created on Nov 27, 2011

@author: Nich
'''
from model import Base, Session
from model.mbot_data import MBotData
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship



class Account(Base):
    __tablename__ = "accounts"
    
    account_id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    mbots = relationship("MBotData")
    
    def __init__(self, name, password):
        self.name = name
        self.password = password


def print_all():
    session = Session()
    for instance in session.query(Account).order_by(Account.account_id): 
        print(instance.name)
        
def get(username):
    session = Session()
    #try:
    return session.query(Account).filter(Account.name==username).one()
    #except:
        #return None

def make_account(username, password):
    session = Session()
    a = Account(username, password)
    session.add(a)
    bot = MBotData("testerbot", 0, 0, )
    
    session.commit()
    

    
