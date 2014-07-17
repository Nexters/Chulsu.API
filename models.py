# -*- coding:utf-8 -*-
from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from database import Base

class Info(Base):
    __tablename__ = 'infos'
    id = Column(Integer, primary_key=True)
    text = Column(String(50), unique=False)
    description = Column(String(120), unique=False)
    etc = Column(String(120), unique=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp())

    def __init__(self, text=None, description=None, etc=None):
        self.text = text
        self.description = description
        self.etc = etc

    def __repr__(self):
        return '<Info %r>' % (self.text)
