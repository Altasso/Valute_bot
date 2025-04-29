from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from uuid import uuid4

def refresh_keyboard(currency_code: str) -> InlineKeyboardMarkup:
    unique = uuid4().hex[:6]
    callback_data = f"refresh:{currency_code.upper()}:{unique}"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔄 Обновить курс",
                    callback_data=callback_data
                )
            ]
        ]
    )