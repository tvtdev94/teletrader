from functools import wraps
from bot.middleware.auth import check_auth


def auth_required(func):
    """Decorator to check authorization"""
    @wraps(func)
    async def wrapper(update, context, *args, **kwargs):
        if not await check_auth(update, context):
            return
        return await func(update, context, *args, **kwargs)
    return wrapper
