from aiogram import Bot
import csv
import requests

API_TOKEN = '5812681090:AAGQligbH6ptDWILpvm1WWhBHi7a-DQ4UKA'

with open('test.csv', newline='') as f:
    data = list(csv.DictReader(f))

for user in data:
    if user['isSent']:
        text = "Привет! Отправляй отзыв: как тебе бал, что понравилось, что не понравилось. Может был какой-то смешной момент?🤪 Также я рад фотографиям ))"
        url_send_text = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id=5729660734&text={text}'
        resp = requests.get(url_send_text)
        print(resp.text)

