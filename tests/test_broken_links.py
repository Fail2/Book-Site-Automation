from urllib.parse import urljoin
from playwright.sync_api import Page, expect

def test_broken_links(page:Page):
    url = "https://books.toscrape.com/index.html"
    page.goto(url)

    expect(page).to_have_url(url)

    links = page.locator('a')

    assert links.count() > 0, 'No hyperlinks found on the homepage'
    hrefs = {href for href in links.evaluate_all(
        "(elements) => elements.map(el => el.getAttribute('href'))"
    ) if href and not href.startswith("#") 
    and not href.startswith("javascript:")
    and not href.startswith("mailto:")
    and not href.startswith("tel:")}
    # print(hrefs)

    for href in hrefs:
        full_url = urljoin(url, href)
        
        response = page.request.get(full_url)
        status = response.status

        print(f'{full_url} -> {status}')

        assert status == 200, (
            f'Expected HTTP 200, got {status} for {full_url}'
        )