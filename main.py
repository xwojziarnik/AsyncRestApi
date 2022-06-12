from sanic import Sanic, Blueprint
from sanic.response import json, HTTPResponse
from pymongo import MongoClient


app = Sanic("Library")
bp = Blueprint('my_blueprint')


@bp.listener('before_server_start')
async def setup_connection(app, loop):
    global client
    client = MongoClient(
        'localhost',
        27017,
        username='root',
        password='example'
    )


@bp.listener('after_server_stop')
async def close_connection(app, loop):
    await client.close()


@app.get("/")
async def homepage(request):
    return HTTPResponse("Hello! Go to -> http://127.0.0.1:8000/books and add book using POST method or list all books using GET method.")


@app.get("/books")
async def get_books(request):
    db = client['library']
    books = db['books'].find()
    return json([{"title": book["title"], "author": book["author"]} for book in books])


@app.post("/books")
async def add_book(request):
    db = client['library']
    books = db['books']

    book = request.json
    book_id = books.insert_one(book).inserted_id
    return json({'Id': str(book_id)})

if __name__ == "__main__":
    app.blueprint(bp)
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)
