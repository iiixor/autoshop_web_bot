# - *- coding: utf- 8 - *-
import configparser

read_config = configparser.ConfigParser()
read_config.read("settings.ini")

BOT_TOKEN = read_config['settings']['token'].strip().replace(" ", "")  # Токен бота
GROUP_URL = read_config['settings']['group_url'].strip().replace(" ", "") # url группы
GROUP_ID = read_config['settings']['group_id'].strip().replace(" ", "") # id группы
PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам
BOT_VERSION = "3.3"  # Версия бота


# Получение администраторов бота
def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read("settings.ini")

    admins = read_admins['settings']['admin_id'].strip().replace(" ", "")

    if "," in admins:
        admins = admins.split(",")
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "\r" in admins: admins.remove("\r")
    while "\n" in admins: admins.remove("\n")

    admins = list(map(int, admins))

    return admins


# УДАЛИШЬ ИЛИ ИЗМЕНИШЬ ССЫЛКИ НА ДОНАТ, КАНАЛ И ТЕМУ БОТА - КАСТРИРУЮ БЛЯТЬ <3
BOT_DESCRIPTION = f"""
<b>⚜ Bot Version: <code>{BOT_VERSION}</code>
""".strip()
