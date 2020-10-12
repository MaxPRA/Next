import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):
    def test_7(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/shop/catalogue/pye-x-fakoshima-kaguya_5892/")

        def add_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains (@class, 'page-item-common__buttons-item')][2]/button")  # добавить в примерку
            return button

        add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains (@class, 'page-item-common__buttons-item')][2]/button"
            )
        ))
        add.click()

        def of_prim(driver):
            prim = browser.find_element_by_xpath(
                "//a[contains(@class, 'sideblock-fitting__button-link')]/button")
            return prim

        of = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@class, 'sideblock-fitting__button-link')]/button"
            )
        ))
        of.click()

        def mail_inp(driver):
            inp = browser.find_element_by_name("email")  # поле email
            return inp

        mail = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "email"
            )
        ))
        mail.click()
        mail.send_keys("testpyeoptics@yandex.ru")  # ввод

        def cont_p(driver):
            p = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-fitting-step-auth__body-step-buttons')]/div")  # продолжить
            return p

        cont = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-fitting-step-auth__body-step-buttons')]/div"
            )
        ))
        cont.click()

        def prod_gost(driver):
            gost = browser.find_element_by_xpath(
                "//button[contains(@class,'ui-button _bordered')]")  # продолжить как гость работает
            return gost

        prod = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class,'ui-button _bordered')]"
            )
        ))
        prod.click()

        def stree_t(driver):
            t = browser.find_element_by_name("name")  # улица
            return t

        stree = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "street"
            )
        ))
        stree.click()
        stree.send_keys("main")  # ввод

        def ho_me(driver):
            me = browser.find_element_by_name(
                "house")
            return me

        ho = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "house"
            )
        ))
        ho.click()
        ho.send_keys("88")

        def name_n(driver):
            n = browser.find_element_by_name("name")  # поле имя фамилия
            return n

        name = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "name"
            )
        ))
        name.click()
        name.send_keys("Как найти Xpath ****")  # ввод

        def phone_number(driver):
            number = browser.find_element_by_name("name")  # поле телефон
            return number

        phone = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "phone"
            )
        ))
        phone.click()
        phone.send_keys("79119324960")  # ввод

        def prodo_p(driver):
            p = browser.find_element_by_xpath(
                "//button")
            return p  # продолжить

        prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//button"
            )
        ))
        prodo.click()

        def con_tin(driver):  # понятно продожить
            tin = browser.find_element_by_xpath(
                "//div[contains (@class, 'page-fitting-step-payment__body-step-buttons')]/div")
            return tin  # продолжить

        con = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains (@class, 'page-fitting-step-payment__body-step-buttons')]/div"
            )
        ))
        con.click()

        # успеваем скопировать код
        time.sleep(15)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
