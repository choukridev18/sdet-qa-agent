from app import app


def test_empty_checkout_returns_error():
    client = app.test_client()
    response = client.post("/checkout", data={})
    text = response.get_data(as_text=True)
    assert "Veuillez renseigner les champs pour confirmer" in text
