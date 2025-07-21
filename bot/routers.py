from aiogram import Router

from config import dp

main_router=Router()
dp.include_router(main_router)