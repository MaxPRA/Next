import pytest
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class MyTestCase(unittest.TestCase):

                                        # ПОИСК НА САЙТЕ
    def test_1(self):
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/")

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
                "//div[@class='common-header-search__results-more']/a")  # показать все результаты (кликнуть по модели сразу не получается)
            return sear

        model = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@class='common-header-search__results-list-item'][1]/a"  # о
            )
        ))
        model.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # self.assertEqual(True, False)

    def test_2(self):                            # ПРОВЕРКА ЗРЕНИЯ всегда падает на staging
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/")

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
            ik = browser.find_element_by_xpath("//div[contains(@class, 'plugin-text')]/p[2]/a")  #
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
        phone.send_keys("79119324960")  # ввод
        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

        # self.assertEqual(True, False)

    def test_3(self):                       # ФИЛЬТРАЦИЯ НА 5+ ФИЛЬТРОВ
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/shop/catalogue/?lense-color=15")

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
        # self.assertEqual(True, False)

    def test_4(self):                   #   АВТОРИЗАЦИЯ И ВХОД В ЛК
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/")

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
        # self.assertEqual(True, False)

    def test_5(self):             # Оофрмление заказа без промокода
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/shop/catalogue/pye-x-fakoshima-franky_5897/")

        def add_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains (@class, 'page-item-common__buttons-item')][1]/button")  # добавить в корзину
            return button

        add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains (@class, 'page-item-common__buttons-item')][1]/button"
            )
        ))
        add.click()

        def per_oforml(driver):
            oforml = browser.find_element_by_xpath(
                "//a[contains(@class, 'sideblock-cart__buttons-item')]")  # перейти к оформлению
            return oforml

        per = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@class, 'sideblock-cart__buttons-item')]"
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
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div")  # выбрать самовывоз
            return mosk

        sam = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div"
            )
        ))
        sam.click()

        def mag_kaz(driver):
            kaz = browser.find_element_by_xpath(
                "//div[contains(@class,'page-checkout-step-shipping__body-step-form')][3]/div[2]/div[1]")  # выбрать казанская
            return kaz

        mag = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'page-checkout-step-shipping__body-step-form')][3]/div[2]/div[1]"
                # выбрать казанская
            )
        ))
        mag.click()

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

        def l_k(driver):
            k = browser.find_element_by_xpath("//div[@class='common-header__content']/div[4]")
            return k

        l = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
               "//div[@class='common-header__content']/div[4]"
            )
        ))
        l.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # self.assertEqual(True, False)

                                    #ПОКУПКА С ПРОМОКОДОМ
    def test_6(self):                # Оофрмление заказа с промокодом
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/shop/catalogue/gosha_5955/")

        def add_button(driver):
            button = browser.find_element_by_xpath(
                "//div[contains (@class, 'page-item-common__buttons-item')][1]/button")  # добавить в корзину
            return button

        add = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains (@class, 'page-item-common__buttons-item')][1]/button"
            )
        ))
        add.click()

        def per_oforml(driver):
            oforml = browser.find_element_by_xpath(
                "//a[contains(@class, 'sideblock-cart__buttons-item')]")  # перейти к оформлению
            return oforml

        per = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//a[contains(@class, 'sideblock-cart__buttons-item')]"
            )
        ))
        per.click()

        def prom_o(driver):
            o = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-cart-promo')]/div")  #
            return o

        prom = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-cart-promo')]/div"
            )
        ))
        prom.click()

        def pro_mo(driver):
            mo = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-cart-promo__form-input')]/input"
            )
            return mo

        pro = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-cart-promo__form-input')]/input"
            )
        ))
        pro.click()
        pro.send_keys("TESTSTAG199520")  # ввод

        def but_promo(driver):
            promo = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-checkout-cart-promo__form-button')]/button"
            )
            return promo

        but = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-cart-promo__form-button')]/button"
            )
        ))
        but.click()

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
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div")  # выбрать самовывоз
            return mosk

        sam = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-checkout-step-shipping__body-step-form')][2]/div/div"
            )
        ))
        sam.click()

        def mag_kaz(driver):
            kaz = browser.find_element_by_xpath(
                "//div[contains(@class,'page-checkout-step-shipping__body-step-form')][3]/div[2]/div[1]")  # выбрать казанская
            return kaz

        mag = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class,'page-checkout-step-shipping__body-step-form')][3]/div[2]/div[1]"
                # выбрать казанская
            )
        ))
        mag.click()

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

        prim = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(  # примерка на дому
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

        def l_k(driver):
            k = browser.find_element_by_xpath("//div[@class='common-header__content']/div[4]")
            return k

        l = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
               "//div[@class='common-header__content']/div[4]"
            )
        ))
        l.click()

        # успеваем скопировать код
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        # self.assertEqual(True, False)

                                            # ПРИМЕРКА
    def test_7(self):               # ПРИМЕРКА
        browser = webdriver.Chrome()
        browser.get("https://dev:dev@staging.pyeoptics.com/shop/catalogue/pye-x-fakoshima-kaguya_5892/")

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
        time.sleep(5)
        def yl_eet(driver):
            eet = browser.find_element_by_name(
                "street")
            return eet

        yl = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.NAME,
                "street"
            )
        ))
        yl.click()
        yl.send_keys("main")

        def ho_use(driver):
            use = browser.find_element_by_name(
                "house")
            return use

        ho = WebDriverWait(browser, 15).until(expected_conditions.element_to_be_clickable(
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
                "//div[contains(@class, 'ui-form__fields-item _third')]/div/div/input")
            return p  # продолжить

        prodo = WebDriverWait(browser, 10).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-fitting-step-shipping__body-step-buttons')]/div"
            )
        ))
        prodo.click()

        def con_tin(driver):  # понятно продожить
            tin = browser.find_element_by_xpath(
                "//div[contains(@class, 'page-fitting-step-payment__body-step-buttons-item')]/button")
            return tin  # продолжить

        con = WebDriverWait(browser, 50).until(expected_conditions.element_to_be_clickable(
            (
                By.XPATH,
                "//div[contains(@class, 'page-fitting-step-payment__body-step-buttons-item')]/button"
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
