import asyncio
from command  import config
from aiogram import Bot, Dispatcher
import logging
from command import comman, game_choice

async def main():
    #Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    #Создаем объект бота
    bot = Bot(token=config.token)

    #Диспетчер
    cj = Dispatcher()

    cj.include_router(game_choice.router)
    cj.include_router(comman.router)

    await cj.start_polling(bot)


if __name__ =='__main__':
  asyncio.run (main())
