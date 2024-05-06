from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from models import Book, SessionLocal, engine
from schemas import Book, BookCreate, BookUpdate

app = app = FastAPI(
    title="Book Management API",
    description="A simple API for managing a book collection",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

# Dependency for database session
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/books", response_model=list[Book])
def get_books(db: Session = Depends(get_db)):
  books = db.query(Book).all()
  return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first()
  if not book:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
  return book

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
  new_book = Book(**book.dict())
  db.add(new_book)
  db.commit()
  db.refresh(new_book)
  return new_book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first()
  if not book:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

  update_data = book_update.dict(exclude_unset=True)
  for key, value in update_data.items():
    setattr(book, key, value)

  db.commit()
  db.refresh(book)
  return book

@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
  book = db.query(Book).filter(Book.id == book_id).first()
  if not book:
    raise HTTP
