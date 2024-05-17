import asyncio
import logging
import sys
import time

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from namoz import namoz_vaqtlari

TOKEN = "5841162833:AAFyptdrE1_PoRvbvSrzZ9VzL4DPp0Kj-NA"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    sent_msg = await message.reply("Yuklanmoqda...")
    nv_rs = namoz_vaqtlari("toshkent")
    lnv = f"""Toshkent vaqti bilan
Bomdod: {nv_rs['bomdod']}
Peshin: {nv_rs['peshin']}
Asr: {nv_rs['asr']}
Shom: {nv_rs['shom']}
Xufton: {nv_rs['xufton']}    
    """
    await bot.edit_message_text(chat_id=message.chat.id, message_id=sent_msg.message_id, text=lnv)


async def main() -> None:
    bot = Bot(TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
