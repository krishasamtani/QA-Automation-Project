from playwright.sync_api import sync_playwright

def test_add_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.click("#add-to-cart-sauce-labs-backpack")

        # Cart badge me "1" dikhna chahiye
        cart_badge = page.locator(".shopping_cart_badge").inner_text()
        assert cart_badge == "1"

        # Button ka text "Remove" ho jaana chahiye
        button_text = page.locator("#remove-sauce-labs-backpack").inner_text()
        assert button_text == "Remove"

        browser.close()

def test_remove_from_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login karo
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Pehle item add karo cart me
        page.click("#add-to-cart-sauce-labs-backpack")

        # Ab cart page pe jao
        page.click(".shopping_cart_link")

        # Item remove karo
        page.click("#remove-sauce-labs-backpack")

        # Cart badge gayab ho jaana chahiye (kyunki 0 items hain)
        cart_badge_count = page.locator(".shopping_cart_badge").count()
        assert cart_badge_count == 0

        browser.close()