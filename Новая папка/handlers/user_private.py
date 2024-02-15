import os

from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

from kbds import reply

buttons_names = ['Проф. союз']

user_private_router = Router()

@user_private_router.message(CommandStart())
async def strt_cmd(message: types.Message):
    await message.answer('Добро пожаловать в чат-бот ГДИ!', reply_markup=reply.get_start_keyboard())

@user_private_router.message(F.text == ('Редактировать'))
async def proc4_cmd(message: types.Message):
    admnin_id = str(os.getenv('ADMIN_ID'))
    user_id = str(message.from_user.id)
    if admnin_id == user_id:
        await message.answer('Редактирование', reply_markup=reply.get_edit_keyboard())

@user_private_router.message(F.text.startswith('--'))
async def proc2_cmd(message: types.Message):
    situation_name = message.text
    msg = reply.get_situation_content(situation_name)
    if msg != '':
        await message.answer(msg, reply_markup=reply.get_start_keyboard())
    else:
        await message.answer('К сожалению, контент отсутствует', reply_markup=reply.get_start_keyboard())

@user_private_router.message(F.text.startswith('-'))
async def proc1_cmd(message: types.Message):
    msg = message.text
    await message.answer('Ситуация', reply_markup=reply.get_situations_keyboard(msg))


# @user_private_router.message(F.text == ('Направление 1'))
# async def proc1_cmd(message: types.Message):
#     await message.answer('Направление_1', reply_markup=reply.start_kb2)


# @user_private_router.message(F.text == ('Направление 1'))
# async def proc1_cmd(message: types.Message):
#     await message.answer('Направление_1', reply_markup=reply.start_kb2)

# @user_private_router.message(F.text == ('Направление 2'))
# async def proc2_cmd(message: types.Message):
#     await message.answer('Направление_2', reply_markup=reply.start_kb2)

# @user_private_router.message(F.text == ('Направление 3'))
# async def proc3_cmd(message: types.Message):
#     await message.answer('Направление_3', reply_markup=reply.start_kb2)

# @user_private_router.message(F.text.contains('Жизненная ситуация'))
# async def answ_cmd(message: types.Message):
#     await message.answer('Наполнение кнопки', reply_markup=reply.g2_main)

@user_private_router.message(F.text == ('Главное меню'))
async def g_main(message: types.Message):
    await message.answer('Главная', reply_markup=reply.get_start_keyboard())

@user_private_router.message()
async def unread_msg(message: types.Message):
    await message.answer('Не понимаю что это значит, я только учусь.')