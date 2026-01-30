from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, CallbackQuery
from aiogram import Router, F
from config import bot  # импортируем bot для пересылки сообщений
import keyboards as kb
from keyboards import main, botik, sait, prilo

router = Router()

CHAT_ID = '-5093180523'



def is_reply_keyboard_press(message):
    buttons_text = [btn.text for row in main.inline_keyboard for btn in row]


@router.message(CommandStart())
async def cmd_start_help(message: Message):
    await message.answer("Привет! ", reply_markup=kb.main)


@router.callback_query(F.data == "y")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Выбери что тебе нужно", reply_markup=kb.prilo)


@router.callback_query(F.data == "igra")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания игры на заказ\n\n Название проекта: \n\n Жанр игры (RPG, стратегия, квест и т.д.):\n\n Целевая платформа (ПК, мобильные устройства, веб, консоли): \n\n Основная идея и сюжет:Аудитория (возраст, интересы):\n\n Требования к графике и стилю:\n\n Продолжительность игры или уровней:Язык и локализация: \n\n Сроки разработки: \n\n Бюджет: \n\n Ваш ЮЗ: \n\n Дополнительные пожелания: \n\n ПИСАТЬ ОДНИМ СООБЩЕНИЕМ")


@router.callback_query(F.data == "no_igra")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания мобильного приложения на заказ\n\n Название проекта:\n\n Целевая платформа iOS, Android, Web и т.д.:\n\n Основная идея и цели приложения:\n\n Основные функции и особенности:\n\n Целевая аудитория:\n\n Предпочтительный дизайн и стиль:\n\n Требуемые сроки разработки:\n\n Контактная информация:\n\n Ваш ЮЗ \n\n Ваш бюджет \n\n  ПИСАТЬ ОДНИМ СООБЩЕНИЕМ")



@router.callback_query(F.data == "s")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Ты тоже хочешь программировать\n\n Тогда тебе по адресу!\n\n Вот анкета\n\n Компьютер/ноутбук\n\n Какие языки программирования хотите изучать\n\n Что вы в итоге хотите сделать (например:сайт)\n\n На сколько курс вы хотите \n\n Полный курс\n Курс на 1-2 недели\n 1-2 занятия \n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")


@router.callback_query(F.data == "h")
async def g(callback: CallbackQuery):
    await callback.message.answer("Выберите вариант сайта который вам подходит" , reply_markup=kb.sait)


@router.callback_query(F.data == "sait_max")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания сайта \n\nДля чего нужен сайт\n\n Нужно фото (если да, то скиньте фото)\n\n Название\n\n Сколько страниц и что на каждой \n\n Что должно храниться в базе данных \n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")

@router.callback_query(F.data == "norm_sait")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания сайта \n\n Для чего нужен сайт\n\n Нужно фото (если да, то скиньте фото)\n\n Название\n\n Сколько страниц и что на каждой \n\n Где должен использоваться JS \n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")


@router.callback_query(F.data == "sait")
async def we_izbranoe(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания сайта \n\n Для чего нужен сайт\n\n Нужно фото (если да, то скиньте фото)\n\n Название\n\n Сколько страниц и что на каждой \n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")


@router.callback_query(F.data == "g")
async def g(callback: CallbackQuery):
    await callback.message.answer("Выберите вариант бота который вам подходит" , reply_markup=kb.botik)


@router.callback_query(F.data == "w")
async def g(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания бота: \n\n Для чего нужен бот\n\n Аватарка\n\n Название\n\n Сколько кнопок и что происходит если нажимаешь на них\n\n Что должно храниться в базе данных\n\n Нужно ли что-то еще \n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")


@router.callback_query(F.data == "q")
async def g(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания бота:\n\nДля чего нужен бот\n\n Аватарка\n\n Название\n\n Сколько кнопок и что происходит если нажимаешь на них\n\n Ваш бюджет \n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")


@router.callback_query(F.data == "n")
async def g(callback: CallbackQuery):
    await callback.message.answer("Анкета для создания бота: \n\n Для чего нужен бот\n\n Аватарка\n\n Название\n\n Ваш бюджет\n\n ЗАПОЛНЯТЬ 1 СООБЩЕНИЕМ")



@router.callback_query(F.data == "f")
async def f(callback: CallbackQuery):
    await callback.message.answer("Мы пока не берем в нашу комманду! \n\n Напишите позже😉")


@router.callback_query(F.data == "m")
async def m(callback: CallbackQuery):
    await callback.message.answer("Стоимость рекламы от 50 руб в день (рассылка всем пользователя) \n\n По поводу заказа рекламы писать @Alinik2005")


@router.callback_query(F.data == "j")
async def j(callback: CallbackQuery):
    await callback.message.answer('😄Наши программмисты очень опытные ребята😄 \n\n 💎У каждого опыт более 3 лет💎\n\n 🌹Бытро выполняем заказы🌹\n\n 💖Оплата после выполнения💖')

@router.message()
async def forward_non_command_non_reply(message: types.Message):
    await bot.forward_message(chat_id=CHAT_ID, from_chat_id=message.chat.id, message_id=message.message_id)


