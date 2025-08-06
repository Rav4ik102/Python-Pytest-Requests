# 1.Создать покемона
import requests

# Актуальный URL
url = "https://api.pokemonbattle.ru/v2/pokemons"

# Хэдеры
headers = {
    "trainer_token": "4217283cb92f046e9e86d503ecf60839"
}

# Тело запроса
payload = {
    "name": "Бот",
    "photo_id": -1
}

# POST-запрос на создание покемона
response = requests.post(url, json=payload, headers=headers)

# Вывод
print("Ответ сервера:", response.status_code)
try:
    print("Тело ответа:", response.json())
except ValueError:
    print("Ответ не в формате JSON:", response.text)



# 2.Изменить имя покемона
import requests

# Актуальный URL
url = "https://api.pokemonbattle.ru/v2/pokemons"

headers = {
    "trainer_token": "4217283cb92f046e9e86d503ecf60839"
}

# Смена имени покемона (PUT)
rename_payload = {
    "pokemon_id": "347573",
    "name": "Генератор",
    "photo_id": -1
}

rename_response = requests.put("https://api.pokemonbattle.ru/v2/pokemons", json=rename_payload, headers=headers)

print("Смена имени — статус:", rename_response.status_code)
print("Ответ:", rename_response.json())



# 3.Поймать в покебол
import requests

# Актуальный URL
url = "https://api.pokemonbattle.ru/v2/pokemons"

headers = {
    "trainer_token": "4217283cb92f046e9e86d503ecf60839"
}

#Поймать в покебол POST
catch_payload = {
    "pokemon_id": "347573"
}

catch_response = requests.post("https://api.pokemonbattle.ru/v2/trainers/add_pokeball", json=catch_payload, headers=headers)

print("Поймать в покебол — статус:", catch_response.status_code)
print("Ответ:", catch_response.json())