from sanic import Sanic, Blueprint
from sanic.response import json

app = Sanic("Library")
bp = Blueprint('my_blueprint')


@bp.listener('before_server_start')
async def setup_connection(app, loop):
    global database
    print('Hello World!')


@bp.listener('after_server_stop')
async def close_connection(app, loop):
    print('Bye bye!')
    await database.close()


@app.get("/books")
async def get_books(request):
    return json({"Hello": "world."})


@app.post("/books")
async def add_book(request):
    return json({"Status": "Ok"})

if __name__ == "__main__":
    app.blueprint(bp)
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True)
