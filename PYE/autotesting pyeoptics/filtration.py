from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
browser.get("https://pyeoptics.com/shop/catalogue/?lense-color=15")

def filter_button(driver):
    button = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__headline-trigger')]/span[2]")    # кнопка фильтр
    return button

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__headline-trigger')]/span[2]"
    )
))
filter.click()




def filter_one(driver):
    one = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__content-list-item-options-item')][1]")    #   круглые
    return one

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item-options-item')][1]"
    )
))
filter.click()
# a = browser.find_element_by_css_selector('.common-filters__list-item-options-item-text').click()   #круглые

def filter_two(driver):
    two = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _small')]/div/div[2]")    #   размер м
    return two

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(    #размер м
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _small')]/div/div[2]"
    )
))
filter.click()
# b = browser.find_element_by_css_selector('.common-filters__list-item_small > div.common-filters__list-item-options > div:nth-child(2)').click()     #размер м

def filter_three(driver):
    three = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[1]")
    return three

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(       # чёрный
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[1]"
    )
))
filter.click()
# c = browser.find_element_by_css_selector('.common-filters__list-item_wide > div.common-filters__list-item-options > div:nth-child(1)').click()  # чёрный

def filter_four(driver):
    four = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[2]")
    return four

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(   #серый
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[2]"
    )
))
filter.click()
# d = browser.find_element_by_css_selector('.common-filters__list-item-options > div:nth-child(4)').click()    #серый

def filter_five(driver):
    five = browser.find_element_by_xpath("//div[contains(@class, 'filters__list-item-options-item_decorated')][7]")
    return five

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  #зелёный
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[7]"
    )
))
filter.click()
# e = browser.find_element_by_css_selector('.common-filters__list-item-options > div:nth-child(8)').click()   #зелёный

def filter_six(driver):
    six = browser.find_element_by_xpath("//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[3]")
    return six

filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(       #  кристальный
 (
        By.XPATH,
        "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[3]"
    )
))
filter.click()
# f = browser.find_element_by_css_selector('.common-filters__list-item_wide > div.common-filters__list-item-options > div:nth-child(3)').click()  #кристальный



# успеваем скопировать код
time.sleep(20)
# закрываем браузер после всех манипуляций
browser.quit()

#пустая строку в конце файла
