import logging
import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher import FSMContext


logging.basicConfig(level=logging.INFO)
API_TOKEN = os.environ['TOKEN']
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Bu bot 5ta unli harifdan kop bolgan habarni ochirib tahslaydi")
    # await state.set_state('start')

@dp.message_handler()
async def handle_message(message: types.Message):
    text = message.text.lower()
    vowel_count = sum(text.count(vowel) for vowel in 'aeiou')

    if vowel_count > 5:
        await message.answer("Bu habarda unli harflar soni 5tadan kop!")
        await message.delete()
    else:
        await message.answer("Bu habarda unli harflar soni 5tadan kam!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
