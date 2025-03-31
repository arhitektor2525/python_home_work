from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def main():
    driver = webdriver.Chrome()

    try:
        driver.get("http://uitestingplayground.com/classattr")

        wait = WebDriverWait(driver, 10)

        blue_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary"))
        )

        blue_button.click()

        time.sleep(2)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()