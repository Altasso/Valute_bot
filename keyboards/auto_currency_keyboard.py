from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import aiohttp
import json

async def get_currency_codes() -> list[str]:
    url = "https://www.cbr-xml-daily.ru/daily_json.js"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text(encoding="utf-8")
            data = json.loads(text)
            return list(data["Valute"].keys())
async def generate_currency_keyboard() -> ReplyKeyboardMarkup:
    codes = await get_currency_codes()
    keyboard = []
    row = []

    for i, code in enumerate(codes, 1):
        row.append(KeyboardButton(text=f"/{code}"))
        if i % 3 == 0:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)