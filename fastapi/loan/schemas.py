from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum

class LoanStatus(str, Enum):
    reserved = "reserved"
    onloan = "on loan"
    available = "available"

class LoanBase(BaseModel):
    id_user: int
    id_book: int
    status: LoanStatus = LoanStatus.available
    start: Optional[date] = None
    end: Optional[date] = None

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    class Config:
        from_attributes = True