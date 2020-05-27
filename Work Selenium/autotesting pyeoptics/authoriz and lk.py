from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome()
browser.get("https://pyeoptics.com/")

def entrance_button(driver):
    button = browser.find_element_by_xpath("//div[contains(@class, 'common-header__content-auth')]")    #
    return button

entrance = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'common-header__content-auth')]"
    )
))
entrance.click()


def username_field(driver):
    field = browser.find_element_by_name("email")    # поле email
    return field

username = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.NAME,
        "email"
    )
))
username.click()
username.send_keys("testpyeoptics@yandex.ru")     #ввод


def password_field(driver):
    field = browser.find_element_by_name("password")    #поле пароль
    return field


password = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.NAME,
        "password"
    )
))
password.click()
password.send_keys("qwerty123")    #ввод


def done_button(driver):
    button = browser.find_element_by_xpath("//button[contains(@class, 'ui-button')]")    #готово вход
    return button

done = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//button[contains(@class, 'ui-button')]"
    )
))
done.click()

def is_user_authorized(driver):
    username = driver.find_element_by_xpath("//a[contains(@class, 'common-header__content-auth') and @href='/cabinet']")
    return username

user = WebDriverWait(browser, 10).until(is_user_authorized)
user.click()




# успеваем скопировать код
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

#пустая строку в конце файла
