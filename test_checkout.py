from playwright.sync_api import sync_playwright

def test_checkout_empty_first_name():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login karo
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Item add karo aur checkout tak jao
        page.click("#add-to-cart-sauce-labs-backpack")
        page.click(".shopping_cart_link")
        page.click("#checkout")

        # First Name khali chodo, baaki fields bharo
        page.fill("#last-name", "Sharma")
        page.fill("#postal-code", "123456")
        page.click("#continue")

        # Error message check karo
        error_message = page.locator("[data-test='error']").inner_text()
        assert "First Name is required" in error_message

        browser.close()

def test_complete_checkout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login karo
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Item add karo aur checkout tak jao
        page.click("#add-to-cart-sauce-labs-backpack")
        page.click(".shopping_cart_link")
        page.click("#checkout")

        # Saare fields valid data se bharo
        page.fill("#first-name", "Krisha")
        page.fill("#last-name", "Samtani")
        page.fill("#postal-code", "123456")
        page.click("#continue")

        # Overview page pe "Finish" click karo
        page.click("#finish")

        # Confirmation message check karo
        confirmation = page.locator(".complete-header").inner_text()
        assert "Thank you for your order!" in confirmation

        browser.close()