import pytest
from playwright.sync_api import expect,TimeoutError


def handle_cookies(page):
    try:
        page.locator("#c-s-bn").click(timeout=2000)
    except TimeoutError:
        pass


def test_homepage_loaded(page):
    homepage_vivaplus = "https://vivaplus.tv/en-eur"
    title_webpage = "Viva+"

    page.goto(homepage_vivaplus)
    handle_cookies(page)

    assert page.title() == title_webpage



def test_login_button(page):
    homepage_vivaplus = "https://vivaplus.tv/en-eur"
    
    page.goto(homepage_vivaplus)
    handle_cookies(page)
    
    page.get_by_role("link", name="Account").click()

    assert page.url.endswith("supporters")
    

def test_added_to_cart(page):
    homepage_vivaplus = "https://vivaplus.tv/en-eur"
    product_name = "VLDL Dice Set"

    # go to homepage
    page.goto(homepage_vivaplus)
    handle_cookies(page)

    # open shop via hamburger menu
    page.get_by_role("button", name="Hamburger").click()
    page.get_by_role("link", name="Shop").click()

    # add product to cart
    page.get_by_role("heading", name=product_name).first.click()
    page.get_by_test_id("product.add.to.cart").click()

    # open cart
    page.get_by_role("link", name="View Cart").click()

    expect(page.get_by_text(product_name)).to_be_visible()