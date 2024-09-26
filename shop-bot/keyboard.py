from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types

baggyy = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='✅Заказать', callback_data='zakaz'),
    ]

])

gg = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='✅ заказать', callback_data='offersss'),
    ]

])
prisekey = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='King Kross',url='https://www.instagram.com/gold_sneakers.bl?igsh=OXNsdW5uNWowcWpl'),
        InlineKeyboardButton(text='Gold Sneakers', url='https://www.instagram.com/king_kross.bl?igsh=M3pvZXB2dW5uOWpt')
    ],
    [
        InlineKeyboardButton(text='🎁Участвовать', callback_data='ggg'),
    ]

])


under = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='<<', callback_data='nazad'),
        InlineKeyboardButton(text='✅ заказать', callback_data='offersss'),
        InlineKeyboardButton(text='>>', callback_data='wpered')
    ],
    [
        InlineKeyboardButton(text='🏚вернуться', callback_data='home'),
    ]

])

sizes = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='M/L', callback_data='ml', ),
        InlineKeyboardButton(text='L/XL', callback_data='lxl'),
        InlineKeyboardButton(text='XL/XXL', callback_data='xlxxl'),
    ]

])

updater = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[


    [
        InlineKeyboardButton(text='NIKE', callback_data='nike_up'),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas_up'),
        InlineKeyboardButton(text='PUMA', callback_data='puma_up'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance_up'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok_up')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other_up')
    ]

])

online = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='🔍Поиск', callback_data='search')
    ],
    [
        InlineKeyboardButton(text='NIKE', callback_data='nike'),
        InlineKeyboardButton(text='ADIDAS', callback_data='adidas'),
        InlineKeyboardButton(text='PUMA', callback_data='puma'),
    ],
    [
        InlineKeyboardButton(text='NEW BALANCE', callback_data='balance'),
        InlineKeyboardButton(text='REEBOK', callback_data='reebok')
    ],
    [
        InlineKeyboardButton(text='OTHER', callback_data='other')
    ]

])
adminpanel = InlineKeyboardMarkup(inline_keyboard=
[
    # [
    #     InlineKeyboardButton(text='➕добавить', callback_data='plus'),
    #     InlineKeyboardButton(text='➖удалить', callback_data='delete')
    # ],
    [
        InlineKeyboardButton(text='Добавить трек код',callback_data='tcode')
    ]

])

# offers_add = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
# [
#     [
#         InlineKeyboardButton(text='Одежда', callback_data='cloth_add', ),
#     ],
#     [
#         InlineKeyboardButton(text='Обувь', callback_data='shoes_add'),
#     ],
#     [
#         InlineKeyboardButton(text='Другоу', callback_data='other_add')
#     ]
#
# ])

# offers_del = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
# [
#     [
#         InlineKeyboardButton(text='Одежда', url='https://www.instagram.com/coolshop001/'),
#     ],
#     [
#         InlineKeyboardButton(text='Обувь', url='https://t.me/Cooltrec'),
#     ]
#
# ])

reply = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='✅Да, отправить заказ', callback_data='yesoffer'),
        InlineKeyboardButton(text='❌Нет, отаказаться', callback_data='nooffer'),
    ]

])

keyboard12 = InlineKeyboardMarkup(resize_keyboard=True, inline_keyboard=
[
    [
        InlineKeyboardButton(text='🛍 Товары', callback_data='offerss'),
    ],
    [
        InlineKeyboardButton(text='👤 Связь с разработчиком', url='https://t.me/i_am_devel0per'),
        InlineKeyboardButton(text='ℹ️ Полная информация', callback_data='info'),


    ],

    [
        InlineKeyboardButton(text='📦 Получить трек код',callback_data='get_code')
    ],

])

reply = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='📩Белпочта', callback_data='bel'),
    ],
    [
        InlineKeyboardButton(text='📩Европочта', callback_data='euro'),
    ],

])
kb = [
    [
        types.KeyboardButton(text="Главное меню"),

    ]
]
nazad_kb = types.ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,
)
keyboard_1 = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(text='👕Одежда', url='https://github.com/Niger22801'),
    ],
    [
        InlineKeyboardButton(text='👟Обувь', url='https://github.com/Niger22801'),
    ]
])

# nazad_kb = InlineKeyboardMarkup(inline_keyboard=
# [
#     [
#         InlineKeyboardButton(text='Назад', callback_data='nazad'),
#     ],
# ])