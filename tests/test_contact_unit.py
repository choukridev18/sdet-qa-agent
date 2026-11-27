from app import app


def test_empty_form_contact_shows_error():
    client = app.test_client()
    response = client.post("/contact", data={})
    text = response.get_data(as_text=True)
    assert "Veuillez renseigner les champs requis" in text
