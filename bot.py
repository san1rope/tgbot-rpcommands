import asyncio
import logging

from aiogram import Dispatcher

from tg_bot.config import Config
from tg_bot.handlers import *

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')

    dp = Dispatcher()
    dp.include_router(r_start)

    await Config.BOT.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(Config.BOT, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
