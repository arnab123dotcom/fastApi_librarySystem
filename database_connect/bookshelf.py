from database_connect.base import Base
from sqlalchemy import TEXT, VARCHAR, Column, INT

class Admin(Base):
    __tablename__ = "bookshelf"

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    numbersOfBook = Column(INT)