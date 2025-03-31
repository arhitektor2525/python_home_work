from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()


driver = webdriver.Firefox(options=firefox_options)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    flash_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    message_text = flash_message.text.strip()
    print("Текст сообщения:", message_text)

finally:
    driver.quit()