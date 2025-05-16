import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage


@pytest.fixture
def driver() -> webdriver.Chrome:
    """
    Фикстура для инициализации и завершения работы драйвера.

    Yields:
        Экземпляр Chrome WebDriver
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Тестирование калькулятора")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка операции сложения с задержкой")
def test_calculator_addition(driver: webdriver.Chrome) -> None:
    """Тест проверяет корректность выполнения операции 7 + 8 с задержкой."""
    page = CalculatorPage(driver)

    with allure.step("Подготовка тестового окружения"):
        page.open()
        page.set_delay(4)  # 4 секунды задержки

    with allure.step("Выполнение вычисления 7 + 8"):
        for button in ["7", "+", "8", "="]:
            page.click_button(button)

    with allure.step("Проверка результата"):
        # Ждем появления результата с учетом задержки
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        result = page.get_result()
        assert result == "15", f"Ожидался результат 15, получено {result}"