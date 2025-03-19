import requests  # Импортирование библиотеки для отправки запросов к API

#Создание общего класса, который содержит метод для работы нашего теста
class TestCreateJoke:

    # URL для отправки запросов
    url = 'https://official-joke-api.appspot.com'

    #Создание метода для теста
    def test_create_random_joke(self):

        types = 'general' # Значение типа шутки type:'general'
        path_random_joke_general = f'/jokes/{types}/random' # Путь до эндпоинта
        url_random_joke_general = self.url + path_random_joke_general # Формирование полного URL
        print(url_random_joke_general)  # Вывод URL

        # Отправка запроса GET
        result = requests.get(url_random_joke_general)
        print(result.json())

        print(f'Status Code: {result.status_code}')  # Вывод статус-кода запроса

        # Сравнение фактического статус кода с ожидаемым
        assert result.status_code == 200, 'Status Code Not Correct'
        print('Status Code Correct')

        # Проверка на присутствие поля type в json-ответе
        check_joke = result.json()
        joke_type = check_joke[0].get('type')
        print(joke_type)

        # Проверка ключа type
        joke_category = check_joke[0].get('type')
        assert joke_category == types, 'Test Failed'
        print('Test Success')

        # Получение текста сетапа шутки из ответа
        check_setup_text = check_joke[0].get('setup')
        print(check_setup_text)

        # Получение текста панчлайна шутки из ответа
        check_punchline_text = check_joke[0].get('punchline')
        print(check_punchline_text)

        # Слово, которое нужно найти
        name_in_joke = 'Chuck'

        #Ищем Chuck в сетапе и панчлайне шутки
        if name_in_joke in check_setup_text:
            print(f'Chuck is found in {check_setup_text}')
        elif name_in_joke in check_punchline_text:
            print(f'Chuck is found in {check_punchline_text}')
        else:
            print(f'Chuck is not found in joke')

start = TestCreateJoke() # Создание экземпляра класса
start.test_create_random_joke() # Вызов метода