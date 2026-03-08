#!/usr/bin/python3
"""
This module contains the class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create Base instance from declarative_base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states
    
    Attributes:
        id: auto-generated, unique integer, primary key, cannot be null
        name: string with maximum 128 characters, cannot be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
