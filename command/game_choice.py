from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from buttons.prof_kbrd import make_row_keyboard


router = Router()


available_hero_names = ["Mage", "Archer", "Berserk"]
available_hero_skills = ["Rookie", "Amateur", "Hardcore"]

class ChoiceHeroNames(StatesGroup):
     choice_hero_names = State()
     choice_hero_skills = State()


#Хэндлер на команду /hero
@router.message(Command("hero"))
async def cmd_hero(message: types.Message, state: FSMContext):
   name = message.chat.first_name
   await message.answer(f"Nice, {name}, выбери героя", reply_markup=make_row_keyboard(available_hero_names))
   await state.set_state(ChoiceHeroNames.choice_hero_names)



@router.message(ChoiceHeroNames.choice_hero_names, F.text.in_(available_hero_names))
async def hero_choose(message: types.Message, state: FSMContext):
   await state.update_data(chosen_hero=message.text.lower())
   await message.answer(f"Thanks, now choose your skill", reply_markup=make_row_keyboard(available_hero_skills))
   await state.set_state(ChoiceHeroNames.choice_hero_skills)



@router.message(ChoiceHeroNames.choice_hero_names)
async def hero_chosen_incorrectly(message: types.Message):

       await message.answer(f"Hero not found", reply_markup=make_row_keyboard(available_hero_names))


@router.message(ChoiceHeroNames.choice_hero_skills, F.text.in_(available_hero_skills))
async def skill_choose(message: types.Message, state: FSMContext):
   user_data = await state.get_data()
   await message.answer(f"You chose {message.text.lower()} skill. Your hero {user_data.get("chosen_hero")}" , reply_markup=types.ReplyKeyboardRemove())

   await state.clear()



@router.message(ChoiceHeroNames.choice_hero_skills)
async def skill_chosen_incorrectly(message: types.Message):

       await message.answer(f"I dont know this skill", reply_markup=make_row_keyboard(available_hero_skills))
