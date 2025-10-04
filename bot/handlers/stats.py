from telegram import Update
from telegram.ext import ContextTypes
from config.messages import get_message
from services.trading_api import trading_api
from utils.decorators import auth_required


@auth_required
async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /stats [period] command"""
    lang = context.user_data.get("lang", "vi")

    period = context.args[0] if context.args else "today"
    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_stats(period)

        text = f"{get_message('stats', lang)} ({period})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Total Trades: {result.get('total_trades', 0)}\n"
        text += f"Wins: {result.get('wins', 0)}\n"
        text += f"Losses: {result.get('losses', 0)}\n"
        text += f"Win Rate: {result.get('win_rate', 0):.1f}%\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        pnl = result.get('total_pnl', 0)
        pnl_emoji = "🟢" if pnl >= 0 else "🔴"
        text += f"Total P&L: {pnl_emoji} ${pnl:,.2f}\n"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


async def stats_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle stats button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_stats("today")

        text = f"{get_message('stats', lang)} (today)\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Trades: {result.get('total_trades', 0)}\n"
        text += f"Win Rate: {result.get('win_rate', 0):.1f}%\n"

        pnl = result.get('total_pnl', 0)
        pnl_emoji = "🟢" if pnl >= 0 else "🔴"
        text += f"P&L: {pnl_emoji} ${pnl:,.2f}\n"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))
