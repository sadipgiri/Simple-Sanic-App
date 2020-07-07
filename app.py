from sanic import Sanic
from sanic.response import json, html, text
import os

app = Sanic("Sadip Simple Sanic App")

# return json response
@app.route("/")
async def test(request):
    return json({"hello": "world"})

# return html
@app.route("/html")
async def test(request):
    template = open(os.getcwd() + "/templates/index.html")
    return html(template.read())

# return text
@app.route("/text")
async def test(request):
    return text("This is Text Response.")

if __name__ == "__main__":
    app.run(host="0.0.0.0")