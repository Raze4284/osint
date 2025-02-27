from telethon import events
import requests

from .. import loader  # Импорт загрузчика модулей Hikka

TOKEN = "7352788141:AAFwTI8fhYV6WXLSPEE1dB5PYEnXlyb6auE"  
API_URL = f"https://api.telegram.org/bot{TOKEN}"

class SearchModule(loader.Module):
    strings = {"name": "SearchModule"}

    async def search_request(self, method, query_value):
        url = f"{API_URL}/{method}"
        params = {"query": query_value}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get("result", "Нет данных")
        except requests.exceptions.RequestException as e:
            return f"Ошибка запроса: {e}"

    async def osphone_cmd(self, message):
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер телефона!")
            return
        result = await self.search_request("phone", args[1])
        await message.reply(f"📞 Результат поиска:\n{result}")

    async def ospass_cmd(self, message):
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите ФИО!")
            return
        result = await self.search_request("name", args[1])
        await message.reply(f"🆔 Результат поиска:\n{result}")

    async def oscar_cmd(self, message):
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите номер автомобиля!")
            return
        result = await self.search_request("car", args[1])
        await message.reply(f"🚗 Результат поиска:\n{result}")

    async def osadress_cmd(self, message):
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите адрес!")
            return
        result = await self.search_request("address", args[1])
        await message.reply(f"🏠 Результат поиска:\n{result}")

    async def osip_cmd(self, message):
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите IP-адрес!")
            return
        result = await self.search_request("ip", args[1])
        await message.reply(f"🌍 Результат поиска:\n{result}")
