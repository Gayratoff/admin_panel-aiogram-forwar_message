from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType

from data.config import ADMINS
from keyboards.inline.menu_panel import kb
from loader import dp,db,bot
from states.state import *

@dp.message_handler(commands=['admin'], chat_id = ADMINS)
async def bot_echo(message: types.Message):
    await message.answer("SIZ ADMIN PANELDASIZ",reply_markup=kb.main())


@dp.callback_query_handler(text="send", chat_id = ADMINS)
async def Admin_send(call: types.CallbackQuery):
    await call.message.answer("Xabar turini Tanlang 👇🏻",reply_markup=kb.admin())


# TEXT xabar uchun
@dp.callback_query_handler(text="text", chat_id = ADMINS)
async def Admin_send(call: types.CallbackQuery):
    await call.message.answer("XABAR YUBORISH UCHUN TEXT KIRITNING")
    await send_text.text.set()

@dp.message_handler(state=send_text.text)
async def bot_echo(message: types.Message, state: FSMContext):
    all_user_id = db.select_all_users()
    for x in all_user_id:
        user_id = x[1]
        await bot.forward_message(chat_id=user_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
        await state.finish()


# PHOTO xabar uchun
@dp.callback_query_handler(text="photo", chat_id = ADMINS)
async def Admin_send(call: types.CallbackQuery):
    await call.message.answer("PHOTO KIRITNING")
    await send_phot.photo.set()

@dp.message_handler(state=send_phot.photo, content_types=ContentType.PHOTO)
async def bot_echo(message: types.Message, state: FSMContext):
    all_user_id = db.select_all_users()
    for x in all_user_id:
        user_id = x[1]
        await bot.forward_message(chat_id=user_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
        await state.finish()


# VIDEO xabar uchun
@dp.callback_query_handler(text="video", chat_id = ADMINS)
async def Admin_send(call: types.CallbackQuery):
    await call.message.answer("VIDEO KIRITNING")
    await send_vid.video.set()

@dp.message_handler(state=send_vid.video, content_types=ContentType.VIDEO)
async def bot_echo(message: types.Message, state: FSMContext):
    all_user_id = db.select_all_users()
    for x in all_user_id:
        user_id = x[1]
        await bot.forward_message(chat_id=user_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
        await state.finish()


# VOICE xabar uchun
@dp.callback_query_handler(text="voice", chat_id = ADMINS)
async def Admin_send(call: types.CallbackQuery):
    await call.message.answer("VOICE KIRITNING")
    await send_voi.voice.set()

@dp.message_handler(state=send_voi.voice, content_types=ContentType.VOICE)
async def bot_echo(message: types.Message, state: FSMContext):
    all_user_id = db.select_all_users()
    for x in all_user_id:
        user_id = x[1]
        await bot.forward_message(chat_id=user_id,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id)
        await state.finish()

