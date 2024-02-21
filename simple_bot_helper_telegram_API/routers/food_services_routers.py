import asyncio

from aiogram import Router, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from aiogram.types import Message

from markups.food_services_markup import StartFoodServicesKB
from markups.main_buttons import MainKeyboard
from requests_to_api.food_services_requests import get_meal_recipe, get_meals_by_main_ingredient, \
    get_meals_by_category, get_meals_by_area

router = Router()


class Form(StatesGroup):
    meal_recipe_s = State()
    meal_ing_s = State()
    meal_category_s = State()
    meal_area_s = State()


@router.message(F.text.lower() == "i want to eat something")
async def food_services_start(message: Message):
    keyboard = StartFoodServicesKB.keyboard
    await message.answer("eat something", reply_markup=keyboard)


@router.message(F.text.lower() == "meal recipe")
async def meal_recipe(message: Message, state: FSMContext):
    await state.set_state(Form.meal_recipe_s)
    await message.answer("Enter meal name:")


@router.message(F.text.lower() == "meals by main ingredient")
async def meals_ingredient(message: Message, state: FSMContext):
    await state.set_state(Form.meal_ing_s)
    await message.answer("Enter meal ingredient:")


@router.message(F.text.lower() == "meals by category")
async def meal_category(message: Message, state: FSMContext):
    await state.set_state(Form.meal_category_s)
    await message.answer("Enter meal category:")


@router.message(F.text.lower() == "meals by area")
async def meal_area(message: Message, state: FSMContext):
    await state.set_state(Form.meal_area_s)
    await message.answer("Enter meal area:")


# -------------------------------------------------------------------


@router.message(Form.meal_recipe_s)
async def get_meal_name_from_user(message: Message, state: FSMContext):
    answer = get_meal_recipe(message.text)
    keyboard = MainKeyboard.keyboard
    await message.answer(answer, reply_markup=keyboard)
    await state.clear()


@router.message(Form.meal_ing_s)
async def get_ingredient_from_user(message: Message, state: FSMContext):
    data = get_meals_by_main_ingredient(message.text)
    keyboard = MainKeyboard.keyboard
    await message.answer(f"Here is some meals by this ingredient:")
    for i in range(len(data)):
        await message.answer(f"{i} meal:\r\n"
                             f"{data[f'Meal{i}']['meal_name']}", reply_markup=keyboard)
        if i == 10:
            break
    await state.clear()


@router.message(Form.meal_category_s)
async def get_category_of_meal_from_user(message: Message, state: FSMContext):
    data = get_meals_by_category(message.text)
    keyboard = MainKeyboard.keyboard
    await message.answer(f"Here is some meals in that category:")
    for i in range(len(data)):
        await message.answer(f"{i} meal:\r\n"
                             f"{data[f'Meal{i}']['meal_name']}", reply_markup=keyboard)
        if i == 10:
            break
    await state.clear()


@router.message(Form.meal_area_s)
async def get_meal_area_from_user(message: Message, state: FSMContext):
    data = get_meals_by_area(message.text)
    keyboard = MainKeyboard.keyboard
    await message.answer(f"Here is some meals in that area:")
    for i in range(len(data)):
        await message.answer(f"{i} meal:\r\n"
                             f"{data[f'Meal{i}']['meal_name']}", reply_markup=keyboard)
        if i == 10:
            break
    await state.clear()
