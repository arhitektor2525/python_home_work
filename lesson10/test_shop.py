import allure
import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture
def driver() -> webdriver.Firefox:
    """
    Фикстура для инициализации и завершения работы драйвера.

    Yields:
        Экземпляр Firefox WebDriver
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка полного цикла оформления заказа")
@allure.description("""
Тест проверяет полный процесс оформления заказа:
1. Авторизация стандартного пользователя
2. Добавление трех товаров в корзину
3. Оформление заказа
4. Проверка итоговой суммы
""")
def test_shop_page(driver: webdriver.Firefox) -> None:
    """Тест полного цикла оформления заказа в интернет-магазине."""
    shop_page = ShopPage(driver)

    with allure.step("1. Открыть и авторизоваться"):
        shop_page.open()
        shop_page.shop_login()

    with allure.step("2. Добавить три товара в корзину"):
        shop_page.add_item_to_card()

    with allure.step("3. Оформить заказ"):
        shop_page.click_to_card()
        shop_page.checkout()
        shop_page.fill_user_data()

    with allure.step("4. Проверить итоговую сумму"):
        total = shop_page.get_total_sum()
        assert total == "$58.29", f"Ожидалась сумма '$58.29', получено '{total}'"