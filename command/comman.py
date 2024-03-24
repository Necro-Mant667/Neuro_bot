from aiogram import types, F, Router
from aiogram.filters.command import Command
from buttons.keyboard import kb1, kb2
from raznoe.random_cat import cat

router = Router()

#Хэндлер на команду /start
@router.message(Command("start"))
async def cmd_start(message: types.Message):
   name = message.chat.first_name
   await message.answer(f"Hello, {name}",reply_markup=kb1)

#Хэндлер на команду /stop
@router.message(Command("stop"))
async def cmd_stop(message: types.Message):
     name = message.chat.first_name
     await message.answer(f"Пока, {name},")

#Хэндлер на команду /close
@router.message(Command("close"))
async def cmd_close(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Yes, of course, {name},")

#Хэндлер на команду /back
@router.message(Command("back"))
async def cmd_back(message: types.Message):
    name = message.chat.first_name
    await message.answer( f"Sure, {name},", reply_markup=kb1)


#Хэндлер на команду /сat
@router.message(Command("cat"))
@router.message(Command("кот"))
@router.message(F.text.lower() == "покажи кота")
async def cmd_cat(message: types.Message):
     name = message.chat.first_name
     img_cat = cat()
     await message.answer(f"Держи кота, {name}",)
     await message.answer_photo(photo=img_cat)
     #await bot.send_photo(message.from_user.id, photo=img_cat)



#@router.message(Command("герой"))
#@router.message(F.text.lower() == "герой")
#async def cmd_brave(message: types.Message):
     #name = message.chat.first_name
     #img_brave = brave()
     #await message.answer(f'Its for you, {name}')
     #await message.answer_photo(photo=img_brave)

 # await message.answer_photo(photo=img_cat)



#Хэндлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}',)
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'кот' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')


