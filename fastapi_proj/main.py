from fastapi import FastAPI
from schema import Book as SchemaBook
from models import Book as ModelBook
from fastapi_sqlalchemy import db, DBSessionMiddleware
from database import SQLALCHEMY_DATABASE_URL

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=SQLALCHEMY_DATABASE_URL)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/book/', response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get('/book/')
async def book():
    book = db.session.query(ModelBook).all()
    return book
