# - *- coding: utf- 8 - *-
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.data.loader import dp,bot

from tgbot.data.config import get_admins
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
        chat_id = -1001698535461
        url = 'https://t.me/chanel_test_11111'
        
        sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
        if sub.status != types.ChatMemberStatus.LEFT:
            return True
        else:
            markup = InlineKeyboardMarkup(row_width = 1,
                                        inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Телеграм группа:',
                                                                url=url)
                                        ]
                                            ])
            await dp.bot.send_message(chat_id =message.from_user.id,
                                        text = f'Подпишитесь на группу и повторите попытку',
                                        reply_markup=markup) 
            return False
