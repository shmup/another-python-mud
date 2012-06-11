from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///fake.db', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()





