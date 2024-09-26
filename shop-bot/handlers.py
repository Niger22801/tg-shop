import random
import sqlite3

from aiogram import Bot, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from config import Ser
from config import Kiber
from config import Kiber1
from config import Kiber2
from config import Kiber4
from config import Updatee
from config import Send
from config import Zakaz
from config import Tcodee
from config import Tcodee1
from keyboard import keyboard12, online, adminpanel, under, updater, gg, prisekey, reply,  keyboard_1,nazad_kb
from main import dp

# @dp.message()
# async def wasd(message: Message, bot: Bot):
#     print('vavavava')
#     print(message.from_user.id)
#     await message.answer(message.video.file_id)
#     #await bot.send_audio(message.from_user.id, 'CQACAgIAAxkBAAOFZdG38Ql4Lcz-ESJ9G7EfvJWEo88AAlE8AALAuJBKzFOlwqzQI_E0BA')
# @dp.message()
# async def sendphoto(message: Message, state: FSMContext):
#     await message.answer( text=str(message.photo[-1].file_id))
# @dp.message(F.text)
# async def wasd(callback:CallbackQuery, bot: Bot):
#     await bot.send_message(callback.from_user.id,text=f'{str(callback.from_user.id)}')

joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

con = sqlite3.connect("offers.db")
cursor = con.cursor()

con.commit()
a = [0]
nnn = 0


# @dp.message(Command('prise'))
# async def prise(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     await bot.send_message(group_id,text='Сообщение')
# AgACAgIAAxkBAAN1Zg2d4jbfUfS-T_-bx3FTudPr8AIAAhjhMRvubHBITqLJzG3bmNcBAAMCAAN4AAM0BA
# ----------------------------------------------
chat_id1 = '1488'
@dp.message(F.text == '/start')
async def start(callback: Message, state: FSMContext, bot: Bot):
    for a in range(callback.message_id-10,callback.message_id):
        try:
            await bot.delete_message(chat_id=callback.chat.id,message_id=a)
        except:
            print('gg')
    global chat_id1
    chat_id1 = callback.chat.id
    await state.clear()
    if not str(callback.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(callback.chat.id) + "\n")
    await bot.send_message(callback.from_user.id,
                           f'Приветствуем {callback.from_user.full_name} \nНастало время углубиться в бот-помощника и функционал.\nПредоставляем: \n\n- Быстрое ознакомление с ассортиментом магазина 👔\n\n- Упрощенная система оформления заказов ✌🏻\n\n- Получение важной для вас информации ℹ️\n\nИ многое другое…',
                           reply_markup=keyboard12)
    await state.update_data(id=callback.message_id)


@dp.message(F.text == 'Главное меню')
async def search(callback: Message, state: FSMContext, bot: Bot):
    await state.clear()

    for a in range(callback.message_id-10,callback.message_id):
        try:
            await bot.delete_message(chat_id=callback.chat.id,message_id=a)
        except:
            print('gg')

    await bot.send_message(callback.from_user.id,
                           f'COOLSHOP ©\n\nПриветствуем, {callback.from_user.full_name} \nНастало время углубиться в бот-помощника и функционал.\nПредоставляем: \n\n- Быстрое ознакомление с ассортиментом магазина 👔\n\n- Упрощенная система оформления заказов ✌🏻\n\n- Получение важной для вас информации ℹ️\n\nИ многое другое…',
                           reply_markup=keyboard12)
    await state.update_data(id=callback.message_id)

