from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/catalog")
def catalog():
    return render_template("catalog.html")


@app.route("/product/<slug>")
def product(slug):
    if slug == "tshirt":
        price = 20
    elif slug == "mug":
        price = 8
    elif slug == "glove":
        price = 16
    else:
        price = 0

    return render_template("product.html", slug=slug, price=price)
