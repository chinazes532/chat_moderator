from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from database import insert_user, get_user

user = Router()

@user.message(F.new_chat_member, ChatTypeFilter(['group', 'supergroup']))
async def start_command_chat(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer(f"<b>{message.from_user.full_name}, добро пожаловать!</b>\n\n"
                             f"Для просмотра списка всех команд введите /help",
                             parse_mode='HTML')
    else:
        await insert_user(message.from_user.id, 0)
        await message.answer(f"<b>{message.from_user.full_name}, добро пожаловать!</b>\n\n"
                             f"Для просмотра списка всех команд введите /help",
                             parse_mode='HTML')

@user.message(Command('help'), ChatTypeFilter(['group', 'supergroup']))
async def help_command(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer("<b>Список команд:</b>\n\n"
                             "<code>/profile</code> - <b>Ваша статистика в чате</b>\n"
                             "<code>/help</code> - <b>Список команд</b>",
                             parse_mode='HTML')
    else:
        await insert_user(message.from_user.id, 0)
        await message.answer("<b>Список команд:</b>\n\n"
                             "<code>/profile</code> - <b>Ваша статистика в чате</b>\n"
                             "<code>/help</code> - <b>Список команд</b>",
                             parse_mode='HTML')

@user.message(Command('profile'), ChatTypeFilter(['group', 'supergroup']))
async def profile_command(message: Message):
    user = await get_user(message.from_user.id)
    if user:
        await message.answer(f"<b>Ваша статистика в чате:</b>\n\n"
                             f"Всего предупреждений: <code>{user[1]}</code>",
                             parse_mode='HTML')
    else:
        await insert_user(message.from_user.id, 0)
        await message.answer(f"<b>Ваша статистика в чате:</b>\n\n"
                             f"Всего предупреждений: <code>0</code>",
                             parse_mode='HTML')
