from sanic import Sanic
from sanic.response import json

app = Sanic("Library")


@app.get("/books")
async def get_books(request):
    return json({"Hello": "world."})

@app.post("/books")
async def add_book(request):
    return json({"Status": "Ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
