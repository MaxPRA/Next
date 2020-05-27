from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
browser.get("https://pyeoptics.com/")


def test_ya(driver):
    ya = browser.find_element_by_xpath("//div[contains(@class, 'common-header-main-menu')][4]/a")   # здесь
    return ya

test = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'common-header-main-menu')][4]/a"
    )
))
test.click()

def kl_ik(driver):
    ik = browser.find_element_by_xpath("//div[contains(@class, 'plugin-text')]/p[2]/a")   # здесь
    return ik

kl = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-text')]/p[2]/a"
    )
))
kl.click()

def na_me(driver):
    me = browser.find_element_by_xpath("//span[contains(@class, 'ant-form-item-children')]/input")   # ваше имя
    return me

na = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//span[contains(@class, 'ant-form-item-children')]/input"
    )
))
na.click()
na.send_keys("Viktor")

def mail_inp(driver):
    inp = browser.find_element_by_name("email")     # поле email
    return inp
mail = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "email"
    )
))
mail.click()
mail.send_keys("testpyeoptics@yandex.ru")     #ввод

def phone_number(driver):
    number= browser.find_element_by_name("name")     # поле телефон
    return number
phone= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "phone"
    )
))
phone.click()
phone.send_keys("9119324960")     #ввод





# успеваем скопировать код
time.sleep(3)
# закрываем браузер после всех манипуляций
browser.quit()

#пустая строку в конце файла
