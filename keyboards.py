from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Заказать бота", callback_data="g")],
[InlineKeyboardButton(text="Заказать сайт", callback_data="h")],
[InlineKeyboardButton(text="Заказать приложение/игру",callback_data="y")],
[InlineKeyboardButton(text="О нас", callback_data="j")],
[InlineKeyboardButton(text="Вступить в нашу команду", callback_data="f")],
[InlineKeyboardButton(text="Научиться программировать", callback_data="s")],
[InlineKeyboardButton(text="Заказать рекламу", callback_data="m")]])





botik = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Боты с базами данных и нейросетями", callback_data="w")],
                                            [InlineKeyboardButton(text="Бот с кнопочками (Reply и Inline клавиатуры)", callback_data="q")],
                                            [InlineKeyboardButton(text="Бот который отвечает только текстом и фотографиями", callback_data="n")]])


sait = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Сайты с текстом, фотографиями, JS и базой данных", callback_data="sait_max")],
                                            [InlineKeyboardButton(text="Сайт с текстом, фотографиями и JS", callback_data="norm_sait")],
                                            [InlineKeyboardButton(text="Сайт с текстом и фотографиями", callback_data="sait")]])

prilo = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Заказать игру", callback_data="igra")],
                                            [InlineKeyboardButton(text="Заказать приложение", callback_data="no_igra")]])