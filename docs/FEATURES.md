# Telegram Trading Bot - Features Checklist

## Phase 1: Setup & Core ⚙️
- [x] Project structure & files
- [x] Dependencies (requirements.txt)
- [x] Environment config (.env.example)
- [x] Bot initialization
- [x] API client to Trading System
- [x] Auth middleware (whitelist users)

## Phase 2: Basic Commands 🤖
- [x] `/start` - Welcome message
- [x] `/help` - Command list
- [x] `/balance` - Xem số dư OKX
- [x] `/orders` - Danh sách orders
- [x] `/positions` - Vị thế đang mở

## Phase 3: Trading Actions 📈
- [x] `/scan` - Quét Discord ngay lập tức
- [x] `/execute` - Chạy auto signals
- [x] `/cancel <order_id>` - Hủy order
- [x] `/close <position_id>` - Đóng vị thế

## Phase 4: Management 🎛️
- [x] `/status` - Trạng thái hệ thống
- [x] `/signals` - Signals gần đây
- [x] `/pause` - Tạm dừng auto trading
- [x] `/resume` - Tiếp tục auto trading
- [x] `/stats` - Thống kê P&L

## Phase 5: Polish ✨
- [x] Bilingual support (VI/EN)
- [x] Inline keyboards
- [x] Error handling
- [x] Loading indicators
- [x] Pretty formatting

---

## API Endpoints cần có ở Trading System

### Actions
- `POST /api/scan/now` - Trigger Discord scan
- `POST /api/execute/auto` - Execute auto signals
- `POST /api/orders/cancel/{id}` - Cancel order
- `POST /api/positions/close/{id}` - Close position
- `POST /api/system/pause` - Pause trading
- `POST /api/system/resume` - Resume trading

### Queries
- `GET /api/account/balance` - Account balance
- `GET /api/orders` - List orders
- `GET /api/positions` - List positions
- `GET /api/signals/recent` - Recent signals
- `GET /api/system/status` - System status
- `GET /api/stats?period=today|week|month` - Statistics

---

## Notes
- Chỉ làm command-based, không auto notifications
- Authentication: API key + whitelist Telegram user IDs
- Keep it simple, focus on functionality first
