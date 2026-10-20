import random
from playwright.sync_api import Page, expect

def test_book_navigation(page: Page):
    url = "https://books.toscrape.com/index.html"
    page.goto(url)

    expect(page).to_have_url(url)

    books = page.locator('article.product_pod')
    assert books.count() >= 5, 'This page shows less than 5 books'

    random_values = random.sample(range(books.count()), 5)

    for value in random_values:
        book = books.nth(value)

        title_link = book.locator('h3 a')
        title = title_link.get_attribute('title')
        assert title and title.strip(), f'Title is empty for book at index {value}'

        book_url = title_link.get_attribute('href')
        assert book_url and book_url.strip(), f'Book URL is empty for book at index {value}'
        title_link.click()
        
        expect(page).to_have_url(f'https://books.toscrape.com/{book_url}')
        
        detail_title = page.locator('h1').first.inner_text()
        assert detail_title and detail_title.strip(), f'Detail title is empty for book at index {value}'
        
        assert title == detail_title,(
            f"Title mismatch! List: {title}, Detail: {detail_title}"
        )

        expect(page.locator('article.product_page')).to_be_visible()
        expect(page.locator('#product_gallery')).to_be_visible()
        expect(page.locator('.product_main')).to_be_visible()
        expect(page.locator('.product_main .price_color')).to_be_visible()

        page.go_back()

        expect(page).to_have_url(url)
        expect(books.nth(value)).to_be_visible()

