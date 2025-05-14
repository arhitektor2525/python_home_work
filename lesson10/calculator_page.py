import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: webdriver.Remote) -> None:
        """
        Инициализация класса CalculatorPage.

        Args:
            driver: WebDriver.Remote - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    @allure.step("Установить задержку вычислений в {delay} секунд")
    def set_delay(self, delay: int) -> None:
        """
        Устанавливает задержку вычислений.

        Args:
            delay: int - значение задержки в секундах
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step("Нажать кнопку {button}")
    def click_button(self, button: str) -> None:
        """
        Нажимает указанную кнопку калькулятора.

        Args:
            button: str - текст на кнопке (например, "7", "+", "=")
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Возвращает результат вычисления.

        Returns:
            str - текст результата вычисления
        """
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text