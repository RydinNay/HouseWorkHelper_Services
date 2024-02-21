from aiogram import Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from markups.main_buttons import StartKeyboard, RegistrateKeyboard, MainKeyboard
from requests_to_api.main_requests import start_request

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    start_kb = StartKeyboard.keyboard
    await message.answer(text=f"To identifi you {message.from_user.full_name} as a user i must take your telephone number", reply_markup = start_kb)


@router.message(or_f(Command("registrate"), F.text.lower() == "registrate"))
async def is_register_or_not(message: Message):
    registrate_kb = RegistrateKeyboard.keyboard
    await message.answer(text=f"Click on this button to registrate", reply_markup=registrate_kb)


@router.message(F.contact)
async def phone_callback(message: Message):
    phone_number = message.contact.phone_number
    print(phone_number)

    response = start_request(phone_number)
    print(response)
    if response is not None:
        main_kb = MainKeyboard.keyboard
        await message.answer(f"Ok, {response}", reply_markup=main_kb)
    else:
        registrate_kb = RegistrateKeyboard.keyboard
        await message.answer(f"You are not register yet, you can registrate here", reply_markup=registrate_kb)


@router.message(F.text.lower() == "create a list of products to buy")
async def food(message: Message):
    await message.answer("make a list")


@router.message(F.text.lower() == "create schedule for housework on week")
async def food(message: Message):
    await message.answer("make a schedule")


@router.message(F.text.lower() == "to main menu")
async def to_main_menu(message: Message, state: FSMContext):
    main_kb = MainKeyboard.keyboard
    await state.clear()
    await message.answer("Here we are", reply_markup=main_kb)