# --------------------------------------------
@dp.callback_query(F.data == 'search')
async def search(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Введите атрибут поиска')
    await state.set_state(Ser.name)


@dp.message(Ser.name)
async def ser(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute(f'SELECT * FROM nike WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()

    cursor.execute(f'SELECT * FROM adidas WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()

    cursor.execute(f'SELECT * FROM puma WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()

    cursor.execute(f'SELECT * FROM balance WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()

    cursor.execute(f'SELECT * FROM other WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()

    cursor.execute(f'SELECT * FROM reebok WHERE name = ?', (str(callback.text),))
    for off in cursor.fetchall():
        await bot.send_photo(callback.from_user.id, photo=off[4])
        await  bot.send_message(callback.from_user.id, f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                                reply_markup=gg)
    con.commit()
    await state.clear()


# --------------------------------------------
@dp.callback_query(F.data == 'get_code')
@dp.callback_query(F.data == 'get_code')
async def code(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='📲Напишите ваш номер телефона в международном формате без "+" вначале: 375331111111')
    await state.set_state(Tcodee1.name)


@dp.message(Tcodee1.name)
async def code(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute(f"SELECT * FROM code WHERE number={str(callback.text)}")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"Ваш трек код:   {off[2]}")
    if not callback.text in cursor.fetchall():
        await bot.send_message(callback.from_user.id, text='Записей не найдено', reply_markup=nazad_kb)

    con.commit()




# --------------------------------------------
@dp.callback_query(F.data == 'tcode')
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Введите номер телефона покупателя без "+" в начале')
    await state.set_state(Tcodee.name)


@dp.message(Tcodee.name)
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(num=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите трек код')
    await state.set_state(Tcodee.name1)


@dp.message(Tcodee.name1)
async def tcode(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f"INSERT INTO code (number, trek) VALUES ({str(data1['num'])}, {str(callback.text)})")
    con.commit()
    await bot.send_message(callback.from_user.id, text='Добавлено')
    await state.clear()


# -------------------------------------------
@dp.callback_query(F.data == 'update')
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM offers")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
    await state.set_state(Updatee.name)
    con.commit()


#
# @dp.callback_query(F.data == 'nike_up')
# async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     cursor.execute("SELECT * FROM nike")
#     for off in cursor.fetchall():
#         await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
#     await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите изменить')
#     await state.set_state(Updatee.name)
#     await state.update_data(firm='nike')
#     con.commit()


@dp.message(Updatee.name)
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(id=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите новые размеры')
    await state.set_state(Updatee.name1)


@dp.message(Updatee.name1)
async def upd(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f"UPDATE offers SET sizes =? WHERE id=?", (str(callback.text), str(data1["id"])))
    # cursor.execute(f'UPDATE {data1["firm"]} SET size ={str(callback.text)} WHERE id={str(data1["id"])}')
    con.commit()
    await bot.send_message(callback.from_user.id, text='обновлено')
    await state.clear()


# ------------------------------------------
# @dp.callback_query(F.data == 'delete')
# async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     await bot.send_message(callback.from_user.id,text='Выбрите тип товара для удаления', reply_markup=offers_del)

@dp.callback_query(F.data == 'cloth_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM cloth")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(type='cloth')
    con.commit()


@dp.callback_query(F.data == 'shoes_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM shoes")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(type='shoes')
    con.commit()


@dp.callback_query(F.data == 'other_del')
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    cursor.execute("SELECT * FROM other")
    for off in cursor.fetchall():
        await  bot.send_message(callback.from_user.id, f"{off[0]} - {off[1]}")
    await bot.send_message(callback.from_user.id, text='Введите id товара, который хотите удалить')
    await state.set_state(Kiber4.name)
    await state.update_data(type='other')
    con.commit()


@dp.message(Kiber4.name)
async def minus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f'DELETE FROM {data1["type"]} WHERE id = ?', (int(callback.text),))
    con.commit()
    await bot.send_message(callback.from_user.id, text='Удалено')
    await state.clear()


# -----------------------------------------
@dp.callback_query(F.data == 'offersss')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           'Это начало оформления заказа\n\nУ вас обязательно должен быть тег профиля в телеграм\n\n')
    await bot.send_message(callback.from_user.id,
                           text='Введите количество, которое хотите приобрести\n\nОформление заказа можно прекратить при помощи /start')
    await state.set_state(Zakaz.name1)


@dp.message(Zakaz.name1)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(count=callback.text)
    await bot.send_message(callback.from_user.id,
                           text='Введите размер\n\nОформление заказа можно прекратить при помощи /start')
    await state.set_state(Zakaz.name2)


@dp.message(Zakaz.name2)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(size=str(callback.text))
    await bot.send_message(callback.from_user.id,
                           text='Выберите способ доставки\n\nОформление заказа можно прекратить при помощи /start',
                           reply_markup=reply)


@dp.callback_query(F.data == 'bel')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='Для заказа Белпочтой:\n1:ФИО\n2:Полный адрес проживания\n3:Номер телефона\n4:Индекс')
    await state.update_data(post='Белпочта')
    await state.set_state(Zakaz.name3)


@dp.callback_query(F.data == 'euro')
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id,
                           text='Для заказа Европочтой:\n1:ФИО\n2:Номер Телефона \n3:Адрес или номер отделения в городе Европочты')
    await state.update_data(post='Европочта')
    await state.set_state(Zakaz.name3)


@dp.message(Zakaz.name3)
async def offer(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, 'Ждите подтверждения заказа от администратора')
    data1 = await state.get_data()
    n1 = data1['n']
    cursor.execute(f"SELECT * FROM {data1['type']}")
    off = cursor.fetchall()[n1]
    await bot.send_photo(callback.from_user.id, photo=off[3])
    await bot.send_message(chat_id=1488076193,
                           text=f'Название: {off[0]}\nКоличество: {data1["count"]}\nРазмер: {data1["size"]}\nПокупатель: @{callback.from_user.username}, {callback.from_user.full_name}\n\n{data1["post"]}:\n{callback.text}')
    await state.clear()


# ----------------------------------------------
@dp.callback_query(F.data == 'offerss')
async def offers(callback: Message, state: FSMContext, bot: Bot):
    data = await state.get_data()
    await bot.delete_message(chat_id=chat_id1,message_id=data['id']+1)
    print(data['id'])
    await bot.send_message(callback.from_user.id, text='Товары',reply_markup=nazad_kb)
    await bot.send_message(callback.from_user.id, text='Выберите тип товара:', reply_markup=keyboard_1)

    # await state.update_data(id=callback.message_id)



# ---------------------------------------------------------------------
@dp.callback_query(F.data == 'cloth')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM cloth')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM cloth")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id,
                           text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(type='cloth')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'shoes')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM shoes')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM shoes")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id,
                           text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(type='shoes')
    await state.update_data(n=0)


@dp.callback_query(F.data == 'other')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    global n
    n = 0
    cursor.execute(f'SELECT COUNT(*) FROM other')
    total = cursor.fetchone()[0]
    a = n + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute("SELECT * FROM other")
    off = cursor.fetchall()[n]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id,
                           text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(type='other')
    await state.update_data(n=0)


# ---------------------------------------------------------------------------------
@dp.callback_query(F.data == 'wpered')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data11 = await state.get_data()
    n1 = data11['n']
    n1 += 1

    cursor.execute(f'SELECT COUNT(*) FROM {data11["type"]}')
    total = cursor.fetchone()[0]
    a = n1 + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute(f"SELECT * FROM {data11['type']}")
    off = cursor.fetchall()[n1]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id,
                           text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()

    await state.set_state(Kiber1.name)
    await state.update_data(n=n1)


@dp.callback_query(F.data == 'nazad')
async def offers(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    await bot.delete_message(chat_id=chat_id1,message_id=data['id']+1)
    data11 = await state.get_data()
    n1 = data11['n']
    n1 -= 1

    cursor.execute(f'SELECT COUNT(*) FROM {data11["type"]}')
    total = cursor.fetchone()[0]
    a = n1 + 1
    await bot.send_message(callback.from_user.id, text=f'[{a} из {total}]')
    con.commit()
    cursor.execute(f"SELECT * FROM {data11['type']}")
    off = cursor.fetchall()[n1]
    await bot.send_photo(callback.from_user.id, photo=off[4])
    await bot.send_message(callback.from_user.id,
                           text=f'{off[1]}          \n\nЦена: {off[2]}\n\nРазмеры: {off[3]}',
                           reply_markup=under)
    con.commit()
    await state.set_state(Kiber1.name)
    await state.update_data(n=n1)


@dp.callback_query(F.data == 'home')
async def home(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.clear()
    await bot.send_message(callback.from_user.id,
                           f'COOLSHOP ©\n\nППриветствуем, … \nНастало время углубиться в бот-помощника и функционал.\nПредоставляем: \n\n- Быстрое ознакомление с ассортиментом магазина 👔\n\n- Упрощенная система оформления заказов ✌🏻\n\n- Получение важной для вас информации ℹ️\n\nИ многое другое…',
                           reply_markup=keyboard12)


@dp.callback_query(F.data == 'info')
async def info(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    print(data['id'])
    await bot.delete_message(chat_id=chat_id1,message_id=data['id']+1)
    await bot.send_message(callback.from_user.id,
                           text='Приветствуем вас, уважаемый клиент 🤝🏻\n\nВы перешли по вкладке -«Полная информация»\n\nЧто представляет из себя магазин ?\n1) В нашем магазине достаточно большой выбор трендовой, качественной и разнообразной одежды на любой вкус 🫦💄\n2) БЕСПЛАТНАЯ доставка по всей РБ‼️\n- Европочта\n- Бел почта (5 BYN)\n3) Присутствует возврат/обмен товара\n4) Данный бот имеет функции:\n- Поможет выбрать нужную одежду, предоставит наличие\n- Свяжет вас с администратором и менеджером в течении (5 минут) \n- Найти нас в других социальных сетях и быть ближе к команде COOLSHOP \n\nХорошего пользования и удачных покупок 😉🔥 ',reply_markup=nazad_kb)


# ---------------------------------------------------------------------------------------
@dp.message(Command('admin'))
async def admin(callback: CallbackQuery, state: FSMContext, bot: Bot):
    if callback.from_user.id == 1488076193 or callback.from_user.id == 1043137371 or callback.from_user.id == 7324053113:
        await bot.send_message(callback.from_user.id, text='Здравствуйте, администратор', reply_markup=adminpanel)


# @dp.callback_query(F.data == 'plus')
# async def plus(callback: CallbackQuery, state: FSMContext, bot: Bot):
#     await bot.send_message(callback.from_user.id, text='Выберите тип товара',reply_markup=offers_add)

@dp.callback_query(F.data == 'cloth_add')
async def plus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(type='cloth')


@dp.callback_query(F.data == 'shoes_add')
async def plus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(type='shoes')


@dp.callback_query(F.data == 'other_add')
async def plus(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await bot.send_message(callback.from_user.id, text='Ведите название товара')
    await state.set_state(Kiber.name)
    await state.update_data(type='other')


@dp.message(Kiber.name)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(name=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите цену')
    await state.set_state(Kiber.name1)


@dp.message(Kiber.name1)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(price=callback.text)
    await bot.send_message(callback.from_user.id, text='Введите размеры')
    await state.set_state(Kiber.name3)


@dp.message(Kiber.name3)
async def zakaz(callback: CallbackQuery, state: FSMContext, bot: Bot):
    await state.update_data(size=callback.text)
    await bot.send_message(callback.from_user.id, text='Отправьте фотографию')
    await state.set_state(Kiber.name4)


@dp.message(Kiber.name4)
async def zakaz(message: Message, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    cursor.execute(f"INSERT INTO {data1['type']}(name, price,size,photo) VALUES (?, ?, ?,?)",
                   (data1['name'], data1['price'], data1['size'], str(message.photo[-1].file_id)))
    con.commit()
    await bot.send_message(message.from_user.id, text='Успешно добавлено')
    await state.clear()


@dp.message(Command('sendall'))
async def mess(callback: CallbackQuery, bot: Bot, state: FSMContext):
    if callback.from_user.id == 1488076193 or callback.from_user.id == 1043137371 or callback.from_user.id == 7324053113:
        await bot.send_message(callback.from_user.id, text='Отправьте фотографию')
        await state.set_state(Send.name)
    else:
        await bot.send_message(callback.from_user.id, text='Вы ввели неизвестную команду')


@dp.message(Send.name)
async def send(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(link=message.photo[-1].file_id)
    await bot.send_message(message.from_user.id, text='Введите текст рассылки')
    await state.set_state(Send.name2)


@dp.message(Send.name2)
async def send(callback: CallbackQuery, state: FSMContext, bot: Bot):
    data1 = await state.get_data()
    with open("joined.txt", "r") as file:
        joinedUsers = file.readlines()
        for user in joinedUsers:
            await bot.send_photo(chat_id=user, photo=f'{data1["link"]}')
            await bot.send_message(chat_id=user, text=callback.text)
    await state.clear()


@dp.message(F.text)
async def error_msg(message: Message, bot: Bot, state: FSMContext):
    price = await state.get_data()
    print(price.get("price"))
    await bot.send_message(chat_id=message.from_user.id, text="Вы ввели неизвестную команду")
