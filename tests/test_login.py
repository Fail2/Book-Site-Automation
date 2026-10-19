
from playwright.sync_api import Page, expect


def test_login_logout_validation(page: Page):
    url = "https://quotes.toscrape.com/"
    page.goto(url)

    expect(page).to_have_url(url)

    login_link = page.locator("a[href='/login']")
    expect(login_link).to_be_visible()


    login_link.click()

    expect(page).to_have_url("https://quotes.toscrape.com/login")

    username_field = page.locator("input[name='username']")
    password_field = page.locator("input[name='password']")

    expect(username_field).to_be_visible()
    expect(password_field).to_be_visible()

    username_field.type('malay')
    password_field.type('malay')

    page.locator("input[type='submit']").click()

    logout_link = page.locator("a[href='/logout']")

    expect(logout_link).to_be_visible()
    expect(logout_link).to_be_enabled()

    print("Login successful. Logout link is visible.")
