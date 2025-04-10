# Description: Book model for SQLAlchemy ORM
#
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from database import Base

class BookDB(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    owner = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(80), nullable=False)
    author = Column(String(80), nullable=True)
    
    # Relationships
    owner_rel = relationship("UserDB", back_populates="books")
    loans = relationship("LoanDB", back_populates="book_rel")