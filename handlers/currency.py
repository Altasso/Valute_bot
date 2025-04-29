from aiogram import Router, types
from aiogram.filters import Command
from services.exchange import get_currency_rate
from keyboards.inline_refresh import refresh_keyboard
from keyboards.auto_currency_keyboard import generate_currency_keyboard
router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    keyboard = await generate_currency_keyboard()
    await message.answer("Привет! Я бот курсов валют.\nВведи код валюты со слешем вначале",
                         reply_markup=keyboard
                         )



@router.message()
async def catch_valute(message: types.Message):
    currency_code = message.text.strip().upper()[1:]
    if not currency_code.isalpha() or len(currency_code) != 3:
        await message.answer("Пожалуйста, введите 3-буквенный код валюты, например: usd, eur, jpy.")
        return
    try:
        rate = await get_currency_rate(currency_code)
        await message.answer(f"Курс {currency_code}: {rate:.2f} ₽",
                             reply_markup=refresh_keyboard(currency_code))
    except (KeyError, TypeError):
        await message.answer(f"Не могу найти валюту {currency_code} 😔")

@router.callback_query()
async def refresh_callback(call: types.CallbackQuery):
    if not call.data.startswith("refresh:"):
        return
    try:
        code = call.data.split(":")[1]

        rate = await get_currency_rate(code)
        await call.message.edit_text(
            f"🔄 Обновлённый курс {code}: {rate} ₽",
            reply_markup=refresh_keyboard(code)
        )
        await call.answer("Курс обновлён!")
    except Exception:
        await call.answer("Ошибка при обновлении", show_alert=True)