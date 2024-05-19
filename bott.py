import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,InputFile,FSInputFile
import io
from removebg import remove_bg
from inlinebuttonss import colors_button

TOKEN = "6858596228:AAGiUE4iKAEi5ED63fOSGWeSshG_rLfHbKA"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\nBu bot rasm orqa fonini o'chirib beradi. \nBotdan foydalanish uchun rasm yuboring❗️❗️❗️"
    await message.reply(text=text)



@dp.message(F.photo)
async def name(message:Message):
    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    await message.answer_photo(photo=file_id,reply_markup=colors_button)
        # await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))

@dp.message()
async def text_message(message:Message):
    message.answer("Iltimos, rasm yuboring!!!")

@dp.callback_query(F.data=="black")
async def black_handler(callback:CallbackQuery):
    await callback.answer("Bu qora")
    # await callback.message.answer("Qorani bosdingiz")
    file_id = callback.message.photo[-1].file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    rasm = remove_bg(photos_url,"black")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()


@dp.startup()
async def bot_start():
    await bot.send_message(5012784380, "Botimiz ishga tushdi !")

@dp.shutdown()
async def bot_start():
    await bot.send_message(5012784380, "Bot to'xtadi !")    


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


