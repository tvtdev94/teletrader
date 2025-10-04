from telegram import Update
from config.settings import ALLOWED_USER_IDS
from config.messages import get_message


def is_authorized(user_id: int) -> bool:
    """Check if user is authorized"""
    return str(user_id) in ALLOWED_USER_IDS


async def check_auth(update: Update, context) -> bool:
    """Check authorization middleware"""
    user_id = update.effective_user.id

    if not is_authorized(user_id):
        lang = context.user_data.get("lang", "vi")
        await update.message.reply_text(get_message("unauthorized", lang))
        return False

    return True
