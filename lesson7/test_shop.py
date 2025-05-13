import pytest
from selenium import webdriver
from shop_page import ShopPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.shop_login()
    shop_page.add_item_to_card()
    shop_page.click_to_card()
    shop_page.checkout()
    shop_page.fill_user_data()
    assert shop_page.get_total_sum() == "$58.29", f"Ожидалась сумма $58.29, получена другая"