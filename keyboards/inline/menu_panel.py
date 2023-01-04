from aiogram import types

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

class Keyboards:
    def main(self):
        menu = types.InlineKeyboardMarkup(row_width=1)
        send = types.InlineKeyboardButton("♻️ Xabar Yuborish", callback_data="send")
        stat = types.InlineKeyboardButton("📊 Statiska", callback_data="stat")
        return menu.add(send,stat)

    def menuus(self):
        menu = types.InlineKeyboardMarkup(row_width=1)
        stat = types.InlineKeyboardButton("📊 Statiska", callback_data="stat")
        return menu.add(stat)

    def admin(self):
        menu = types.InlineKeyboardMarkup(row_width=1)
        photo = types.InlineKeyboardButton("PHOTO XABAR YUBORISH",callback_data="photo")
        video = types.InlineKeyboardButton("VIDEO XABAR YUBORISH", callback_data="video")
        voice = types.InlineKeyboardButton("VOICE XABAR YUBORISH", callback_data="voice")
        text = types.InlineKeyboardButton("TEXT XABAR YUBORISH", callback_data="text")
        return menu.add(photo,video,voice,text)

kb = Keyboards()