import requests

base_url = "http://3.21.164.220/"
id = "0xa32eAC7b4814d5EeC99EB1BAa5275660007D7328"
headers = {
    "Authorization": f"Bearer {id}",
    "Content-Type": "application/json"
}

def get_resource(resource_path, params=None):
    url = f"{base_url}/{resource_path}"
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибка при выполнении GET-запроса: {response.status_code}")
        return None

def post_resource(resource_path, payload):
    url = f"{base_url}/{resource_path}"
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        data = response.json()
        return data
    else:
        print(f"Ошибка при выполнении POST-запроса: {response.status_code}")
        return None

def put_resource(resource_path, payload):
    url = f"{base_url}/{resource_path}"
    response = requests.put(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Ошибка при выполнении PUT-запроса: {response.status_code}")
        return None

def go_1():
    # Получение списка пользователей с параметрами
    endpoint = "users"
    params = {
        "status": "active",
        "page": 1,
        "per_page": 10
    }
    users = get_resource(endpoint, params=params)
    if users:
        for user in users:
            print(user)

def go_2():
    # Получение отдельного пользователя
    user_id = 1
    endpoint = f"users/{user_id}"
    user = get_resource(endpoint)
    if user:
        print("Пользователь:", user)

def go_3():
    # Обновление пользователя
    user_id = 1
    endpoint = f"users/{user_id}"
    updated_user = {
        "name": data.name,
        "email": data.email
    }
    updated_user = put_resource(endpoint, updated_user)
    if updated_user:
        print("Обновленный пользователь:", updated_user)

print("DECENTRATHON 2023 | Task3 | Author: Исяновы Team")
print(
"""
Команды:
 ___________________________________
|1) Получить список пользователей   |
|2) Получить отдельного пользователя|
|3) Обновление пользователя         |
-------------------------------------
""")

com=0
def input_com():
    print("\n")
    com=int(input("Выбор команды 1-3:"))
    
    if com<1 or com>4:
        print("\n")
        input_com()
    elif com==1:
        go_1()
        input_com()
    elif com==2:
        go_2()
        input_com()
    elif com==3:
        go_3()
        input_com()
input_com()

