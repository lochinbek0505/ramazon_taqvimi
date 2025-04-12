from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import asyncio

TOKEN = "7802726591:AAHxS4-VDPwG4tu-56MqFwGgVq1Up4AN_-Q"
WEB_APP_URL = "https://shopapp3-9dfa3.web.app/"

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
,    reply_markup=keyboard,
    disable_web_page_preview=True
)
async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
