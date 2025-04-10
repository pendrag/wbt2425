from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import BookDB
from .schemas import BookCreate, Book

def create_book(db: Session, book: BookCreate):
    db_book = BookDB(**book.dict())
    try:
        db.add(db_book)
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookDB).offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

def update_book(db: Session, book_id: int, book: BookCreate):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in book.dict().items():
        setattr(db_book, key, value)
    
    try:
        db.commit()
        db.refresh(db_book)
        return db_book
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

def delete_book(db: Session, book_id: int):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    try:
        db.delete(db_book)
        db.commit()
        return {"message": "Book deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))