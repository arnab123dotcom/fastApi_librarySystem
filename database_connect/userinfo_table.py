from database_connect.base import Base
from sqlalchemy import TEXT, VARCHAR, Column

class User(Base):
    __tablename__ = "userinfo"

    id = Column(TEXT, primary_key=True)
    username = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(VARCHAR(100))