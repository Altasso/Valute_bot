import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import currency

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(currency.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())