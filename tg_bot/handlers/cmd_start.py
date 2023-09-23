import logging

from aiogram import Router, F, types
from aiogram.enums import ChatType
from aiogram.utils.markdown import hcode

logger = logging.getLogger(__name__)
router = Router()


@router.message(F.chat.type == ChatType.PRIVATE)
async def start(message: types.Message):
    logger.info(f"Handler called. {start.__name__}. user_id={message.from_user.id}")

    text = [
        '<b>Bot Developer: <a href="">@san1rope</a></b>',
        '<b>Source Code: <a href="">GitHub</a></b>'
    ]
    await message.answer('\n'.join(text))
