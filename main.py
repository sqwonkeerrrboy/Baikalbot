import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5022788582:AAF5dIEORKPibBLqFGkXlqmaCIJevC5q4W8')
dp = Dispatcher(bot)

@dp.message_handler(commands = ["start"])
async def precces_start_command(messege: types.message):
    await messege.reply("Привет! \nНапиши мне что-нибудь!")

@dp.message_handler(commands = ["help"])
async def precces_help_command(messege: types.message):
    await messege.reply("Напиши мне что-нибудь, а я тебе отправлю это в ответ!")

@dp.message_handler()
async def echo_messege(msg: types.message):
    await bot.send_message(msg.from_user.id, "Я не понял вашей команды! \n Для того, что бы узнать доступные вам комнды используйте /help!")


if __name__ == '__main__':
    print("Бот запущен!")
    executor.start_polling(dp)



