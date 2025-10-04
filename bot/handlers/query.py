from telegram import Update
from telegram.ext import ContextTypes
from config.messages import get_message
from services.trading_api import trading_api
from utils.decorators import auth_required


@auth_required
async def balance_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /balance command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_balance()
        available = result.get("available", 0)
        frozen = result.get("frozen", 0)
        total = available + frozen

        text = f"{get_message('balance', lang)}\n"
        text += f"━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Available: {available:,.2f} USDT\n"
        text += f"Frozen: {frozen:,.2f} USDT\n"
        text += f"━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Total: {total:,.2f} USDT"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def orders_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /orders command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_orders()
        orders = result.get("orders", [])

        if not orders:
            await msg.edit_text(get_message("no_orders", lang))
            return

        text = f"{get_message('orders', lang)} ({len(orders)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for order in orders[:10]:  # Limit to 10
            text += f"#{order.get('id')} | {order.get('symbol')}\n"
            text += f"Type: {order.get('type')} {order.get('side')}\n"
            text += f"Price: ${order.get('price'):,.2f}\n"
            text += f"Amount: {order.get('amount')}\n"
            text += f"Status: {order.get('status')}\n\n"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def positions_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /positions command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_positions()
        positions = result.get("positions", [])

        if not positions:
            await msg.edit_text(get_message("no_positions", lang))
            return

        text = f"{get_message('positions', lang)} ({len(positions)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for pos in positions[:10]:  # Limit to 10
            text += f"#{pos.get('id')} | {pos.get('symbol')}\n"
            text += f"Side: {pos.get('side')}\n"
            text += f"Size: {pos.get('size')}\n"
            text += f"Entry: ${pos.get('entry_price'):,.2f}\n"
            text += f"Current: ${pos.get('current_price'):,.2f}\n"
            pnl = pos.get('pnl', 0)
            pnl_emoji = "🟢" if pnl >= 0 else "🔴"
            text += f"P&L: {pnl_emoji} ${pnl:,.2f}\n\n"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def signals_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /signals command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_signals()
        signals = result.get("signals", [])

        if not signals:
            await msg.edit_text(get_message("no_signals", lang))
            return

        text = f"{get_message('signals', lang)} ({len(signals)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for sig in signals[:10]:  # Limit to 10
            text += f"#{sig.get('id')} | {sig.get('symbol')}\n"
            text += f"Type: {sig.get('type')} {sig.get('side')}\n"
            text += f"Price: ${sig.get('price'):,.2f}\n"
            text += f"Status: {sig.get('status')}\n\n"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


@auth_required
async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /status command"""
    lang = context.user_data.get("lang", "vi")

    msg = await update.message.reply_text(get_message("loading", lang))

    try:
        result = await trading_api.get_status()

        text = f"{get_message('status', lang)}\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Bot: {'🟢 Running' if result.get('running') else '🔴 Stopped'}\n"
        text += f"Auto Trading: {'✅ ON' if result.get('auto_trading') else '⏸ OFF'}\n"
        text += f"Last Scan: {result.get('last_scan', 'N/A')}\n"
        text += f"Errors: {result.get('errors', 0)}\n"

        await msg.edit_text(text)
    except Exception as e:
        await msg.edit_text(get_message("error", lang).format(str(e)))


# Callback handlers
async def balance_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle balance button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_balance()
        available = result.get("available", 0)
        frozen = result.get("frozen", 0)
        total = available + frozen

        text = f"{get_message('balance', lang)}\n"
        text += f"━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Available: {available:,.2f} USDT\n"
        text += f"Frozen: {frozen:,.2f} USDT\n"
        text += f"━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Total: {total:,.2f} USDT"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))


async def orders_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle orders button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_orders()
        orders = result.get("orders", [])

        if not orders:
            await query.edit_message_text(get_message("no_orders", lang))
            return

        text = f"{get_message('orders', lang)} ({len(orders)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for order in orders[:5]:  # Limit to 5 for callback
            text += f"#{order.get('id')} | {order.get('symbol')}\n"
            text += f"{order.get('type')} {order.get('side')}\n"
            text += f"${order.get('price'):,.2f}\n\n"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))


async def positions_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle positions button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_positions()
        positions = result.get("positions", [])

        if not positions:
            await query.edit_message_text(get_message("no_positions", lang))
            return

        text = f"{get_message('positions', lang)} ({len(positions)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for pos in positions[:5]:  # Limit to 5
            pnl = pos.get('pnl', 0)
            pnl_emoji = "🟢" if pnl >= 0 else "🔴"
            text += f"{pos.get('symbol')} {pos.get('side')}\n"
            text += f"P&L: {pnl_emoji} ${pnl:,.2f}\n\n"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))


async def signals_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle signals button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_signals()
        signals = result.get("signals", [])

        if not signals:
            await query.edit_message_text(get_message("no_signals", lang))
            return

        text = f"{get_message('signals', lang)} ({len(signals)})\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"

        for sig in signals[:5]:
            text += f"{sig.get('symbol')} {sig.get('side')}\n"
            text += f"${sig.get('price'):,.2f}\n\n"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))


async def status_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle status button callback"""
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "vi")

    await query.edit_message_text(get_message("loading", lang))

    try:
        result = await trading_api.get_status()

        text = f"{get_message('status', lang)}\n"
        text += "━━━━━━━━━━━━━━━━━━━━━\n"
        text += f"Bot: {'🟢 Running' if result.get('running') else '🔴 Stopped'}\n"
        text += f"Auto: {'✅ ON' if result.get('auto_trading') else '⏸ OFF'}\n"
        text += f"Last Scan: {result.get('last_scan', 'N/A')}\n"

        await query.edit_message_text(text)
    except Exception as e:
        await query.edit_message_text(get_message("error", lang).format(str(e)))
