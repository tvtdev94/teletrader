from telegram import Update
from telegram.ext import ContextTypes
from config.messages import get_message
from services.trading_api import trading_api
from utils.decorators import auth_required


@auth_required
async def scan_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /scan command - Trigger Discord scan"""
    lang = context.user_data.get("lang", "vi")

    # Send loading message
    msg = await update.message.reply_text(get_message("scan_started", lang))

    try:
        result = await trading_api.scan_now()
        count = result.get("count", 0)
        await msg.edit_text(get_message("scan_success", lang).format(count))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def execute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /execute command - Execute auto signals"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("execute_started", lang))

    try:
        result = await trading_api.execute_auto()
        count = result.get("count", 0)
        await msg.edit_text(get_message("execute_success", lang).format(count))
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


async def scan_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle scan button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("scan_started", lang))

    try:
        result = await trading_api.scan_now()
        count = result.get("count", 0)
        await query.edit_message_text(get_message("scan_success", lang).format(count))
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))


async def execute_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle execute button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("execute_started", lang))

    try:
        result = await trading_api.execute_auto()
        count = result.get("count", 0)
        await query.edit_message_text(get_message("execute_success", lang).format(count))
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))
