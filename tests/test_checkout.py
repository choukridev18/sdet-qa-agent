from playwright.sync_api import Page, expect

URL = "http://127.0.0.1:5001"


def test_empty_checkout_shows_error(page: Page):
    page.goto(f"{URL}/reset")
    page.goto(f"{URL}/checkout")
    page.get_by_test_id("checkout-submit").click()
    expect(
        page.get_by_text("Veuillez renseigner les champs pour confirmer")
    ).to_be_visible()


def test_login(page: Page):
    page.goto(f"{URL}/reset")
    page.get_by_test_id("link-login").click()
    expect(page).to_have_url(f"{URL}/login")
    page.get_by_test_id("login-username").fill("choukri")
    page.get_by_test_id("login-password").fill("testeur")
    page.get_by_test_id("login-submit").click()
    expect(page).to_have_url(f"{URL}/")
    expect(page.get_by_test_id("home-welcome")).to_contain_text("choukri")
