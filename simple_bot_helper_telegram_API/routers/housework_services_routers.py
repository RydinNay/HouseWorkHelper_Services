from aiogram import Router, F
from aiogram.types import Message

router = Router()


@router.message(F.text.lower() == "create schedule for housework on week")
async def food(message: Message):
    await message.answer("make a schedule")
