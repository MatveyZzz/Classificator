import requests
import os

# Конфигурация ключей
API_KEY = "ajekb8lgaglvnbhdkrut"
SECRET_KEY = "AQVN1ForBUK_uuLab92XzKrx-ORjoOuiAAmu2jCM"
API_URL = "https://yagpt.yourapiurl.com/v1/endpoint"  # Замените на реальный URL API YaGPT


# Функция для отправки текста в YaGPT
def send_to_yagpt(text: str) -> str:
    headers = {
        "Authorization": f"Bearer {SECRET_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-model",  # Замените на нужную модель
        "input": text,
    }
    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["response"]  # Замените ключ на реальный
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return ""


# Парсер отзывов
def cleaner(n: str) -> str:
    junk = ["<p>", "</p>", "<ul>", "</ul>", "\\r\\n", "<li>", "</li>", "\\r\\n\\r\\n", "\xa0"]
    for junkpiece in junk:
        n = n.replace(junkpiece, "")
    n = n.replace("\n", " ")
    return n


reviews = {}
for page in range(1, 3):
    url = f"https://www.banki.ru/services/responses/list/ajax/?page={page}&type=all&bank=promsvyazbank"
    response = requests.get(url).json()
    data = response["data"]

    for review_data in data:
        review_id = review_data["id"]
        review_text = cleaner(review_data["text"])
        reviews[review_id] = review_text

# Отправляем отзывы в YaGPT и печатаем результаты
for review_id, review_text in reviews.items():
    print(f"Review ID: {review_id}")
    print(f"Original Review: {review_text}")
    yagpt_response = send_to_yagpt(review_text)
    print(f"YaGPT Response: {yagpt_response}")
    print("===============================")
