from pydantic import BaseModel

class UserSignin(BaseModel):
    email: str
    password: str