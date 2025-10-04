from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def language_keyboard():
    """Language selection keyboard"""
    keyboard = [
        [
            InlineKeyboardButton("🇻🇳 Tiếng Việt", callback_data="lang_vi"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def main_menu_keyboard(lang="vi"):
    """Main menu keyboard"""
    if lang == "vi":
        keyboard = [
            [
                InlineKeyboardButton("💰 Số dư", callback_data="balance"),
                InlineKeyboardButton("📊 Orders", callback_data="orders")
            ],
            [
                InlineKeyboardButton("📈 Positions", callback_data="positions"),
                InlineKeyboardButton("🎯 Signals", callback_data="signals")
            ],
            [
                InlineKeyboardButton("🔄 Quét Discord", callback_data="scan"),
                InlineKeyboardButton("🚀 Execute", callback_data="execute")
            ],
            [
                InlineKeyboardButton("📊 Trạng thái", callback_data="status"),
                InlineKeyboardButton("📈 Thống kê", callback_data="stats")
            ]
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("💰 Balance", callback_data="balance"),
                InlineKeyboardButton("📊 Orders", callback_data="orders")
            ],
            [
                InlineKeyboardButton("📈 Positions", callback_data="positions"),
                InlineKeyboardButton("🎯 Signals", callback_data="signals")
            ],
            [
                InlineKeyboardButton("🔄 Scan Discord", callback_data="scan"),
                InlineKeyboardButton("🚀 Execute", callback_data="execute")
            ],
            [
                InlineKeyboardButton("📊 Status", callback_data="status"),
                InlineKeyboardButton("📈 Stats", callback_data="stats")
            ]
        ]
    return InlineKeyboardMarkup(keyboard)
