from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from api import urls
from secure import encrypt_message

async def make_inline_group(groups,is_admin=False,admin_id=None):
    keyboard = InlineKeyboardBuilder()
    for group in groups:
        keyboard.add(
            InlineKeyboardButton(
                text=f"📚 {group['name']}",
                callback_data=f"group^{group['id']}^{group['name']}"
            )
        )
    if is_admin and admin_id:
        decrypted_id=encrypt_message(str(admin_id))
        keyboard.add(InlineKeyboardButton(text="🛠Admin panel",url=urls.frontend_url+f'?admin_id={decrypted_id}'))
    keyboard.adjust(2)
    return keyboard.as_markup()

async def choose_inline(group_id,group_name):
    schedular=InlineKeyboardBuilder()
    schedular.add(
        InlineKeyboardButton(
            text="🗓Bugungi jadval",
            callback_data=f'daily^{group_id}^{group_name}'
        ),InlineKeyboardButton(
            text="📅 Haftalik jadval",
            callback_data=f'weekly^{group_id}^{group_name}'
        ),
        InlineKeyboardButton(text='⬅️ back',callback_data="back_choose"),

    )
    schedular.adjust(2)
    return schedular.as_markup()


back_ikb=InlineKeyboardBuilder()
back_ikb.add(InlineKeyboardButton(text='return',callback_data="back_schedule"))
back_ikb.as_markup()

