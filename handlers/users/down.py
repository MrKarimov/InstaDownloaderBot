from aiogram import types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from loader import dp
from insta import kali


from aiogram.dispatcher.filters import Text

teng="https://www.instagram.com"
@dp.message_handler()
if teng==Text(startswith='https://www.instagram.com'):


 async def test(message:types.Message):
    answ = kali(message.text)

    await message.answer_audio(answ['media'])
else:
 async def test2(messmessage.textage:types.Message):
    answ = kali()

    await message.answer(answ['media'])
# @dp.callback_query_handler(Text(startswith='🎵'))
# async def test2(call:CallbackQuery):
#     await call.answer(cache_time=60)
#     data = call.data[1:]
#     await call.message.answer_audio(data)