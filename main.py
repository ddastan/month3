from config import bot,dp
from aiogram import executor
from handlers import start,echo,files,quiz,game
from db import database

async def on_startup(_):
    await database.sql_create()



start.register_start(dp)
files.register_file(dp)
quiz.register_quiz(dp)
game.register_game(dp)
echo.register_echo(dp)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)