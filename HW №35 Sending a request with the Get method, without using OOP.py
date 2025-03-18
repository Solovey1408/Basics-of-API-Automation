import requests  # Импортирование библиотеки для отправки запросов к API

# URL для отправки запросов
url = 'https://api.chucknorris.io/jokes/SaNhjgqeRIOFxoZIELJekA'
print(url)  # Вывод URL

# Отправка запроса GET
result = requests.get(url)
print('Status Code: ' + str(result.status_code))  # Вывод статус-кода запроса

# Проверка статуса ответа
assert 200 == result.status_code

# Дополнительная проверка статуса кода с помощью условия
if result.status_code == 200:
    print('Success Status Code Correct')
else:
    print('Failed Status Code Not Correct')

# Установка кодировки для корректного отображения текста
result.encoding = 'utf-8'

# Вывод тела ответа в JSON формате
print(result.text)