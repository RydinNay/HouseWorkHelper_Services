from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class StartFoodServicesKB:
    kb = [
        [
            KeyboardButton(text="Meal recipe"),
            KeyboardButton(text="Meals by main ingredient"),
            KeyboardButton(text="Meals by category"),
            KeyboardButton(text="Meals by area"),

            KeyboardButton(text="To main menu")
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Send your phone, if you register, else request the link and registrate in our service"
    )
