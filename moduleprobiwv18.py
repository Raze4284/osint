from telethon import events
import asyncio
from .. import loader  # Импорт загрузчика модулей Hikka

class EyeOfGodModule(loader.Module):
    """Модуль для автоматического поиска информации через бота Глаз бога"""
    strings = {"name": "EyeOfGodSearch"}
    
    # Имя бота Глаз бога
    BOT_USERNAME = "FS00CIETY_bot"  # Замените на актуальное имя бота без @
    
    async def client_ready(self, client, db):
        """Вызывается при готовности клиента"""
        self.client = client
        self.db = db
        # Получаем entity бота для дальнейшего использования
        try:
            self.bot_entity = await client.get_entity(f"@{self.BOT_USERNAME}")
        except Exception as e:
            self.bot_entity = None
            print(f"Не удалось получить entity бота: {e}")
    
    async def send_cmd_to_bot(self, command, query_value):
        """Отправляет команду боту и возвращает его ответ"""
        if not self.bot_entity:
            try:
                self.bot_entity = await self.client.get_entity(f"@{self.BOT_USERNAME}")
            except Exception as e:
                return f"❌ Ошибка: Не удалось найти бота @{self.BOT_USERNAME}"
        
        try:
            # Отправляем команду боту
            await self.client.send_message(self.bot_entity, f"/{command} {query_value}")
            
            # Ждем ответ от бота
            start_time = asyncio.get_event_loop().time()
            timeout = 60  # 60 секунд таймаут
            
            while (asyncio.get_event_loop().time() - start_time) < timeout:
                # Проверяем новые сообщения
                messages = await self.client.get_messages(
                    self.bot_entity,
                    limit=3,  # Проверяем последние 3 сообщения
                )
                
                for msg in messages:
                    # Если сообщение новое (после отправки команды)
                    if msg.date.timestamp() > start_time - 5:  # 5 секунд запаса
                        # Проверяем, что это не эхо нашей команды
                        if not msg.out and f"/{command}" not in msg.text:
                            return msg.text
                
                # Ждем 2 секунды перед следующей проверкой
                await asyncio.sleep(2)
            
            return "⏱️ Превышен таймаут ожидания ответа от бота"
        
        except Exception as e:
            return f"❌ Ошибка при общении с ботом: {str(e)}"
    
    async def process_command(self, message, command):
        """Обрабатывает команду, отправляет запрос боту и возвращает результат"""
        args = message.raw_text.split(" ", 1)
        
        if len(args) < 2:
            await message.reply(f"⚠️ Укажите параметр для поиска!\nПример: .{command} значение")
            return
        
        query_value = args[1]
        
        # Отправляем статусное сообщение
        status_message = await message.reply(f"🔍 Отправляю запрос боту Глаз бога (/{command} {query_value})...\nПожалуйста, подождите.")
        
        # Отправляем команду боту и получаем ответ
        response = await self.send_cmd_to_bot(command, query_value)
        
        # Обрабатываем результат
        if response:
            # Обработка результата для безопасного отображения
            safe_result = str(response).replace('<', '&lt;').replace('>', '&gt;')
            
            try:
                await status_message.edit(f"🔍 Результат от бота Глаз бога:\n\n{safe_result}", parse_mode=None)
            except Exception as e:
                # Если сообщение слишком длинное или есть другие проблемы с редактированием
                await status_message.delete()
                await message.reply(f"🔍 Результат от бота Глаз бога:\n\n{safe_result}", parse_mode=None)
        else:
            await status_message.edit("❌ Не удалось получить ответ от бота.")
    
    async def phone_cmd(self, message):
        """Поиск по номеру телефона"""
        await self.process_command(message, "phone")
    
    async def name_cmd(self, message):
        """Поиск по ФИО"""
        await self.process_command(message, "name")
    
    async def car_cmd(self, message):
        """Поиск по номеру автомобиля"""
        await self.process_command(message, "car")
    
    async def address_cmd(self, message):
        """Поиск по адресу"""
        await self.process_command(message, "address")
    
    async def ip_cmd(self, message):
        """Поиск по IP-адресу"""
        await self.process_command(message, "ip")
    
    async def vk_cmd(self, message):
        """Поиск по VK"""
        await self.process_command(message, "vk")
    
    async def inst_cmd(self, message):
        """Поиск по Instagram"""
        await self.process_command(message, "inst")
    
    async def tg_cmd(self, message):
        """Поиск по Telegram"""
        await self.process_command(message, "tg")
    
    async def email_cmd(self, message):
        """Поиск по Email"""
        await self.process_command(message, "email")