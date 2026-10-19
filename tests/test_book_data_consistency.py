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
        homepage_title = title_link.get_attribute('title').strip()
        homepage_price = book.locator('.price_color').inner_text().strip()
        
        assert homepage_price.startswith('£'), f'Price missing £ sign {homepage_price}'
        assert len(homepage_price) > 1, f'Invalid homepage_price {homepage_price}'

        book_url = title_link.get_attribute('href')

        title_link.click()
        
        expect(page).to_have_url(f'https://books.toscrape.com/{book_url}')
        
        details_title = page.locator('h1').first.inner_text().strip()

   
        assert homepage_title == details_title,(
            f"Title mismatch! Homepage: {homepage_title}, Detail: {details_title}"
        )

        details_price = page.locator('.product_main .price_color').inner_text().strip()
        assert details_price.startswith('£'), f'Price missing £ sign {details_price}'
        assert len(details_price) > 1, f'Invalid details_price {details_price}'

        assert homepage_price == details_price,(
            f"Price mismatch! Homepage: {homepage_price}, Detail: {details_price}"
        )

        expect(page.locator('article.product_page')).to_be_visible()
        expect(page.locator('#product_gallery')).to_be_visible()
        expect(page.locator('.product_main')).to_be_visible()
        expect(page.locator('.product_main .price_color')).to_be_visible()

        page.go_back()

        expect(page).to_have_url(url)
        expect(books.nth(value)).to_be_visible()

