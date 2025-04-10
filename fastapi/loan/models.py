# Description: Loan models for SQLAlchemy ORM.
#
from sqlalchemy import Column, Integer, Date, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database import Base
from .schemas import LoanStatus

class LoanDB(Base):
    __tablename__ = "loan"
    id_user = Column(Integer, ForeignKey('user.id'), primary_key=True, index=True)
    id_book = Column(Integer, ForeignKey('book.id'), primary_key=True, index=True)
    status = Column(Enum(LoanStatus), default=LoanStatus.reserved)
    start = Column(Date, nullable=True)
    end = Column(Date, nullable=True)

    # Relationships
    user_rel = relationship("UserDB", back_populates="loans")
    book_rel = relationship("BookDB", back_populates="loans")