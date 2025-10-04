from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from config.messages import get_message
from config.settings import DEFAULT_LANGUAGE
from bot.keyboards.menus import language_keyboard, main_menu_keyboard
from utils.decorators import auth_required


@auth_required
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    if "lang" not in context.user_data:
        context.user_data["lang"] = DEFAULT_LANGUAGE

    lang = context.user_data["lang"]
    await update.message.reply_text(
        get_message("welcome", lang),
        reply_markup=language_keyboard()
    )


@auth_required
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    lang = context.user_data.get("lang", "vi")
    await update.message.reply_text(get_message("help", lang))


@auth_required
async def lang_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /lang command"""
    args = context.args
    if args and args[0] in ["vi", "en"]:
        context.user_data["lang"] = args[0]
        lang = args[0]
        await update.message.reply_text(get_message("language_selected", lang))
    else:
        await update.message.reply_text(
            "Select language:",
            reply_markup=language_keyboard()
        )


async def language_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle language selection callback"""
    query = update.callback_query
    await query.answer()

    lang = query.data.split("_")[1]  # lang_vi or lang_en
    context.user_data["lang"] = lang

    await query.edit_message_text(
        get_message("language_selected", lang),
        reply_markup=main_menu_keyboard(lang)
    )
