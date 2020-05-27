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