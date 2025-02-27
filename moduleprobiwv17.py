from telethon import events
import asyncio
from .. import loader  # Импорт загрузчика модулей Hikka

class EyeOfGodModule(loader.Module):
    """Модуль для поиска информации через бота Глаз бога"""
    strings = {"name": "EyeOfGodSearch"}
    
    # Имя бота Глаз бога
    BOT_USERNAME = "@FS00CIETY_bot"  # Замените на актуальное имя бота
    
    async def process_command(self, message, command):
        """Обрабатывает команду и отображает информацию для отправки боту"""
        args = message.raw_text.split(" ", 1)
        
        if len(args) < 2:
            await message.reply(f"⚠️ Укажите параметр для поиска!\nПример: .{command} значение")
            return
        
        query_value = args[1]
        
        # Создаем инструкцию для пользователя
        instruction = f"📱 **Поиск через Глаз бога**\n\n" \
                     f"1️⃣ Перейдите к боту {self.BOT_USERNAME}\n" \
                     f"2️⃣ Отправьте боту команду: /{command} {query_value}\n" \
                     f"3️⃣ Дождитесь ответа от бота\n\n" \
                     f"ℹ️ Бот может запросить оплату за полную информацию."
        
        await message.reply(instruction, parse_mode="Markdown")
    
    async def osphone_cmd(self, message):
        """Поиск по номеру телефона"""
        await self.process_command(message, "phone")
    
    async def ospass_cmd(self, message):
        """Поиск по ФИО"""
        await self.process_command(message, "name")
    
    async def oscar_cmd(self, message):
        """Поиск по номеру автомобиля"""
        await self.process_command(message, "car")
    
    async def osadress_cmd(self, message):
        """Поиск по адресу"""
        await self.process_command(message, "address")
    
    async def osip_cmd(self, message):
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