import wikipedia
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6483176491:AAGJimsmLJM4CYN2ayfh2mG1MEGM0YwHPbo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum!\nWikipedia botimizga xush kelibsiz!\nMatiningizni kiriting.")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        matn = message.text
        await message.answer(wikipedia.summary(matn))
    except:
        await message.answer("Bunday ma'lumot yo'q")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)