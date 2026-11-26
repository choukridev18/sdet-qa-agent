from playwright.sync_api import Page, expect

URL = "http://127.0.0.1:5001"


def test_empty_checkout_shows_error(page: Page):
    page.goto(f"{URL}/reset")
    page.goto(f"{URL}/checkout")
    page.get_by_test_id("checkout-submit").click()
    expect(
        page.get_by_text("Veuillez renseigner les champs pour confirmer")
    ).to_be_visible()
