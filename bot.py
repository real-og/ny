from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging
import db

logging.basicConfig(level=logging.INFO)

# API_TOKEN = str(os.environ.get('BOT_TOKEN'))
API_TOKEN = '5812681090:AAGQligbH6ptDWILpvm1WWhBHi7a-DQ4UKA'
TARGET_CHAT_ID = '277961206'

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot, storage=storage)

class State(StatesGroup):
    choose_name = State()
    choose_company = State()
    get_check = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    db.add_line(id=message.from_id)
    await message.answer("<strong>Привет!</strong>\n Ты регаешься на Новогодний бал БГУИР, вводи своё ФИО", parse_mode='HTML')
    await State.choose_name.set()


@dp.message_handler(state=State.choose_name)
async def choose_name(message: types.Message):
    input = message.text.strip().title()
    db.edit_name(id=message.from_id, name=input)
    await message.answer(f"Ты зареган под именем *{input}*\nТеперь введи название компании, в которую пожертвовал либо кидай ссылку", parse_mode='Markdown')
    await State.choose_company.set()


@dp.message_handler(state=State.choose_company)
async def choose_company(message: types.Message):
    input = message.text.strip()
    db.edit_company(message.from_id, input)
    await message.answer(f"*Отлично!*\nПоследний шаг - пришли подтверждение\n\n_*скорее всего это фото чека_", parse_mode='Markdown')
    await State.get_check.set()
    

@dp.message_handler(state=State.get_check, content_types=['any'])
async def choose_cost(message: types.Message):
    await message.answer("Твой чек отправлен админу, ожидай подтверждения. По вопросам пиши @mlifefor в том числе по уточнению информации")
    await bot.send_message(chat_id=TARGET_CHAT_ID, text='В бота прислали вот:')
    await bot.forward_message(chat_id=TARGET_CHAT_ID, from_chat_id=message.from_id, message_id=message.message_id)
    db.edit_sent_status(message.from_id, True)


@dp.message_handler(text='Да')
async def choose_cos(message: types.Message):
    if TARGET_CHAT_ID == str(message.from_id):
        who = message.reply_to_message.forward_from.id

        db.edit_active_status(who, True)
        await bot.send_message(chat_id=who, text='Поздравляю, тебя подтвердили!')
    

if __name__ == '__main__':
    print("Starting")
    executor.start_polling(dp, skip_updates=True)
    