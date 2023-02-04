from _datetime import datetime
from functools import wraps
import bs4
import requests
import fake_headers

# 1
def decorator_one(decorator):
    @wraps(decorator)
    def new_function(*args, **kwargs):
        result = decorator(*args, **kwargs)
        time_date = datetime.now()
        print(f"Функция  выполнена {decorator.__name__}, результат = {result}")
        end = (f"Конец функции {decorator.__name__},{time_date}, аргументы {args} и {kwargs} получается {result} \n")
        with open("decorater.txt", "a", encoding='utf-8') as file:
            file.write(end)
        return decorator(*args, **kwargs)

    return new_function
if __name__ == '__main__':
    answer = int(input("выберите 1 или 2 (1-Сложение, 2-Вычитание): "))
    if answer == 1:
        @decorator_one
        def addition(a, b):
            return a + b
        addition(1, 2)
    if answer == 2:
        @decorator_one
        def subtraction(a, b):
            return a - b
        subtraction(2, 1)



# 2
def logger_path(path):
    def decorator_one(decorator):
        @wraps(decorator)
        def new_function(*args, **kwargs):
            result = decorator(*args, **kwargs)
            time_date = datetime.now()
            way = path
            print(f"Функция  выполнена {decorator.__name__}, результат = {result}")
            end = (f"Конец функции {decorator.__name__},{time_date}, аргументы {args} и {kwargs} получается {result} \n")
            with open(way, "a", encoding='utf-8') as file:
                file.write(end)

            return decorator(*args, **kwargs)

        return new_function
    return decorator_one


if __name__ == '__main__':
    answer = int(input("выберите 1 или 2 (1-Сложение, 2-Вычитание): "))

    if answer == 1:
        @logger_path(input('Введите путь'))
        def addition(a, b):
            return a + b
        addition(1, 2)


    if answer == 2:
        @logger_path(input('Введите путь'))
        def subtraction(a, b):
            return a - b
        subtraction(2, 1)


#3
def logger_path(path):
    def decorator_one(decorator):
        @wraps(decorator)
        def new_function(*args, **kwargs):
            result = decorator(*args, **kwargs)
            KEYWORD = [result]
            URL = 'https://habr.com/ru/all/'
            HEADERS = fake_headers.Headers(browser='chrome', os='win', headers=True).generate()

            respons = requests.get(URL, headers=HEADERS)

            text = respons.text

            soup = bs4.BeautifulSoup(text, features='html.parser')
            articl = soup.find_all('article')
            for art in articl:
                hubs = art.find_all(class_="tm-article-snippet tm-article-snippet")
                hubs = [hub.text.strip() for hub in hubs]
                for hub in hubs:
                    if set(hub.split(' ')) & set(KEYWORD):
                        time_date = datetime.now()
                        href = art.find(class_="tm-article-snippet__title-link").attrs["href"]
                        title = art.find("h2").find("span").text
                        date_ = art.find(class_="tm-article-snippet__datetime-published").text
                        result_url = f'{date_} {title} ==> {URL}{href}'
                        print(f"Функция  выполнена {decorator.__name__}, результат = {result_url}")
                        end = (
                            f"Конец функции {decorator.__name__},{time_date},"
                            f" аргументы {args} и {kwargs} получается {result} \n")
                        way = path
                        with open(way, "a", encoding='utf-8') as file:
                            file.write(end)

            return decorator(*args, **kwargs)

        return new_function
    return decorator_one


if __name__ == '__main__':
        @logger_path(input('Введите путь'))
        def addition(word):
            return word
        addition(input("Введите слова для поиска"))




