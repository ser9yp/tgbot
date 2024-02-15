from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import sqlite3


#Формируем стартовую клавиатуру с кнопками - Направления

def get_vectors():
    connection = sqlite3.connect("./sqlite/db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vectors")
    return cursor.fetchall()

def create_start_kb():
    keyboard = []
    vectors = get_vectors()
    #Перебираем массив кортежей, в которых данные по направлению
    for item in vectors:
        keyboard.append([KeyboardButton(text='-' + str(item[1]))])

    return keyboard

def get_start_keyboard():

    return ReplyKeyboardMarkup(
        keyboard = create_start_kb(),
        resize_keyboard=True,
        input_field_placeholder='Что вас интересует?'
    )

#Конец


#Формируем клавиатуру ситуаций по направлению

def get_vector_id(vector_name):
    connection = sqlite3.connect("./sqlite/db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM vectors WHERE vector_name = ?", (vector_name, ))
    return cursor.fetchone()

def get_situations_by_vector_id(id):
    connection = sqlite3.connect("./sqlite/db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM situations WHERE category = ?", (id, ))
    return cursor.fetchall()

def create_situations_keyboard(keyboard_name):
    keyboard_name = keyboard_name[1::]
    vector_id = int(get_vector_id(keyboard_name)[0])
    situations = get_situations_by_vector_id(vector_id)
    keyboard = []

    for item in situations:
        keyboard.append([KeyboardButton(text='--' + str(item[1]))])

    return keyboard

def get_situations_keyboard(keyboard_name):
    return ReplyKeyboardMarkup(
        keyboard = create_situations_keyboard(keyboard_name),
        resize_keyboard=True,
        input_field_placeholder='Что вас интересует?'
    )

def get_situation_content(name):
    name = name[2::]
    connection = sqlite3.connect("./sqlite/db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM situations WHERE name = ?", (name, ))
    data = cursor.fetchone()
    return data[3]


def get_main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Главное меню"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='Вернуться на главную'
    )

def get_edit_keyboard():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Добавить направление")
            ],
            [
                KeyboardButton(text="Добавить жизненную ситуацию")
            ],
            [
                KeyboardButton(text="Добавить контент")
            ],
            [
                KeyboardButton(text="Главное меню"),
            ],
        ],
        resize_keyboard=True,
        input_field_placeholder='Режим редактирования'
    )

del_kbd = ReplyKeyboardRemove()