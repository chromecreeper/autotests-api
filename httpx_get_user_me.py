import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем POST-запрос к эндпоинту /api/v1/authentication/login
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

# Выводим JSON-ответ и статус-код
print(login_response.status_code)

access_token = login_response_data["token"]["accessToken"]
headers = {
    "Authorization": f"Bearer {access_token}"}

get_user_me_response = httpx.get("http://localhost:8000/api/v1/users/me",headers=headers)
print(get_user_me_response.status_code)
print(get_user_me_response.json())