from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")

    blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    blue_button.click()

    print("Кнопка успешно нажата!")
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

finally:
    driver.quit()