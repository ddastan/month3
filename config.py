from aiogram import Bot, dispatcher, Dispatcher
from decouple import config

token=config('TOKEN')
bot=Bot(token=token)
dp = Dispatcher(bot=bot)