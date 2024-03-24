from aiogram import types


button1 = types.KeyboardButton(text="/start")
button2 = types.KeyboardButton(text="/stop")
button3 = types.KeyboardButton(text="/hero")
button4 = types.KeyboardButton(text="покажи кота")
button5 = types.KeyboardButton(text="/close")
button6 = types.KeyboardButton(text="/back")
button7 = types.KeyboardButton(text="/ок")

keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]

keyboard2 = [
    [button4, button6],
]


kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)