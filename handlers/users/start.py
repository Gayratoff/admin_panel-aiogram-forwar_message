from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from keyboards.inline.menu_panel import kb
from loader import dp,db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    try:
        db.add_user(user_id=user_id)
    except:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=kb.menuus())


@dp.callback_query_handler(text="stat")
async def Admin_send(call: types.CallbackQuery):
    statiska = db.stat()
    for x in statiska:
        await call.message.answer(f"Bot foidalanuvchilari <b>{x} nafar</b>")
