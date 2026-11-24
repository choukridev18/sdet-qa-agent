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
    user = session.get("user", "")

    return render_template("home.html", user=user)


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


@app.route("/cart", methods=["GET", "POST"])
def cart():
    list_products = session.get("cart", [])
    somme_total = 0
    for i in list_products:
        somme_total += i["price"]
    if request.method == "POST":
        promo = request.form.get("promo", "")
        if promo == "CHOUKRI47":
            if session.get("user", ""):
                session["promo"] = promo
            else:
                somme_total *= 0.9

    if session.get("promo", "") == "CHOUKRI47" and session.get("user", ""):
        somme_total *= 0.9
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


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if username == "choukri" and password == "testeur":
            session["user"] = username
            return redirect("/")
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/logout", methods=["POST"])
def logout():
    session["user"] = ""
    session["promo"] = ""
    return redirect("/")


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    message = ""
    if request.method == "POST":
        name = request.form.get("name", "")
        address = request.form.get("address", "")
        if name != "" and address != "":
            session["cart"] = []
            session["promo"] = ""
            message = "Merci pour vos achats"

    return render_template("checkout.html", message=message)
