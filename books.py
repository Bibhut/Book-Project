from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"}
]



@app.get("/books")
async def read_all_books():
    return BOOKS


# Using Path Parameters
@app.get("/books/{book_title}")
async def read_books_with_book_title(book_title:str):
    for book in BOOKS:
        title = book.get('title')
        if title and  title.casefold() == book_title.casefold():
            return book

