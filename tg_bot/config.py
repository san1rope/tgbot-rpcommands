import os

from aiogram import Bot, enums
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT = Bot(os.getenv("BOT_TOKEN"), parse_mode=enums.ParseMode.HTML)
