# Description: User models for SQLAlchemy ORM.
#
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, SmallInteger
from database import Base

# SQLAlchemy Models
class UserDB(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    role = Column(SmallInteger, nullable=False, default=0)
    
    # Relationships
    books = relationship("BookDB", back_populates="owner_rel")
    loans = relationship("LoanDB", back_populates="user_rel")