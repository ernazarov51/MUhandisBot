import os

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import html, F
from bot import scripts as s
from bot.buttons.inline import make_inline_group, choose_inline, back_ikb
from bot.routers import main_router
from api import scripts
from api import urls
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    groups=scripts.get_data(urls.groups)
    admins=os.getenv("ADMIN").split(',')
    is_admin=True if str(message.from_user.id) in admins else False
    ikb= await make_inline_group(groups,is_admin)
    await message.answer(f"Assalomu Alaykum, {html.bold(message.from_user.full_name)}!\n📚 Guruhingizni tanlang",reply_markup=ikb)

@main_router.callback_query(F.data.startswith('group'))
async def handle_group(callback: CallbackQuery):
    group_id = int(callback.data.split('^')[1])
    group_name=callback.data.split('^')[2]
    ikb = await choose_inline(group_id,group_name)

    await callback.message.edit_text(
        text=f"Guruh Nomi: {group_name}\nTanlang:",
        reply_markup=ikb
    )

    await callback.answer()


@main_router.callback_query(F.data.startswith('weekly'))
async def handle_choose(callback:CallbackQuery):
    group_id = int(callback.data.split('^')[1])
    group_name = callback.data.split('^')[2]
    data=scripts.get_data(urls.get_lesson_list_by_group(group_id))
    text=await s.format_lesson_weekly(group_name,data)
    await callback.message.edit_text(
        text=text,reply_markup=back_ikb.as_markup()
    )


@main_router.callback_query(F.data.startswith('daily'))
async def handle_choose2(callback:CallbackQuery):
    group_id = int(callback.data.split('^')[1])
    group_name = callback.data.split('^')[2]
    data=scripts.get_data(urls.get_lesson_list_by_group(group_id))
    text=await s.format_lesson_daily(group_name,data)
    await callback.message.edit_text(
        text=text,reply_markup=back_ikb.as_markup()
    )

@main_router.callback_query(F.data.startswith('back'))
async def handle_back(callback:CallbackQuery):
    groups = scripts.get_data(urls.groups)
    admins = os.getenv("ADMIN").split(',')
    is_admin = True if str(callback.message.chat.id) in admins else False
    ikb = await make_inline_group(groups, is_admin)
    await callback.message.edit_text(f"{html.bold(callback.message.from_user.full_name)}!\n📚 Guruhingizni tanlang",
                         reply_markup=ikb)
