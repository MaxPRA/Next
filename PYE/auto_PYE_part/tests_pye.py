import unittest
import pytest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os
import math


class MyTestCase(unittest.TestCase):
    def test_1(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/")

        def add_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains(@class, 'common-header__content-search')]")  # кнопка поиска
            return button

        add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'common-header__content-search')]"
            )
        ))
        add.click()

        def inp_sear(driver):
            sear = browser.find_element_by_name("query")  # поле для ввода
            return sear

        inp = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "query"
            )
        ))
        inp.click()
        inp.send_keys('36')  # ввод

        def model_sear(driver):
            sear = browser.find_element_by_xpath(
                "//div[@class='common-header-search__results-more']/a")  # показать все результата (кликнуть по модели сразу не получается)
            return sear

        model = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='common-header-search__results-more']/a"  # открывается окно с результатами
            )
        ))
        model.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        #self.assertEqual(True, False)

    def test_2(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/")

        def test_ya(driver):
            ya = browser.find_element_by_xpath("//div[contains(@class, 'common-header-main-menu')][4]/a")  # здесь
            return ya

        test = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'common-header-main-menu')][4]/a"
            )
        ))
        test.click()

        def kl_ik(driver):
            ik = browser.find_element_by_xpath("//div[contains(@class, 'plugin-text')]/p[2]/a")  # здесь
            return ik

        kl = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-text')]/p[2]/a"
            )
        ))
        kl.click()

        def na_me(driver):
            me = browser.find_element_by_xpath("//span[contains(@class, 'ant-form-item-children')]/input")  # ваше имя
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
        phone.send_keys("9119324960")  # ввод
        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        #self.assertEqual(True, False)

    def test_3(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/shop/catalogue/?lense-color=15")

        def filter_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__headline-trigger')]/span[2]")  # кнопка фильтр
            return button

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__headline-trigger')]/span[2]"
            )
        ))
        filter.click()

        def filter_one(driver):
            one = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item-options-item')][1]")  # круглые
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
            two = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _small')]/div/div[2]")  # размер м
            return two

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # размер м
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _small')]/div/div[2]"
            )
        ))
        filter.click()

        # b = browser.find_element_by_css_selector('.common-filters__list-item_small > div.common-filters__list-item-options > div:nth-child(2)').click()     #размер м

        def filter_three(driver):
            three = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[1]")
            return three

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # чёрный
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[1]"
            )
        ))
        filter.click()

        # c = browser.find_element_by_css_selector('.common-filters__list-item_wide > div.common-filters__list-item-options > div:nth-child(1)').click()  # чёрный

        def filter_four(driver):
            four = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[2]")
            return four

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # серый
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[2]"
            )
        ))
        filter.click()

        # d = browser.find_element_by_css_selector('.common-filters__list-item-options > div:nth-child(4)').click()    #серый

        def filter_five(driver):
            five = browser.find_element_by_xpath(
                "//div[contains(@class, 'filters__list-item-options-item_decorated')][7]")
            return five

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # зелёный
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[7]"
            )
        ))
        filter.click()

        # e = browser.find_element_by_css_selector('.common-filters__list-item-options > div:nth-child(8)').click()   #зелёный

        def filter_six(driver):
            six = browser.find_element_by_xpath(
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[3]")
            return six

        filter = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # кристальный
            (
                By.XPATH,
                "//div[contains(@class, 'plugin-common-catalog-filters__content-list-item _wide')]/div/div[3]"
            )
        ))
        filter.click()
        # f = browser.find_element_by_css_selector('.common-filters__list-item_wide > div.common-filters__list-item-options > div:nth-child(3)').click()  #кристальный

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        #self.assertEqual(True, False)

    def test_4(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/")

        def entrance_button(driver):
            button = browser.find_element_by_xpath("//div[contains(@class, 'common-header__content-auth')]")  #
            return button

        entrance = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'common-header__content-auth')]"
            )
        ))
        entrance.click()

        def username_field(driver):
            field = browser.find_element_by_name("email")  # поле email
            return field

        username = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "email"
            )
        ))
        username.click()
        username.send_keys("testpyeoptics@yandex.ru")  # ввод

        def password_field(driver):
            field = browser.find_element_by_name("password")  # поле пароль
            return field

        password = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "password"
            )
        ))
        password.click()
        password.send_keys("qwerty123")  # ввод

        def done_button(driver):
            button = browser.find_element_by_xpath("//button[contains(@class, 'ui-button')]")  # готово вход
            return button

        done = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//button[contains(@class, 'ui-button')]"
            )
        ))
        done.click()

        def is_user_authorized(driver):
            username = driver.find_element_by_xpath(
                "//a[contains(@class, 'common-header__content-auth') and @href='/cabinet']")
            return username

        user = WebDriverWait(browser, 10).until(is_user_authorized)
        user.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        #self.assertEqual(True, False)

    def test_5(self):
        browser = webdriver.Chrome()
        browser.get("https://pyeoptics.com/shop/catalogue/?lense-color=14")

        def pye_optics(driver):
            optics = browser.find_element_by_xpath(
                "//a[(@class = 'common-card-product') and @href='/shop/catalogue/polo_6134/']")  # модель очков из появ. списка
            return optics

        pye = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//a[(@class = 'common-card-product') and @href='/shop/catalogue/polo_6134/']"
            )
        ))
        pye.click()

        def add_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-item__info-buttons-item')][1]")  # добавить в корзину
            return button

        add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-item__info-buttons-item')][1]"
            )
        ))
        add.click()

        def per_oforml(driver):
            oforml = browser.find_element_by_xpath(
                "//a[contains(@class, 'page-item__cart-buttons-item')]")  # перейти к оформлению
            return oforml

        per = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@class, 'page-item__cart-buttons-item')]"
            )
        ))
        per.click()

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
                "//div[contains(@class, 'page-checkout-step-auth__body-step-buttons')]")  # продолжить
            return p

        cont = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-auth__body-step-buttons')]"
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

        def sam_mosk(driver):
            mosk = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div")  # выбрать примерку
            return mosk

        sam = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div"
            )
        ))
        sam.click()

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
        stree.send_keys("Проспект строителей")  # ввод

        def ho_me(driver):
            me = browser.find_element_by_name("name")  # дом
            return me

        ho = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "house"
            )
        ))
        ho.click()
        ho.send_keys("2")  # ввод

        def k_s(driver):
            s = browser.find_element_by_name("name")  # корпус
            return s

        k = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "building"
            )
        ))
        k.click()
        k.send_keys("6")  # ввод

        def apa_rt(driver):
            rt = browser.find_element_by_name("name")  # корпус
            return rt

        apa = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "apartment"
            )
        ))
        apa.click()
        apa.send_keys("777")  # ввод

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
        phone.send_keys("9119324960")  # ввод

        def prodo_p(driver):
            p = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-buttons-item')]")
            return p  # продолжить

        prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-buttons-item')]"
            )
        ))
        prodo.click()

        def prim_erka(driver):
            erka = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-step-payment__body-step-form-options-item-info')]/span[2]")
            return erka

        prim = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # только оправу
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-payment__body-step-form-options-item-info')]/span[2]"
            )
        ))
        prim.click()

        def prodo_o(driver):
            o = browser.find_element_by_xpath("//button[contains(@class, 'ui-button _uppercase')]")
            return o  # продолжить

        prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # продолжить
            (
                By.XPATH,
                "//button[contains(@class, 'ui-button _uppercase')]"
            )
        ))
        prodo.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()