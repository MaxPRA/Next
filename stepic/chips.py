# успеваем скопировать код   time.sleep(5)
# закрываем браузер после всех манипуляций      browser.quit()
# browser.execute_script("window.scrollBy(0, 100);")      прокрутка


  # current_dir = os.path.abspath(os.path.dirname(__file__))
 #  file_path = os.path.join(current_dir, 'file.txt')

# browser.switch_to.alert переключение на alert сообщение в браузере

 #                                          Полезные ссылки


#  https://stepik.org/lesson/171979/step/1?unit=146657
   #    https://habr.com/ru/post/358950/ пирамида тестов 2018 г статья
# https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36   f string
# https://medium.com/nuances-of-programming   Статья про модульное тестирование
# https://stepik.org/lesson/187065/step/12?unit=161976 обязательная инфа + подтянуть работу с гит
#  https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc - про pytest более углубленно
#  https://habr.com/ru/post/132554/ - - как работает yield  --- teardown
# https://habr.com/ru/company/yandex/blog/242795/    ФИКСТУРЫ
# https://docs.pytest.org/en/latest/fixture.html    ФИКСТУРЫ
#
#
#
#
#
#
#
#
#
#
#



#    генератор выполняется до тех пор пока не встретит yield,
#    после этого он останавливает выполнение и возвращает значение, потом можно снова вызвать генератор и он продолжит
#    свое выполнение до тех пор пока не дойдет до конца кода генератора,
#    если код не скрывать и я все правильно понимаю, то это нечто следующее:
                                #РАБОТА ГЕНЕРАТОРА
# def simple_generator():
#      print('generator starts working')
#      yield 42
#      print('generator stopped working')
#
# gen = simple_generator()
# value = next(gen)
# print(value)
#
# # Тут появится исключение StopIteration и генератор закончит свое выполнение, кроме того, если
# # захотим снова использовать генератор, то придется создавать новый объект генератора, потому что # прошлый истощился
# next(gen)
#
# # Из-за возникновения StopIteration генераторы можно использовать в цикле for и тут
# # StopIteration будет скрыт циклом
# for i in simple_generator(): pass
# И yield может быть несколько, не обязательно один и каждый раз работа его будет приостанавливаться





#           Например, для проверки того, что в текущем url содержится строка login:

 # assert "login" in browser.current_url, # сообщение об ошибке



# подсчет математической функции
# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
# x = browser.find_element_by_id("input_value").text
# y = calc(x)
# browser.find_element_by_id('answer').send_keys(y)
#  browser.find_element_by_class_name('btn-primary').click()

# Копирование числа из алерта в буфер обмена
# alert = browser.switch_to.alert
# alert_text = alert.text
# addToClipBoard = alert_text.split(': ')[-1]
# pyperclip.copy(addToClipBoard)