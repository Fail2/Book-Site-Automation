import re
from playwright.sync_api import Page, expect

def test_homepage(page:Page):
    url = "https://books.toscrape.com/index.html"
    page.goto(url)

    expect(page).to_have_url(url)
    expect (page).to_have_title(re.compile("Books to Scrape"))

    headers = page.locator("h1, h2, h3, h4, h5, h6")
    assert headers.count() > 0, 'No header found on the page'
    for i in range(headers.count()):
        header = headers.nth(i)
        if header.is_visible():
            expect(header).to_be_visible()
            text = header.inner_text().strip()
            assert text != '', f'Header {i} has empty text'
    
    books = page.locator('article.product_pod')
    expect(books.first).to_be_visible()
    assert books.count() > 0, 'Book list is empty'
    