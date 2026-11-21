from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "dev"

PRODUCTS = {
    "tshirt": 20,
    "mug": 8,
    "glove": 16,
    "scarf": 6,
}


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/catalog")
def catalog():
    query = request.args.get("q", "")
    articles = PRODUCTS
    if query:
        articles = {}
        for name, price in PRODUCTS.items():
            if query.lower() in name.lower():
                articles[name] = price
    return render_template("catalog.html", liste_articles=articles)


@app.route("/product/<slug>")
def product(slug):
    price = PRODUCTS.get(slug, 0)
    return render_template("product.html", slug=slug, price=price)


@app.route("/cart")
def cart():
    list_products = session.get("cart", [])
    somme_total = 0
    for i in list_products:
        somme_total += i["price"]
    return render_template("cart.html", cart_items=list_products, total=somme_total)


@app.route("/cart/add/<slug>", methods=["POST"])
def add_to_cart(slug):
    items = list(session.get("cart", []))
    items.append({"slug": slug, "price": PRODUCTS.get(slug, 0)})
    session["cart"] = items
    return redirect("/cart")


@app.route("/cart/clear", methods=["POST"])
def clear():
    session["cart"] = []
    return redirect("/cart")
