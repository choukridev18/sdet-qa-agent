from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:5001"


def open_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(URL)
        page.get_by_test_id("link-catalog").click()
        page.get_by_test_id("search-product").fill("mug")
        page.get_by_test_id("search-submit").click()
        print(page.inner_text("body"))
        input("Entrée pour fermer…")


open_shop()
