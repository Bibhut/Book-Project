from fastapi import FastAPI
app = FastAPI()


BOOKS = [
    {"author": "Author One", "title": "Title One", "category": "Science" },
    {"author": "Author Two", "title": "Title Two", "category": "Social Studies" },
    {"author": "Author Three", "title": "Title Three", "category": "Nepali" },
    {"author": "Author Four", "title": "Title Four", "category": "History" },
    {"author": "Author Five", "title": "Title Five", "category": "Math" }
]

@app.get('/books/{author}')
async def get_book_based_on_author(author: str):
    for book in BOOKS:
        book_author = book.get('author')
        if book_author and book_author.casefold() == author.casefold():
            return book