import logging

from aiogram import Router, F, types
from aiogram.enums import ChatType
from aiogram.filters import CommandStart

logger = logging.getLogger(__name__)
router = Router()


@router.message(F.chat.type == ChatType.PRIVATE, CommandStart())
async def start(message: types.Message):
    logger.info(f"Handler called. {start.__name__}. user_id={message.from_user.id}")

    text = [
        '<b> 🗯 INFO 🗯 </b>\n',
        '<b>Localization of the bot: Ukrainian</b>',
        '<b>Supported chat types: GROUP, SUPERGROUP</b>\n',
        '<b>Bot Developer: <a href="https://t.me/san1rope">@san1rope</a></b>',
        '<b>Source Code: <a href="https://github.com/san1rope/tgbot-rpcommands">tgbot-rpcommands</a></b>'
    ]
    await message.answer(text='\n'.join(text), disable_web_page_preview=True)
