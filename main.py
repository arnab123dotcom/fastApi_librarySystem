from fastapi import FastAPI
from database_connect.base import Base
from database_connect import database
from routes import auth, admin_bookpanel

app = FastAPI()

Base.metadata.create_all(database.engine)

app.include_router(admin_bookpanel.router)
app.include_router(auth.router, prefix="/auth")
