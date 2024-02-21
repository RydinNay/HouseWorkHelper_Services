from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


class StartKeyboard:
    kb = [
        [
            KeyboardButton(text="Send phone number", request_contact=True),
            KeyboardButton(text="Registrate")
        ],
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Send your phone, if you register, else request the link and registrate in our service"
    )


class RegistrateKeyboard:
    kb = [
        [
            InlineKeyboardButton(text="Registrate Link", url="https://docs.aiogram.dev/uk-ua/latest/index.html")
        ]
    ]

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=kb
    )


class MainKeyboard:
    kb = [
        [
            KeyboardButton(text="I want to eat something"),
            KeyboardButton(text="Create a list of products to buy"),
            KeyboardButton(text="Create schedule for housework on week")
        ]
    ]

    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="There is main features of our app"
    )
