# Telegram Trading Bot

Telegram bot để quản lý và điều khiển hệ thống trading.

## ✨ Features

- 🔐 Authentication với whitelist user IDs
- 🌐 Bilingual support (VI/EN)
- 📊 Query thông tin: balance, orders, positions, signals
- 🚀 Trading actions: scan Discord, execute signals
- 🎛️ Management: cancel orders, close positions, pause/resume
- 📈 Statistics: P&L, win rate

## 🚀 Quick Start

### Option 1: Python (Recommended for Development)

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Edit .env with your credentials

# 4. Run
python bot/main.py
```

📖 **Chi tiết:** [docs/SETUP.md](docs/SETUP.md)

### Option 2: Docker (Recommended for Production)

```bash
# 1. Configure
cp .env.example .env
# Edit .env

# 2. Run
docker-compose up -d

# 3. View logs
docker-compose logs -f
```

🐳 **Chi tiết:** [docs/DOCKER.md](docs/DOCKER.md)

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

## 📂 Project Structure

```
teletrader/
├── bot/
│   ├── handlers/          # Command handlers
│   ├── keyboards/         # Inline keyboards
│   ├── middleware/        # Auth, etc.
│   └── main.py           # Entry point
├── config/
│   ├── settings.py        # Config loader
│   └── messages.py        # Bilingual messages
├── services/
│   └── trading_api.py     # API client
├── utils/
│   └── decorators.py      # Helpers
├── docs/
│   ├── SETUP.md          # Setup guide (venv, etc.)
│   ├── DOCKER.md         # Docker guide
│   └── FEATURES.md       # Feature checklist
├── .env.example          # Config template
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker image
└── docker-compose.yml    # Docker Compose
```

## 📚 Documentation

- **[Setup Guide](docs/SETUP.md)** - Hướng dẫn cài đặt chi tiết (venv, Telegram bot setup, troubleshooting)
- **[Docker Guide](docs/DOCKER.md)** - Deploy với Docker, network config, production setup
- **[Features](docs/FEATURES.md)** - Feature checklist và development progress

## 🛠️ Development

1. Fork/clone repo
2. Setup theo [docs/SETUP.md](docs/SETUP.md)
3. Check [docs/FEATURES.md](docs/FEATURES.md) để biết features đã implement
4. Tạo Pull Request

## 📝 Notes

- Bot chỉ response khi nhận command (không có auto notifications)
- Cần Trading System API đang chạy để bot hoạt động
- Chỉ whitelist user IDs mới được dùng bot
