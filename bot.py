import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from keyboards import start_keyboard, links_keyboard, dynamic_keyboard_initial, dynamic_keyboard_expanded, main_menu_keyboard, all_inline_keyboard, links_menu_keyboard
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def start_command(message: Message):
    """
    Обработчик команды /start. Показывает стартовую инлайн-кнопку.
    """
    await message.answer("Нажмите Старт для запуска бота на луну)))", reply_markup=start_keyboard())

@dp.callback_query(F.data == "start")
async def start_callback(callback: CallbackQuery):
    """
    Обработчик нажатия на кнопку Старт. Показывает главное меню.
    """
    await callback.message.edit_text(
        f"Привет {callback.from_user.full_name}, я бот!",
        reply_markup=await main_menu_keyboard()
    )

@dp.callback_query(F.data == "hello")
async def hello_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Привет. Показывает приветствие и главное меню.
    """
    if callback.message.text == f"Привет, {callback.from_user.full_name}!":
        await callback.answer("Вы уже нажали Привет!", show_alert=True)
        return
    await callback.message.edit_text(
        f"Привет, {callback.from_user.full_name}!",
        reply_markup=await main_menu_keyboard()
    )

@dp.callback_query(F.data == "goodbye")
async def goodbye_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Пока. Показывает прощание и главное меню.
    """
    await callback.message.edit_text(
        f"До свидания, {callback.from_user.full_name}!",
        reply_markup=await main_menu_keyboard()
    )

@dp.callback_query(F.data == "all_links")
async def all_links_handler(callback: CallbackQuery):
    """
    Обработчик кнопки /links. Показывает меню ссылок.
    """
    await callback.message.edit_text(
        "Выберите категорию:",
        reply_markup=links_keyboard()
    )

@dp.callback_query(F.data == "all_dynamic")
async def all_dynamic_handler(callback: CallbackQuery):
    """
    Обработчик кнопки /dynamic. Показывает динамическое меню.
    """
    await callback.message.edit_text(
        "Динамическое меню:",
        reply_markup=dynamic_keyboard_initial()
    )

@dp.callback_query(F.data == "show_menu")
async def show_menu_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Меню. Показывает меню с кнопками /links и /dynamic.
    """
    await callback.message.edit_text(
        "Меню:",
        reply_markup=links_menu_keyboard()
    )

@dp.callback_query(F.data == "show_more")
async def show_more_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Показать больше. Показывает расширенное динамическое меню.
    """
    await callback.message.edit_text(
        "Выберите опцию:",
        reply_markup=dynamic_keyboard_expanded()
    )

@dp.callback_query(F.data == "option_1")
async def option_1_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Опция 1. Показывает выбранную опцию и кнопку Меню.
    """
    from keyboards import InlineKeyboardBuilder, InlineKeyboardButton
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Меню", callback_data="show_menu"))
    await callback.message.edit_text(
        "Вы выбрали Опцию 1",
        reply_markup=builder.as_markup()
    )

@dp.callback_query(F.data == "option_2")
async def option_2_handler(callback: CallbackQuery):
    """
    Обработчик кнопки Опция 2. Показывает выбранную опцию и кнопку Меню.
    """
    from keyboards import InlineKeyboardBuilder, InlineKeyboardButton
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Меню", callback_data="show_menu"))
    await callback.message.edit_text(
        "Вы выбрали Опцию 2",
        reply_markup=builder.as_markup()
    )

@dp.message(Command("links"))
async def links_command(message: Message):
    """
    Обработчик команды /links. Показывает меню ссылок (инлайн-клавиатура).
    """
    await message.answer("Выберите категорию:", reply_markup=links_keyboard())

@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    """
    Обработчик команды /dynamic. Показывает динамическое меню (инлайн-клавиатура).
    """
    await message.answer("Динамическое меню:", reply_markup=dynamic_keyboard_initial())

async def main():
    """
    Запуск бота.
    """
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())