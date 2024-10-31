from __future__ import annotations
from aiogram.filters import CommandStart
from aiogram.types import Message
from typing import TYPE_CHECKING
from aiogram import Router
from aiogram.filters import Command
from bot.db.create import create_user

if TYPE_CHECKING:
    from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = create_user(user_id=message.from_user.id, 
                                  username=message.from_user.username, 
                                  name=message.from_user.full_name)
    print(user['is_user_created'])
    if user["is_user_created"]:
        await message.answer(f"Salom, {message.from_user.full_name}!\nSizni qayta ko'rib turganimizdan xursandmiz!")  
    else:
        await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!\n")
