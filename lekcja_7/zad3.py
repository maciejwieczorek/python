#!/usr/bin/env 

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.org import sessionmaker
from sqlalchemy.types import NUMERIC

Base = declarative_base()

import sqlite3


class Test(Base):
    __table_name__ = 'Ksiazka'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    value = Culumn(Numeric)
    
class Test1(Base
    
engine = create_engine('sqlite://example3', echo=True)

Base.metadata.create_all(engine)

Session = sessonmaker(bind = engine)

session = Session()
