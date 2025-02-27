from telethon import events
import requests

from .. import loader  # Импорт загрузчика модулей Hikka

TOKEN = "7352788141:AAFwTI8fhYV6WXLSPEE1dB5PYEnXlyb6auE"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

class SearchModule(loader.Module):
    strings = {"name": "SearchModule"}

    async def send_command(self, command, query_value):
        """Отправляет команду боту и возвращает его ответ"""
        params = {
            "chat_id": "@FS00CIETY_bot",  # Замени на username или ID бота
            "text": f"/{command} {query_value}",
            "parse_mode": "HTML"
        }
        try:
            response = requests.post(API_URL, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("result", {}).get("text", "Нет данных")
        except requests.exceptions.RequestException as e:
            return f"Ошибка запроса: {e}"

    async def osphone_cmd(self, message):
        """Поиск по номеру телефона"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер телефона!")
            return
        result = await self.send_command("osphone", args[1])
        await message.reply(f"📞 Результат поиска:\n{result}")

    async def ospass_cmd(self, message):
        """Поиск по ФИО"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите ФИО!")
            return
        result = await self.send_command("ospass", args[1])
        await message.reply(f"🆔 Результат поиска:\n{result}")

    async def oscar_cmd(self, message):
        """Поиск по номеру автомобиля"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер автомобиля!")
            return
        result = await self.send_command("oscar", args[1])
        await message.reply(f"🚗 Результат поиска:\n{result}")

    async def osadress_cmd(self, message):
        """Поиск по адресу"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите адрес!")
            return
        result = await self.send_command("osadress", args[1])
        await message.reply(f"🏠 Результат поиска:\n{result}")

    async def osip_cmd(self, message):
        """Поиск по IP-адресу"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите IP-адрес!")
            return
        result = await self.send_command("osip", args[1])
        await message.reply(f"🌍 Результат поиска:\n{result}")
