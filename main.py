from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from Translator import translate
from random import randint

API_TOKEN = "Bot token"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
url1 = "https://t.me/matematika_patsha/248"
url2 = "https://t.me/c/1631587206/228"
a = randint(1, 9999) 

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply(f"Assalamu alaykum {message.from_user.full_name}\nTarjimon botiga xush kelibsiz! \n\n/help")

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply("Botdan foydalanish qoidasi:\n\t1. Botga inglizcha yoki o`zbekcha so`z yuboring\n\t2. Agar inglizcha bo`lsa o`zbekchaga, o`zbekcha bo`lsa inglizchaga tarjima qilib beradi.")

@dp.message_handler(Text(equals='reklama'))
async def reklama(message: types.Message):
    await message.reply(url1)
    await message.reply(url2)

@dp.message_handler(Text(equals='random'))
async def random(message: types.Message):
    await message.reply(f"Random sani\t{a}")

@dp.message_handler()
async def tarjimon(message: types.Message):
    await message.reply(translate(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
