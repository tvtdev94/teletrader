MESSAGES = {
    "welcome": {
        "vi": "👋 Chào mừng đến Trading Bot!\n\nChọn ngôn ngữ / Select language:",
        "en": "👋 Welcome to Trading Bot!\n\nChọn ngôn ngữ / Select language:"
    },
    "language_selected": {
        "vi": "✅ Đã chọn Tiếng Việt",
        "en": "✅ English selected"
    },
    "help": {
        "vi": """📋 Danh sách lệnh:

🔹 Thông tin
/balance - Xem số dư tài khoản
/orders - Danh sách orders
/positions - Vị thế đang mở
/status - Trạng thái hệ thống
/signals - Signals gần đây

🔹 Trading
/scan - Quét Discord ngay
/execute - Chạy auto signals
/cancel <order_id> - Hủy order
/close <position_id> - Đóng vị thế

🔹 Quản lý
/pause - Tạm dừng auto trading
/resume - Tiếp tục auto trading
/stats - Thống kê P&L

🔹 Khác
/lang <vi|en> - Đổi ngôn ngữ
/help - Hiển thị trợ giúp""",
        "en": """📋 Command list:

🔹 Information
/balance - View account balance
/orders - List orders
/positions - Open positions
/status - System status
/signals - Recent signals

🔹 Trading
/scan - Scan Discord now
/execute - Run auto signals
/cancel <order_id> - Cancel order
/close <position_id> - Close position

🔹 Management
/pause - Pause auto trading
/resume - Resume auto trading
/stats - P&L statistics

🔹 Other
/lang <vi|en> - Change language
/help - Show help"""
    },
    "unauthorized": {
        "vi": "⛔ Bạn không có quyền sử dụng bot này",
        "en": "⛔ You are not authorized to use this bot"
    },
    "error": {
        "vi": "❌ Lỗi: {}",
        "en": "❌ Error: {}"
    },
    "loading": {
        "vi": "⏳ Đang xử lý...",
        "en": "⏳ Processing..."
    },
    "balance": {
        "vi": "💰 Số dư tài khoản",
        "en": "💰 Account Balance"
    },
    "orders": {
        "vi": "📊 Danh sách Orders",
        "en": "📊 Orders List"
    },
    "positions": {
        "vi": "📈 Vị thế đang mở",
        "en": "📈 Open Positions"
    },
    "no_orders": {
        "vi": "Không có orders nào",
        "en": "No orders found"
    },
    "no_positions": {
        "vi": "Không có vị thế nào",
        "en": "No positions found"
    },
    "scan_started": {
        "vi": "🔄 Đang quét Discord...",
        "en": "🔄 Scanning Discord..."
    },
    "scan_success": {
        "vi": "✅ Quét thành công!\nTìm thấy: {} signals",
        "en": "✅ Scan successful!\nFound: {} signals"
    },
    "execute_started": {
        "vi": "🚀 Đang thực thi signals...",
        "en": "🚀 Executing signals..."
    },
    "execute_success": {
        "vi": "✅ Đã tạo {} orders",
        "en": "✅ Created {} orders"
    },
    "cancel_success": {
        "vi": "✅ Đã hủy order #{}",
        "en": "✅ Cancelled order #{}"
    },
    "close_success": {
        "vi": "✅ Đã đóng vị thế #{}",
        "en": "✅ Closed position #{}"
    },
    "pause_success": {
        "vi": "⏸ Đã tạm dừng auto trading",
        "en": "⏸ Auto trading paused"
    },
    "resume_success": {
        "vi": "▶️ Đã tiếp tục auto trading",
        "en": "▶️ Auto trading resumed"
    },
    "status": {
        "vi": "📊 Trạng thái hệ thống",
        "en": "📊 System Status"
    },
    "signals": {
        "vi": "🎯 Signals gần đây",
        "en": "🎯 Recent Signals"
    },
    "no_signals": {
        "vi": "Không có signals nào",
        "en": "No signals found"
    },
    "stats": {
        "vi": "📈 Thống kê P&L",
        "en": "📈 P&L Statistics"
    }
}

def get_message(key: str, lang: str = "vi", **kwargs) -> str:
    """Get message by key and language"""
    msg = MESSAGES.get(key, {}).get(lang, MESSAGES.get(key, {}).get("vi", ""))
    if kwargs:
        return msg.format(**kwargs)
    return msg
