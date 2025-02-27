from telethon import events
import requests

from .. import loader  # Импорт загрузчика модулей Hikka

TOKEN = "7352788141:AAFwTI8fhYV6WXLSPEE1dB5PYEnXlyb6auE"  # Замени на свой токен бота (обязательно в кавычках!)
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"  # Telegram Bot API URL

class SearchModule(loader.Module):
    """Модуль для поиска информации через Telegram Bot API"""
    strings = {"name": "SearchModule"}

    async def send_command(self, message, command, query_value):
        """Отправляет команду боту и возвращает его ответ"""
        params = {
            "chat_id": message.chat_id,  # Отправляем в тот же чат
            "text": f"/{command} {query_value}"
        }
        try:
            response = requests.post(API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("result", {}).get("text", "❌ Нет данных")
        except requests.exceptions.RequestException as e:
            return f"❌ Ошибка запроса: {e}"

    async def osphone_cmd(self, message):
        """Поиск по номеру телефона"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер телефона!")
            return
        result = await self.send_command(message, "osphone", args[1])
        await message.reply(f"📞 Результат поиска:\n{result}")

    async def ospass_cmd(self, message):
        """Поиск по ФИО"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите ФИО!")
            return
        result = await self.send_command(message, "ospass", args[1])
        await message.reply(f"🆔 Результат поиска:\n{result}")

    async def oscar_cmd(self, message):
        """Поиск по номеру автомобиля"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер автомобиля!")
            return
        result = await self.send_command(message, "oscar", args[1])
        await message.reply(f"🚗 Результат поиска:\n{result}")

    async def osadress_cmd(self, message):
        """Поиск по адресу"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите адрес!")
            return
        result = await self.send_command(message, "osadress", args[1])
        await message.reply(f"🏠 Результат поиска:\n{result}")

    async def osip_cmd(self, message):
        """Поиск по IP-адресу"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите IP-адрес!")
            return
        result = await self.send_command(message, "osip", args[1])
        await message.reply(f"🌍 Результат поиска:\n{result}")
