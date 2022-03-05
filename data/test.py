from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())  # Получение списка всех работ
print(get('http://localhost:5000/api/jobs/1').json())  # Корректное получение одной работы
print(get('http://localhost:5000/api/jobs/999').json())  # Получение одной работы — неверный id
print(get('http://localhost:5000/api/jobs/q').json())  # Получение одной работы - строка в ID
