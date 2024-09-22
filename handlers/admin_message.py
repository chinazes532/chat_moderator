from contextlib import suppress

from aiogram import Router, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, ChatPermissions
from aiogram.filters import CommandStart, Command, CommandObject

from filters.is_admin import AdminProtect
from filters.chat_type import ChatTypeFilter

from filters.parse_time import parse_time
from filters.admin_chat import admin_chat

import keyboards as kb

from database import (add_warn, get_user,
                      delete_all_warn)

admin = Router()


@admin.message(CommandStart(), ChatTypeFilter(['private']), AdminProtect())
async def start_command(message: Message):
    await message.answer("Вы авторизовались как администратор!\n"
                         "Выберите действие:")


@admin.message(Command('warn'), ChatTypeFilter(['group', 'supergroup']))
async def warn_command(message: Message, bot: Bot):
    if not message.reply_to_message or not await admin_chat(message, bot):
        await message.answer("Эта команда должна быть ответом на сообщение")
        return

    user_id = message.reply_to_message.from_user.id
    user = await get_user(user_id)

    if user is None:
        await message.answer("Пользователь не найден.")
        return

    if user[1] >= 2:
        await add_warn(user_id)
        await bot.restrict_chat_member(
            user_id=user_id,
            chat_id=message.chat.id,
            until_date=None,
            permissions=ChatPermissions(can_send_messages=False)
        )
        await message.reply("Вы были заблокированы в чате, вы можете попросить разбан у админа.",
                             parse_mode='HTML',
                             reply_markup=kb.admin)
    else:
        await add_warn(user_id)
        username = message.reply_to_message.from_user.username or "пользователь"
        await message.reply(f"@{username} <code>вы были предупреждены.\n"
                            f"Количество предупреждений: {user[1] + 1}/3</code>",
                            parse_mode='HTML')


@admin.message(Command('unwarn'), ChatTypeFilter(['group', 'supergroup']))
async def unwarn_command(message: Message, bot: Bot):
    if message.reply_to_message or not await admin_chat(message, bot):
        await delete_all_warn(message.reply_to_message.from_user.id)
        await message.reply(f"<code>с вас были сняты все предупреждения</code>",
                            parse_mode='HTML')

        await bot.restrict_chat_member(chat_id=message.chat.id,
                                       user_id=message.reply_to_message.from_user.id,
                                       permissions=ChatPermissions(can_send_messages=True,
                                                                   can_send_other_messages=True))
        await message.answer(f" Все ограничения с пользователя  были сняты!")
    else:
        await message.answer("Эта команда должна быть ответом на сообщение")


@admin.message(Command("mute"), ChatTypeFilter(['group', 'supergroup']))
async def func_mute(message: Message, command: CommandObject, bot: Bot):
    reply_message = message.reply_to_message

    if not reply_message or not await admin_chat(message, bot):
        await message.reply("<b>❌  Произошла ошибка!</b>",
                            parse_mode='HTML')
        return

    date = parse_time(command.args)
    mention = reply_message.from_user.mention_html(reply_message.from_user.first_name)

    with suppress(TelegramBadRequest):
        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=reply_message.from_user.id, until_date=date,
                                       permissions=ChatPermissions(can_send_messages=False))
        await message.answer(f"🔇 Пользователь <b>{mention}</b> был заглушен!",
                             parse_mode='HTML')


