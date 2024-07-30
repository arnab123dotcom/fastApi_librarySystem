from pydantic import BaseModel

class BookInfo(BaseModel):
    bookName: str
    num: int