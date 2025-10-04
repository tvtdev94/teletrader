import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
from config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers.start import (
    start_command,
    help_command,
    lang_command,
    language_callback,
)
from bot.handlers.trading import (
    scan_command,
    execute_command,
    scan_callback,
    execute_callback,
)
from bot.handlers.query import (
    balance_command,
    orders_command,
    positions_command,
    signals_command,
    status_command,
    balance_callback,
    orders_callback,
    positions_callback,
    signals_callback,
    status_callback,
)
from bot.handlers.management import (
    cancel_command,
    close_command,
    pause_command,
    resume_command,
)
from bot.handlers.stats import (
    stats_command,
    stats_callback,
)

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("lang", lang_command))

    # Trading commands
    application.add_handler(CommandHandler("scan", scan_command))
    application.add_handler(CommandHandler("execute", execute_command))

    # Query commands
    application.add_handler(CommandHandler("balance", balance_command))
    application.add_handler(CommandHandler("orders", orders_command))
    application.add_handler(CommandHandler("positions", positions_command))
    application.add_handler(CommandHandler("signals", signals_command))
    application.add_handler(CommandHandler("status", status_command))

    # Management commands
    application.add_handler(CommandHandler("cancel", cancel_command))
    application.add_handler(CommandHandler("close", close_command))
    application.add_handler(CommandHandler("pause", pause_command))
    application.add_handler(CommandHandler("resume", resume_command))

    # Stats commands
    application.add_handler(CommandHandler("stats", stats_command))

    # Callback query handlers
    application.add_handler(CallbackQueryHandler(language_callback, pattern="^lang_"))
    application.add_handler(CallbackQueryHandler(balance_callback, pattern="^balance$"))
    application.add_handler(CallbackQueryHandler(orders_callback, pattern="^orders$"))
    application.add_handler(CallbackQueryHandler(positions_callback, pattern="^positions$"))
    application.add_handler(CallbackQueryHandler(signals_callback, pattern="^signals$"))
    application.add_handler(CallbackQueryHandler(status_callback, pattern="^status$"))
    application.add_handler(CallbackQueryHandler(scan_callback, pattern="^scan$"))
    application.add_handler(CallbackQueryHandler(execute_callback, pattern="^execute$"))
    application.add_handler(CallbackQueryHandler(stats_callback, pattern="^stats$"))

    # Start bot
    logger.info("Starting bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
