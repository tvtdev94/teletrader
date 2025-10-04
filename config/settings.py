import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_IDS = os.getenv("ALLOWED_USER_IDS", "").split(",")

# Trading System API
TRADING_API_URL = os.getenv("TRADING_API_URL", "http://localhost:8000/api")
TRADING_API_KEY = os.getenv("TRADING_API_KEY")

# Default Language
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "vi")
