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
    await message.answer(
    "👋 Assalomu alaykum!\n\n"
    "Web App-ni ochish uchun tugmani bosing:\n"
    "📲 Bizning ilovamizni yuklab oling(https://t.me/ramazon_time_mobile/13)",
    reply_markup=keyboard,
    disable_web_page_preview=True
)
async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
