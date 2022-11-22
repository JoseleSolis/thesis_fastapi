from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Person(Base):
        __tablename__ = 'person'
        id = Column(Integer, primary_key=True)
        name = Column(String(20))
        last_name = Column(String(20))
        
class Item(Base):
        __tablename__ = 'item'
        id = Column(Integer, primary_key=True)
        serial_number = Column(String(8))
        description = Column(String(256))
        stock_number = Column(Integer)
        category_id = Column(Integer, ForeignKey('category.id'))

class ItemCategory(Base):
        __tablename__ = 'category'
        id = Column(Integer, primary_key=True)
        name = Column(String(256))



