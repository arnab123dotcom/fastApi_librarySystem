from fastapi import APIRouter, HTTPException, Depends
from database_connect.bookshelf import Admin
from database_connect.database import get_db
from pydantic_schemas.book_issued import BookInfo
from sqlalchemy.orm import Session
import uuid

router = APIRouter()

@router.post("/addBook", status_code=201)
def addBook(book: BookInfo, db: Session=Depends(get_db)):
    bookFromDb = db.query(Admin).filter(Admin.name == book.bookName).first()

    if bookFromDb:
        if book.num == 1:
            book.num = bookFromDb.numbersOfBook
            book.num += 1
        else:
            bookFromDb.numbersOfBook += book.num
        db.commit()
        db.refresh(bookFromDb)
        return bookFromDb
    
    newBook = Admin(id=str(uuid.uuid4()), name=book.bookName, numbersOfBook=book.num)

    db.add(newBook)
    db.commit()
    db.refresh(newBook)

    return newBook


    

