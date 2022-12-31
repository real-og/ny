from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import csv

logging.basicConfig(level=logging.INFO)

def get_user_by_id(id):
    data = get_data()
    for i in data:
        if i['id'] == str(id):
            return i

def get_data() -> list(dict()):
    with open('test.csv', newline='') as f:
        return list(csv.DictReader(f))

# API_TOKEN = str(os.environ.get('BOT_TOKEN'))
API_TOKEN = '5812681090:AAGQligbH6ptDWILpvm1WWhBHi7a-DQ4UKA'
TARGET_CHAT_ID = '277961206'

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(content_types=['any'])
async def choose_cost(message: types.Message):
    await message.answer("<strong>Отзыв принят</strong>\n Всего самого лучшего в Новом году🥽⛄️", parse_mode='HTML')
    user = get_user_by_id(message.from_id)
    await bot.send_message(chat_id=TARGET_CHAT_ID, text=f"<strong>Отправил</strong>\n{user['name']}", parse_mode='HTML')
    await bot.forward_message(chat_id=TARGET_CHAT_ID, from_chat_id=message.from_id, message_id=message.message_id)
    

if __name__ == '__main__':
    print("Starting")
    executor.start_polling(dp, skip_updates=True)
    