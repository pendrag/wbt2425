from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import date
from .models import LoanDB
from .schemas import LoanCreate, Loan
from book.models import BookDB

def create_loan(db: Session, loan: LoanCreate):
    db_loan = LoanDB(**loan.dict())
    try:
        db.add(db_loan)
        db.commit()
        db.refresh(db_loan)
        return db_loan
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_loans(db: Session, skip: int = 0, limit: int = 100):
    return db.query(LoanDB).offset(skip).limit(limit).all()

def get_loan(db: Session, user_id: int, book_id: int, start_date: date):
    db_loan = db.query(LoanDB).filter(
        LoanDB.id_user == user_id,
        LoanDB.id_book == book_id,
        LoanDB.start == start_date
    ).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan

def update_loan(db: Session, user_id: int, book_id: int, start_date: date, loan: LoanCreate):
    db_loan = db.query(LoanDB).filter(
        LoanDB.id_user == user_id,
        LoanDB.id_book == book_id,
        LoanDB.start == start_date
    ).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    for key, value in loan.dict().items():
        setattr(db_loan, key, value)
    
    try:
        db.commit()
        db.refresh(db_loan)
        return db_loan
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def delete_loan(db: Session, user_id: int, book_id: int, start_date: date):
    db_loan = db.query(LoanDB).filter(
        LoanDB.id_user == user_id,
        LoanDB.id_book == book_id,
        LoanDB.start == start_date
    ).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    
    try:
        db.delete(db_loan)
        db.commit()
        return {"message": "Loan deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_available_books(db: Session):
    subquery = db.query(LoanDB.id_book).filter(LoanDB.status == 'available').subquery()
    available_books = db.query(BookDB).filter(BookDB.id.in_(subquery)).all()
    return available_books