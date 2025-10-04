from telegram import Update
from telegram.ext import ContextTypes
from config.messages import get_message
from services.trading_api import trading_api
from utils.decorators import auth_required


@auth_required
async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /cancel <order_id> command"""
    lang = context.user_data.get("lang", "vi")

    if not context.args:
        await update.message.reply_text("Usage: /cancel <order_id>")
        return

    order_id = context.args[0]
    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        await trading_api.cancel_order(order_id)
        await msg.edit_text(get_message("cancel_success", lang).format(order_id))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def close_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /close <position_id> command"""
    lang = context.user_data.get("lang", "vi")

    if not context.args:
        await update.message.reply_text("Usage: /close <position_id>")
        return

    position_id = context.args[0]
    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        await trading_api.close_position(position_id)
        await msg.edit_text(get_message("close_success", lang).format(position_id))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def pause_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /pause command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        await trading_api.pause_trading()
        await msg.edit_text(get_message("pause_success", lang))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def resume_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /resume command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        await trading_api.resume_trading()
        await msg.edit_text(get_message("resume_success", lang))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))
