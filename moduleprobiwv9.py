from telethon import events
import requests
from .. import loader  # Импорт загрузчика модулей Hikka

TOKEN = "7352788141:AAFwTI8fhYV6WXLSPEE1dB5PYEnXlyb6auE"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"  # Telegram Bot API URL

class SearchModule(loader.Module):
    """Модуль для поиска информации через Telegram Bot API"""
    strings = {"name": "SearchModule"}

    async def send_command(self, query_value, command):
    """Отправляет команду боту и возвращает его ответ"""
    # Здесь нужно указать реальный chat_id получателя
    # Это может быть ваш user_id или ID группы
    chat_id = "498179796"  # Замените на реальный ID
    
    params = {
        "chat_id": chat_id,
        "text": f"/{command} {query_value}"
    }
    try:
        response = requests.post(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("result", {}).get("text", "❌ Нет данных")
    except requests.exceptions.RequestException as e:
        return f"❌ Ошибка запроса: {e}"

    async def process_command(self, message, command):
        """Обрабатывает команду, отправляя сообщение от имени пользователя"""
        args = message.raw_text.split(" ", 1)
        if len(args) < 2:
            await message.reply("⚠ Укажите параметр запроса!")
            return
        query_value = args[1]
        status_message = await message.reply("🔍 Выполняю поиск...")
        result = await self.send_command(query_value, command)
        
        # Обработка результата для безопасного отображения
        safe_result = str(result).replace('<', '&lt;').replace('>', '&gt;')
        
        try:
            # Используем parse_mode=None для предотвращения ошибок форматирования
            await status_message.edit(f"🔍 Результат поиска:\n{safe_result}", parse_mode=None)
        except Exception as e:
            # Если редактирование не удалось, отправляем новое сообщение
            await status_message.delete()
            await message.reply(f"🔍 Результат поиска:\n{safe_result}", parse_mode=None)

    async def osphone_cmd(self, message):
        """Поиск по номеру телефона"""
        await self.process_command(message, "osphone")

    async def ospass_cmd(self, message):
        """Поиск по ФИО"""
        await self.process_command(message, "ospass")

    async def oscar_cmd(self, message):
        """Поиск по номеру автомобиля"""
        await self.process_command(message, "oscar")

    async def osadress_cmd(self, message):
        """Поиск по адресу"""
        await self.process_command(message, "osadress")

    async def osip_cmd(self, message):
        """Поиск по IP-адресу"""
        await self.process_command(message, "osip")