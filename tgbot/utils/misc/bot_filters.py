# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.data.loader import dp,bot

from tgbot.data.config import get_admins, GROUP_URL, GROUP_ID
from tgbot.services.api_sqlite import get_settingsx


# Проверка на админа
class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if message.from_user.id in get_admins():
            return True
        else:
            return False


# Проверка на возможность покупки товара
class IsBuy(BoundFilter):
    async def check(self, message: types.Message):
        get_settings = get_settingsx()

        if get_settings['status_buy'] == "True" or message.from_user.id in get_admins():
            return False
        else:
            return True


# Проверка на возможность пополнения
class IsRefill(BoundFilter):
    async def check(self, message: types.Message):
        get_settings = get_settingsx()

        if get_settings['status_refill'] == "True" or message.from_user.id in get_admins():
            return False
        else:
            return True


# Проверка на технические работы
class IsWork(BoundFilter):
    async def check(self, message: types.Message):
        get_settings = get_settingsx()

        if get_settings['status_work'] == "False" or message.from_user.id in get_admins():
            return False
        else:
            return True

class IsSubscriber(BoundFilter):
    async def check(self, message:types.Message):
        chat_id = GROUP_ID
        url = GROUP_URL
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if sub.status != types.ChatMemberStatus.LEFT:
            return True
        else:
            markup = InlineKeyboardMarkup(row_width = 1,
                                        inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Dread Pirate 🏴‍☠️',
                                                                url=url)
                                        ]
                                            ])
            await message.answer(text = f'Вступите в чат и повторите попытку',reply_markup=markup)
            return False

class IsPrivate(BoundFilter):
    async def check(self, message:types.Message):
        return message.chat.type == types.ChatType.PRIVATE
