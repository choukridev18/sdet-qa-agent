from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:5001"


def click(page, test_id):
    page.get_by_test_id(test_id).click()


def fill(page, test_id, text):
    page.get_by_test_id(test_id).fill(text)


def open_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        click(page, "link-catalog")
        fill(page, "search-product", "mug")
        click(page, "search-submit")
        print(page.inner_text("body"))
        input("Entrée pour fermer…")


open_shop()
