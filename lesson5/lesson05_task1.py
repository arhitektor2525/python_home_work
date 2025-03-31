from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Открыть браузер Google Chrome
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Перейти на страницу
    driver.get("http://uitestingplayground.com/dynamicid")

    # Ожидать появления кнопки (до 10 секунд) и кликнуть
    blue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn"))
    )
    blue_button.click()

    print("✅ Кнопка успешно нажата!")

    # Небольшая задержка для визуальной проверки
    input("Нажмите Enter для закрытия браузера...")

finally:
    # Закрыть браузер
    driver.quit()
