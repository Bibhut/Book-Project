from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "History"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Science"}
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



@app.get("/books/{author}/")
async def read_book_with_author_and_category(author:str, category:str):
    books_to_return = []
    for book in BOOKS:
        book_author = book.get('author')
        book_category = book.get('category')
        if((book_author and book_author.casefold() == author.casefold()) and ( book_category and  book_category.casefold() == category.casefold())):
            books_to_return.append(book)
    return books_to_return

@app.get("/books/")
async def read_book_with_query( category:str):
    books_to_return = []
    for book in BOOKS:
        book_category = book.get('category')
        if(book_category and  book_category.casefold() == category.casefold()):
            books_to_return.append(book)
    return books_to_return


# POST Method to add new books. 
@app.post("/book/create_book")
async def create_books(new_book=Body()):
    BOOKS.append(new_book)
    return BOOKS

#PUT Method to update book
@app.put('/books/update_book')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        book_title = BOOKS[i].get('title')
        if book_title and book_title.casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book
            break
    return BOOKS

@app.delete('/books/delete_book')
async def delete_book(delete_book=Body()):
    for i in range(len(BOOKS)):
        book_title = BOOKS[i].get('title')
        if book_title and book_title.casefold() == delete_book.get('title').casefold():
           BOOKS.pop(i)
           break
    return BOOKS