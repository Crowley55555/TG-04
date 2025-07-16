from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard():
    """
    Стартовая инлайн-кнопка для запуска бота.
    """
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Старт", callback_data="start")]
        ]
    )
    return keyboard


async def main_menu_keyboard():
    """
    Главное меню с кнопками Привет, Пока, Меню.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Привет", callback_data="hello"),
        InlineKeyboardButton(text="Пока", callback_data="goodbye"),
        InlineKeyboardButton(text="Меню", callback_data="show_menu")
    )
    builder.adjust(2)
    return builder.as_markup()


def links_keyboard():
    """
    Клавиатура с кнопками-ссылками и кнопкой Меню.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Новости", url="https://news.yandex.ru/"),
        InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru/"),
        InlineKeyboardButton(text="Видео", url="https://www.youtube.com/")
    )
    builder.row(
        InlineKeyboardButton(text="Меню", callback_data="show_menu")
    )
    builder.adjust(1)
    return builder.as_markup()


def dynamic_keyboard_initial():
    """
    Начальная динамическая клавиатура с кнопкой 'Показать больше'.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Показать больше", callback_data="show_more")
    )
    return builder.as_markup()


def dynamic_keyboard_expanded():
    """
    Расширенная динамическая клавиатура с кнопками 'Опция 1', 'Опция 2' и 'Меню'.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Опция 1", callback_data="option_1"),
        InlineKeyboardButton(text="Опция 2", callback_data="option_2")
    )
    builder.row(
        InlineKeyboardButton(text="Меню", callback_data="show_menu")
    )
    return builder.as_markup()


def all_inline_keyboard():
    """
    Клавиатура со всеми основными инлайн-кнопками проекта.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="Привет", callback_data="hello"),
        InlineKeyboardButton(text="Пока", callback_data="goodbye"),
        InlineKeyboardButton(text="/links", callback_data="all_links"),
        InlineKeyboardButton(text="/dynamic", callback_data="all_dynamic")
    )
    builder.adjust(2)
    return builder.as_markup()


def links_menu_keyboard():
    """
    Клавиатура для возврата к меню ссылок и динамического меню.
    """
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text="/links", callback_data="all_links"),
        InlineKeyboardButton(text="/dynamic", callback_data="all_dynamic")
    )
    builder.adjust(2)
    return builder.as_markup()