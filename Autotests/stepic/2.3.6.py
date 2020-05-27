from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    el = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(el)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()