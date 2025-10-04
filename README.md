# Telegram Trading Bot

Telegram bot để quản lý và điều khiển hệ thống trading.

## Features

- 🔐 Authentication với whitelist user IDs
- 🌐 Bilingual support (VI/EN)
- 📊 Query thông tin: balance, orders, positions, signals
- 🚀 Trading actions: scan Discord, execute signals
- 🎛️ Management: cancel orders, close positions, pause/resume
- 📈 Statistics: P&L, win rate

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment

Copy `.env.example` to `.env` and update:

```bash
cp .env.example .env
```

Edit `.env`:
```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
ALLOWED_USER_IDS=your_telegram_user_id
TRADING_API_URL=http://your-trading-system.com/api
TRADING_API_KEY=your_api_key
DEFAULT_LANGUAGE=vi
```

### 3. Run bot

```bash
python bot/main.py
```

## Commands

### Basic
- `/start` - Welcome & language selection
- `/help` - Command list
- `/lang <vi|en>` - Change language

### Query
- `/balance` - Account balance
- `/orders` - Active orders
- `/positions` - Open positions
- `/signals` - Recent signals
- `/status` - System status

### Trading
- `/scan` - Scan Discord now
- `/execute` - Execute auto signals

### Management
- `/cancel <order_id>` - Cancel order
- `/close <position_id>` - Close position
- `/pause` - Pause auto trading
- `/resume` - Resume auto trading
- `/stats [period]` - P&L statistics

## API Endpoints Required

Your Trading System must expose these endpoints:

### Actions
- `POST /api/scan/now`
- `POST /api/execute/auto`
- `POST /api/orders/cancel/{id}`
- `POST /api/positions/close/{id}`
- `POST /api/system/pause`
- `POST /api/system/resume`

### Queries
- `GET /api/account/balance`
- `GET /api/orders`
- `GET /api/positions`
- `GET /api/signals/recent?limit=10`
- `GET /api/system/status`
- `GET /api/stats?period=today|week|month`

## Project Structure

```
teletrader/
├── bot/
│   ├── handlers/          # Command handlers
│   ├── keyboards/         # Inline keyboards
│   └── middleware/        # Auth, etc.
├── config/
│   ├── settings.py        # Config
│   └── messages.py        # Bilingual messages
├── services/
│   └── trading_api.py     # API client
├── utils/
│   └── decorators.py      # Helpers
├── .env.example           # Config template
├── requirements.txt       # Dependencies
└── README_FEATURE.md      # Feature checklist
```

## Development

See [README_FEATURE.md](README_FEATURE.md) for feature checklist.
