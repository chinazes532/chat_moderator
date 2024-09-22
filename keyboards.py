from aiogram.types import (InlineKeyboardMarkup, InlineKeyboardButton)


admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="👨‍💻 Администратор", url='https://t.me/username')
        ],
    ]
)