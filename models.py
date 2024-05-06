from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Book(Base):
  __tablename__ = "books"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, nullable=False)
  author = Column(String, nullable=False)
  year = Column(Integer, nullable=False)
  isbn = Column(String, nullable=False, unique=True)

  def __repr__(self):
    return f"Book(id={self.id}, title='{self.title}', author='{self.author}', year={self.year}, isbn='{self.isbn}')"

# Database connection details (replace with your actual configuration)
DATABASE_URL = "sqlite:///books.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
