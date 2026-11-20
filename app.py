from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "dev"


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


@app.route("/cart")
def cart():
    return render_template("cart.html", cart_items=session.get("cart", []))


@app.route("/cart/add/<slug>", methods=["POST"])
def add_to_cart(slug):
    items = list(session.get("cart", []))
    items.append(slug)
    session["cart"] = items
    return redirect("/cart")
