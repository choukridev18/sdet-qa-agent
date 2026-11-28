from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:5001"


def click(page, test_id):
    page.get_by_test_id(test_id).click()


def fill(page, test_id, text):
    page.get_by_test_id(test_id).fill(text)


def read(page):
    return page.inner_text("body")


def listen_console(page):
    message = []
    page.on("console", lambda msg: message.append(msg.text))
    return message


def listen_network(page):
    message = []
    page.on("requestfailed", lambda req: message.append(req.url))
    return message


def report_bug(text):
    return f"BUG: {text}"


def finish(browser):
    browser.close()


def open_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        logs = listen_console(page)
        network = listen_network(page)
        page.goto(URL)
        click(page, "link-catalog")
        fill(page, "search-product", "mug")
        click(page, "search-submit")
        print(read(page))
        print(logs)
        print(network)
        print(report_bug("serveur: 404"))
        input("Entrée pour fermer…")
        finish(browser)


open_shop()
