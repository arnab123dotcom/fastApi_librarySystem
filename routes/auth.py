from fastapi import Depends, HTTPException, APIRouter
from pydantic_schemas.signin_info import UserSignin
from pydantic_schemas.signup_info import UserSignup
from database_connect.userinfo_table import User
from database_connect.bookshelf import Admin
from sqlalchemy.orm import Session
from database_connect.database import get_db
import uuid
import json

router = APIRouter()

@router.post("/signup", status_code=201)
def signup_user(user: UserSignup, db: Session=Depends(get_db)):
    userFromDb = db.query(User).filter(User.email == user.email).first()

    if userFromDb:
        raise HTTPException(400, "The email already exists!")
    
    newUser = User(id=str(uuid.uuid4()), username=user.username, email=user.email, password=user.password)
    
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

@router.post("/signin")
def signin_user(user: UserSignin, db: Session=Depends(get_db)):
    userFromDb = db.query(User).filter(User.email == user.email).first()
    booklist = db.query(Admin.name, Admin.numbersOfBook).all()

    if not userFromDb:
        raise HTTPException(400, "Sign Up first!")
    
    if user.password != userFromDb.password:
        raise HTTPException(400, "Incorrect Password!!")
    
    bookinfo = {}
    
    for book in booklist:
        bookinfo[book[0]] = book[1]

    return json.dumps(bookinfo, sort_keys=True)
