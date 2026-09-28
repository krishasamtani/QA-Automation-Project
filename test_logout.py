from playwright.sync_api import sync_playwright
def test_logout():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Login karo
        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        # Hamburger menu kholo
        page.click("#react-burger-menu-btn")

        # Logout click karo
        page.click("#logout_sidebar_link")

        # Wapas login page pe aana chahiye
        assert page.url == "https://www.saucedemo.com/"

        browser.close()

def test_locked_out_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com")
        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        error_message = page.locator("[data-test='error']").inner_text()
        assert "Sorry, this user has been locked out" in error_message

        browser.close()