import aiohttp
import json
#from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_currency_rate(currency_code: str) -> float:
    url = "https://www.cbr-xml-daily.ru/daily_json.js"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text(encoding='utf-8')
            try:
                data = json.loads(text)
            except Exception as e:
                text = await response.text()
                print(f"Ошибка при парсинге JSON:\n{text}")
                raise ValueError("Не удалось прочитать JSON от сервера") from e

            valute_data = data.get("Valute", {})
            currency = valute_data.get(currency_code.upper())

            if not currency:
                raise KeyError(f"Валюта {currency_code.upper()} не найдена!")

            return currency["Value"]
