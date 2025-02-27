from telethon import events
import asyncio
from .. import loader  # Импорт загрузчика модулей Hikka

class SearchModule(loader.Module):
    """Модуль для поиска информации через Telegram бота"""
    strings = {"name": "ShinigamiEyes"}

    async def wait_for_bot_response(self, client, chat_id, timeout=60):
        """Ожидает ответ от бота в течение указанного времени"""
        start_time = asyncio.get_event_loop().time()
        
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            # Проверяем новые сообщения
            async for message in client.iter_messages(chat_id, limit=5):
                # Возвращаем самое новое сообщение как ответ
                if message.date.timestamp() > start_time:
                    return message.text
            
            # Ждем 1 секунду перед следующей проверкой
            await asyncio.sleep(1)
        
        return "⏱️ Превышен таймаут ожидания ответа от бота"

    async def process_command(self, message, bot_username):
        """Обрабатывает команду и запрашивает пользователя отправить данные боту"""
        args = message.raw_text.split(" ", 1)
        
        # Если аргументы есть, используем их как исходное сообщение
        if len(args) > 1:
            query_value = args[1]
            status_message = await message.reply(f"📱 Пожалуйста, отправьте следующее значение боту @{FS00CIETY_bot}:\n\n{query_value}\n\nОжидаю ответ от бота...")
            
            # Получаем ID чата пользователя
            user_id = message.from_id
            
            # Ждем ответ от бота
            response = await self.wait_for_bot_response(message.client, bot_username)
            
            try:
                # Обработка результата для безопасного отображения
                safe_result = str(response).replace('<', '&lt;').replace('>', '&gt;') if response else "❌ Ответ не получен"
                await status_message.edit(f"🔍 Результат поиска:\n{safe_result}", parse_mode=None)
            except Exception as e:
                await status_message.delete()
                await message.reply(f"🔍 Результат поиска:\n{safe_result}", parse_mode=None)
        else:
            await message.reply(f"ℹ️ Пожалуйста, укажите значение для поиска после команды.\nПример: .osphone +79XXXXXXXXX")

    async def osphone_cmd(self, message):
        """Поиск по номеру телефона"""
        await self.process_command(message, "@FS00CIETY_bot")

    async def ospass_cmd(self, message):
        """Поиск по ФИО"""
        await self.process_command(message, "@FS00CIETY_bot")

    async def oscar_cmd(self, message):
        """Поиск по номеру автомобиля"""
        await self.process_command(message, "@FS00CIETY_bot)

    async def osadress_cmd(self, message):
        """Поиск по адресу"""
        await self.process_command(message, "@FS00CIETY_bot")

    async def osip_cmd(self, message):
        """Поиск по IP-адресу"""
        await self.process_command(message, "@FS00CIETY_bot")