from aiogram import executor, types, Dispatcher, Bot


BOT_TOKEN = "6423016511:AAF8rRzXJOZWkbj6eYVX60c-g_RKij2s9ms"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("hello welcome to my bot")


@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer("No halp")


@dp.message_handler(commands="bio")
async def start(message: types.Message):
    await message.answer("Asadbek Pazlitdinov 2009.8.08")


@dp.message_handler(commands="photo")
async def start(message: types.Message):
    await message.answer_photo(photo="https://n1s1.hsmedia.ru/ff/12/77/ff127718f50b54cd2a27fecf4842b774/400x600_1_0d57eeaada921afcb761b2711ce69043@3333x5000_0xrvs87oEi_5192448164080838924.jpg")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
