from telepyrobot.__main__ import TelePyroBot
from pyrogram.types import Message


async def admin_check(c: TelePyroBot, m: Message) -> bool:
    chat_id = m.chat.id
    user_id = m.from_user.id

    check_status = await c.get_chat_member(chat_id=chat_id, user_id=user_id)
    admin_strings = ["creator", "administrator"]
    if check_status.status not in admin_strings:
        return False
    else:
        return True