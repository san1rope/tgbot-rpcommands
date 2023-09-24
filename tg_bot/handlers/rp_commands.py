import logging
from random import randint

from aiogram import Router, types, F, enums
from aiogram.filters import Command
from aiogram.utils.markdown import hcode

from tg_bot.config import Config

logger = logging.getLogger(__name__)
router = Router()


@router.message(F.chat.type.in_({enums.ChatType.GROUP, enums.ChatType.SUPERGROUP}), Command('me'))
async def cmd_me(message: types.Message):
    logger.info(f"Handler called. {cmd_me.__name__}. user_id={message.from_user.id}")

    if Config.BOT.id not in [admin.user.id for admin in await message.chat.get_administrators()]:
        return

    args = message.text.strip().split()
    if not args:
        return

    args[1] = args[1].lower()

    await message.delete()
    await message.answer(
        text=f"<b>{hcode(message.from_user.full_name)} </b>{' '.join(args[1:])}",
        disable_web_page_preview=True
    )


@router.message(F.chat.type.in_({enums.ChatType.GROUP, enums.ChatType.SUPERGROUP}), Command('do'))
async def cmd_do(message: types.Message):
    logger.info(f"Handler called. {cmd_do.__name__}. user_id={message.from_user.id}")

    if Config.BOT.id not in [admin.user.id for admin in await message.chat.get_administrators()]:
        return

    args = message.text.strip().split()
    if not args:
        return

    args = message.text.strip().split()
    args[1] = args[1][0].upper() + args[1][1:]
    if not args[-1].endswith('.'):
        args[-1] = args[-1] + '.'

    await message.delete()
    await message.answer(
        text=f"{' '.join(args[1:])} | {hcode(message.from_user.full_name)}",
        disable_web_page_preview=True
    )


@router.message(F.chat.type.in_({enums.ChatType.GROUP, enums.ChatType.SUPERGROUP}), Command('todo'))
async def cmd_todo(message: types.Message):
    logger.info(f"Handler called. {cmd_todo.__name__}. user_id={message.from_user.id}")

    if Config.BOT.id not in [admin.user.id for admin in await message.chat.get_administrators()]:
        return

    args = message.text.strip().split()
    if not args:
        return

    command_args = ' '.join(args[1:])
    if '*' not in command_args:
        return

    temp = command_args.split('*')

    await message.delete()
    await message.answer(
        text=f"{hcode(message.from_user.full_name)}: <b>{temp[0]}</b> - {temp[1]}",
        disable_web_page_preview=True
    )


@router.message(F.chat.type.in_({enums.ChatType.GROUP, enums.ChatType.SUPERGROUP}), Command('try'))
async def cmd_try(message: types.Message):
    logger.info(f"Handler called. {cmd_try.__name__}. user_id={message.from_user.id}")

    if Config.BOT.id not in [admin.user.id for admin in await message.chat.get_administrators()]:
        return

    args = message.text.strip().split()
    if not args:
        return

    args[1] = args[1].lower()

    await message.delete()
    await message.answer(
        text=f"{hcode(message.from_user.full_name)} {' '.join(args[1:])} | <b>{'Вдало' if randint(0, 1) else 'Невдало'}</b>",
        disable_web_page_preview=True
    )


# @router.message(F.chat.type.in_({enums.ChatType.GROUP, enums.ChatType.SUPERGROUP}))
# async def global_chat(message: types.Message):
#     logger.info(f"Handler called. {global_chat.__name__}. user_id={message.from_user.id}")
#
#     if Config.BOT.id not in [admin.user.id for admin in await message.chat.get_administrators()]:
#         return
#
#     args = message.text.strip().split()
#     if not args:
#         return
#
#     await message.delete()
#     await message.answer(
#         text=f"{hcode(message.from_user.full_name)} говорить: {' '.join(args)}",
#         disable_web_page_preview=True
#     )
