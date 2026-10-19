from playwright.sync_api import Page, expect

def test_product_images(page: Page):
    url = "https://books.toscrape.com/index.html"
    page.goto(url)

    expect(page).to_have_url(url)

    for i in range(1,6):

        books = page.locator('article.product_pod').all()

        for book in books:
            expect(book).to_be_visible()
            image = book.locator('.image_container img')
            img_src = image.get_attribute('src')
            assert img_src and img_src.strip(), 'Image src is missing or empty'
            expect(image).to_be_visible()
            img_alt = image.get_attribute('alt')
            assert img_alt and img_alt.strip(), 'Image alt is missing or empty'

            expect(image).to_contain_class('thumbnail')
            expect(image).to_be_visible()
            
        print(f'Page {i}: Image validations passed')

        if i == 5:
            break
        next = page.locator('.next')

        if next.count()>0:
            next.locator('a').click()
            expect(page).to_have_url(f'https://books.toscrape.com/catalogue/page-{i+1}.html')
        else:
            break
        
