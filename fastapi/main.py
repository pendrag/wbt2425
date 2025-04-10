from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import date
from typing import List
from sqlalchemy.orm import Session
from database import get_db
from user import crud as user_crud, schemas as user_schemas
from book import crud as book_crud, schemas as book_schemas
from loan import crud as loan_crud, schemas as loan_schemas
from book.schemas import Book  # Import Book schema
from auth import is_admin_user, is_valid_user
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from config import config

app = FastAPI()

# Mount the public directory as a static files directory
app.mount("/public", StaticFiles(directory="fastapi/public"), name="public")

app.add_middleware(
    CORSMiddleware,
    allow_origins=config['CORS_ORIGINS'],  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Redirect root URL to the public index.html
@app.get("/")
async def redirect_typer():
    return RedirectResponse("/public/index.html")

# User CRUD Operations
@app.post("/user/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@app.get("/user/", response_model=List[user_schemas.User])
async def read_users(skip: int = 0, limit: int = 100, 
                     db: Session = Depends(get_db), 
                     _: user_schemas.User = Depends(is_admin_user)):
    return user_crud.get_users(db, skip, limit)

@app.get("/user/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db),
              current_user: user_schemas.User = Depends(is_valid_user)):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    return user_crud.get_user(db, user_id)

@app.put("/user/{user_id}", response_model=user_schemas.User)
def update_user(user_id: int, user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, user_id, user)

@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user(db, user_id)

# Book CRUD Operations
@app.post("/book/", response_model=book_schemas.Book)
def create_book(book: book_schemas.BookCreate, db: Session = Depends(get_db)):
    return book_crud.create_book(db, book)

@app.get("/book/", response_model=List[book_schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return book_crud.get_books(db, skip, limit)

@app.get("/book/available", response_model=List[book_schemas.Book])
def get_available_books(db: Session = Depends(get_db)):
    return loan_crud.get_available_books(db)

@app.get("/book/{book_id}", response_model=book_schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.get_book(db, book_id)

@app.put("/book/{book_id}", response_model=book_schemas.Book)
def update_book(book_id: int, book: book_schemas.BookCreate, db: Session = Depends(get_db)):
    return book_crud.update_book(db, book_id, book)

@app.delete("/book/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    return book_crud.delete_book(db, book_id)

# Loan CRUD Operations
@app.post("/loan/", response_model=loan_schemas.Loan)
def create_loan(loan: loan_schemas.LoanCreate, db: Session = Depends(get_db)):
    return loan_crud.create_loan(db, loan)

@app.get("/loan/", response_model=List[loan_schemas.Loan])
def read_loans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return loan_crud.get_loans(db, skip, limit)

@app.get("/loan/{user_id}/{book_id}/{start_date}", response_model=loan_schemas.Loan)
def read_loan(user_id: int, book_id: int, start_date: date, db: Session = Depends(get_db)):
    return loan_crud.get_loan(db, user_id, book_id, start_date)

@app.put("/loan/{user_id}/{book_id}/{start_date}", response_model=loan_schemas.Loan)
def update_loan(user_id: int, book_id: int, start_date: date, loan: loan_schemas.LoanCreate, db: Session = Depends(get_db)):
    return loan_crud.update_loan(db, user_id, book_id, start_date, loan)

@app.delete("/loan/{user_id}/{book_id}/{start_date}")
def delete_loan(user_id: int, book_id: int, start_date: date, db: Session = Depends(get_db)):
    return loan_crud.delete_loan(db, user_id, book_id, start_date)

# Authentication
from auth import login_user, Token
from fastapi.security import OAuth2PasswordRequestForm  

@app.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_user(db, form_data.username, form_data.password)

