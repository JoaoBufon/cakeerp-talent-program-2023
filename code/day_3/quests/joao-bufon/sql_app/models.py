from sqlalchemy import Boolean, Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from .database import Base

class Item(Base):
    __trablename__ = "items"
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="items")
    
    
class User(Base):
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    description = Column(String, index=True)