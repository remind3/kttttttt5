from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Укажи свой путь к geckodriver.exe
GECKODRIVER_PATH = r"C:\Users\danich\Downloads\geckodriver-v0.36.0-win64\geckodriver.exe"
admin_url = "http://localhost/opencart/admin"

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=Service(GECKODRIVER_PATH), options=options)
driver.maximize_window()

try:
    # Вход в админку
    driver.get(admin_url)
    driver.find_element(By.ID, "input-username").send_keys("admin")
    driver.find_element(By.ID, "input-password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Закрытие предупреждения, если есть
    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
    except:
        pass

    # Создание категории Devices
    driver.find_element(By.ID, "menu-catalog").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Categories").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[data-bs-original-title='Add New']").click()
    driver.find_element(By.ID, "input-name-1").send_keys("Devices")
    driver.find_element(By.ID, "input-meta-title-1").send_keys("Devices Meta")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    # Добавление товаров
    driver.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(2)

    def add_product(name):
        driver.find_element(By.CSS_SELECTOR, "a[data-bs-original-title='Add New']").click()
        driver.find_element(By.ID, "input-name-1").send_keys(name)
        driver.find_element(By.ID, "input-meta-title-1").send_keys(f"{name} Meta")
        driver.find_element(By.LINK_TEXT, "Data").click()
        driver.find_element(By.ID, "input-model").send_keys(name.lower())
        driver.find_element(By.LINK_TEXT, "Links").click()
        driver.find_element(By.ID, "input-category").send_keys("Devices")
        time.sleep(1)
        driver.find_element(By.ID, "input-category").send_keys(Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

    for item in ["Mouse A", "Mouse B", "Keyboard A", "Keyboard B"]:
        add_product(item)

    # Проверка на главной странице
    driver.get("http://localhost/opencart/")
    time.sleep(2)
    for term in ["Mouse A", "Keyboard B"]:
        search_box = driver.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys(term)
        driver.find_element(By.CSS_SELECTOR, "#search button").click()
        time.sleep(2)

    # Удаление 1 мыши и 1 клавиатуры
    driver.get(admin_url)
    time.sleep(2)
    driver.find_element(By.ID, "menu-catalog").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT, "Products").click()
    time.sleep(2)

    def delete_product(name):
        driver.find_element(By.NAME, "filter_name").clear()
        driver.find_element(By.NAME, "filter_name").send_keys(name)
        driver.find_element(By.ID, "button-filter").click()
        time.sleep(1)
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.CSS_SELECTOR, "button[data-bs-original-title='Delete']").click()
        driver.switch_to.alert.accept()
        time.sleep(2)

    for name in ["Mouse A", "Keyboard A"]:
        delete_product(name)

    # Повторная проверка поиска
    driver.get("http://localhost/opencart/")
    time.sleep(2)
    for term in ["Mouse A", "Keyboard A", "Mouse B", "Keyboard B"]:
        search_box = driver.find_element(By.NAME, "search")
        search_box.clear()
        search_box.send_keys(term)
        driver.find_element(By.CSS_SELECTOR, "#search button").click()
        time.sleep(2)

finally:
    driver.quit()