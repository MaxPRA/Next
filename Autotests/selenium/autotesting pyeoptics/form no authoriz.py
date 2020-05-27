from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


browser = webdriver.Chrome()
browser.get("https://pyeoptics.com/shop/catalogue/?lense-color=14")

def pye_optics(driver):
    optics = browser.find_element_by_xpath("//a[(@class = 'common-card-product') and @href='/shop/catalogue/polo_6134/']")   # модель очков из появ. списка
    return optics

pye = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//a[(@class = 'common-card-product') and @href='/shop/catalogue/polo_6134/']"
    )
))
pye.click()

def add_button(driver):
    button = browser.find_element_by_xpath("//div[contains(@class, 'page-item__info-buttons-item')][1]")   # добавить в корзину
    return button

add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
 (
        By.XPATH,
        "//div[contains(@class, 'page-item__info-buttons-item')][1]"
    )
))
add.click()

def per_oforml(driver):
    oforml = browser.find_element_by_xpath("//a[contains(@class, 'page-item__cart-buttons-item')]")   #  перейти к оформлению
    return oforml

per = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.XPATH,
        "//a[contains(@class, 'page-item__cart-buttons-item')]"
    )
))
per.click()

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

def cont_p(driver):
    p = browser.find_element_by_xpath("//div[contains(@class, 'page-checkout-step-auth__body-step-buttons')]")   #  продолжить
    return p

cont = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.XPATH,
        "//div[contains(@class, 'page-checkout-step-auth__body-step-buttons')]"
    )
))
cont.click()

def prod_gost(driver):
    gost = browser.find_element_by_xpath("//button[contains(@class,'ui-button _bordered')]")   #  продолжить как гость работает
    return gost

prod = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.XPATH,
        "//button[contains(@class,'ui-button _bordered')]"
    )
))
prod.click()

def sam_mosk(driver):
    mosk = browser.find_element_by_xpath("//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div")   #  выбрать примерку
    return mosk

sam = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.XPATH,
        "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div"
    )
))
sam.click()

def stree_t(driver):
    t = browser.find_element_by_name("name")     # улица
    return t
stree= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "street"
    )
))
stree.click()
stree.send_keys("Проспект строителей")     #ввод

def ho_me(driver):
    me = browser.find_element_by_name("name")     # дом
    return me
ho= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "house"
    )
))
ho.click()
ho.send_keys("2")     #ввод

def k_s(driver):
    s = browser.find_element_by_name("name")     # корпус
    return s
k= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "building"
    )
))
k.click()
k.send_keys("6")     #ввод

def apa_rt(driver):
    rt = browser.find_element_by_name("name")     # корпус
    return rt
apa= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "apartment"
    )
))
apa.click()
apa.send_keys("777")     #ввод

def name_n(driver):
    n = browser.find_element_by_name("name")     # поле имя фамилия
    return n
name= WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.NAME,
        "name"
    )
))
name.click()
name.send_keys("Как найти Xpath ****")     #ввод

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

def prodo_p(driver):
    p = browser.find_element_by_xpath("//div[contains(@class, 'page-checkout-step-shipping__body-step-buttons-item')]")
    return p   #  продолжить

prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
    (
        By.XPATH,
        "//div[contains(@class, 'page-checkout-step-shipping__body-step-buttons-item')]"
    )
))
prodo.click()

def prim_erka(driver):
    erka = browser.find_element_by_xpath("//div[contains(@class, 'page-checkout-step-payment__body-step-form-options-item-info')]/span[2]")
    return erka

prim = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(      #  только оправу
    (
        By.XPATH,
        "//div[contains(@class, 'page-checkout-step-payment__body-step-form-options-item-info')]/span[2]"
    )
))
prim.click()


def prodo_o(driver):
    o = browser.find_element_by_xpath("//button[contains(@class, 'ui-button _uppercase')]")
    return o   #  продолжить

prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(   # продолжить
    (
        By.XPATH,
        "//button[contains(@class, 'ui-button _uppercase')]"
    )
))
prodo.click()


# успеваем скопировать код
time.sleep(8)
# закрываем браузер после всех манипуляций
browser.quit()

#пустая строку в конце файла
