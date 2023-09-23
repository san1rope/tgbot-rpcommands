import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand

from tg_bot.config import Config
from tg_bot.handlers import *

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/me", description="Використання: /me (дія від першої особи)"),
        BotCommand(command="/do", description="Використання: /do (дія від третьої особи)"),
        BotCommand(command="/try", description="Використання: /try (дія від першої ссоби)")
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    dp = Dispatcher()
    dp.include_router(r_start)
    dp.include_router(r_rp_commands)

    loop = asyncio.get_event_loop()
    loop.create_task(set_commands(Config.BOT))

    await Config.BOT.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(Config.BOT, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
