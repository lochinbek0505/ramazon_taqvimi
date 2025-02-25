from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "7981476993:AAHjGHZVxwx1FTPuUoBITJAUHMZ3lDIxb1o"
WEB_APP_URL = "https://namoz-time.web.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="🌍 Web App-ni ochish", web_app=types.WebAppInfo(url=WEB_APP_URL))],
        ],
        resize_keyboard=True
    )
    await message.answer("👋 Assalomu alaykum! Web App-ni ochish uchun tugmani bosing:", reply_markup=keyboard)

async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
