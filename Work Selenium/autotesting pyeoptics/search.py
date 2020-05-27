import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get("https://pyeoptics.com/")

def add_button(driver):
    button = browser.find_element_by_xpath("//div[contains(@class, 'common-header__content-search')]")    #   кнопка поиска
    return button

add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'common-header__content-search')]"
    )
))
add.click()

def inp_sear(driver):
    sear = browser.find_element_by_name("query")    #   поле для ввода
    return sear

inp = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.NAME,
        "query"
    )
))
inp.click()
inp.send_keys('36')         #ввод

def model_sear(driver):
    sear = browser.find_element_by_xpath("//div[@class='common-header-search__results-more']/a")    #   показать все результата (кликнуть по модели сразу не получается)
    return sear

model = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[@class='common-header-search__results-more']/a"     # открывается окно с результатами
    )
))
model.click()


# успеваем скопировать код
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

#пустая строку в конце файла
