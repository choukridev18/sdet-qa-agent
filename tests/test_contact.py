from playwright.sync_api import Page, expect

URL = "http://127.0.0.1:5001"


def test_empty_contact_shows_error(page: Page):
    page.goto(f"{URL}/reset")
    page.get_by_test_id("link-contact").click()
    expect(page).to_have_url(f"{URL}/contact")
    page.get_by_test_id("contact-submit").click()
    expect(page.get_by_text("Veuillez renseigner les champs requis")).to_be_visible()
