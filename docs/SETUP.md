# Setup Guide - Telegram Trading Bot

Hướng dẫn cài đặt chi tiết từ đầu.

## 📋 Prerequisites

- Python 3.11+
- pip
- Telegram account
- Trading System API đang chạy

## 🔧 Setup Steps

### 1. Clone Repository (nếu chưa có)

```bash
git clone <your-repo-url>
cd teletrader
```

### 2. Create Virtual Environment

#### Windows:
```bash
# Tạo venv
python -m venv venv

# Activate venv
venv\Scripts\activate

# Verify
where python
# Should show: <path>\teletrader\venv\Scripts\python.exe
```

#### Linux/Mac:
```bash
# Tạo venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Verify
which python
# Should show: <path>/teletrader/venv/bin/python
```

**Note:** Sau này mỗi lần chạy, cần activate venv trước:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

### 3. Install Dependencies

```bash
# Đảm bảo venv đã activate
pip install --upgrade pip
pip install -r requirements.txt
```

Verify installation:
```bash
pip list
# Should see: python-telegram-bot, httpx, pydantic, python-dotenv
```

### 4. Get Telegram Bot Token

1. Mở Telegram, tìm **@BotFather**
2. Gửi: `/newbot`
3. Đặt tên bot: `My Trading Bot` (hoặc tên khác)
4. Đặt username: `my_trading_bot` (phải unique, kết thúc bằng `bot`)
5. BotFather sẽ cho bạn **TOKEN** (dạng: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

**⚠️ Lưu token này, không share cho ai!**

### 5. Get Your Telegram User ID

1. Mở Telegram, tìm **@userinfobot**
2. Gửi: `/start`
3. Bot sẽ trả về **User ID** của bạn (vd: `123456789`)

**Note:** Chỉ User ID này mới được dùng bot (whitelist).

### 6. Configure Environment

```bash
# Copy template
cp .env.example .env
```

Edit `.env` file:
```env
# Telegram Bot
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
ALLOWED_USER_IDS=123456789

# Trading System API
TRADING_API_URL=http://localhost:8000/api
TRADING_API_KEY=your_api_key_here

# Language
DEFAULT_LANGUAGE=vi
```

**Config notes:**
- `TELEGRAM_BOT_TOKEN`: Token từ BotFather
- `ALLOWED_USER_IDS`: User ID của bạn (có thể nhiều, cách nhau bởi dấu phẩy: `123,456,789`)
- `TRADING_API_URL`: URL của Trading System API
- `TRADING_API_KEY`: API key để xác thực với Trading System
- `DEFAULT_LANGUAGE`: `vi` hoặc `en`

### 7. Verify Trading System API

Đảm bảo Trading System đang chạy và accessible:

```bash
# Test connection
curl http://localhost:8000/api/system/status
```

Nếu thành công, sẽ nhận được JSON response.

### 8. Run Bot

```bash
# Đảm bảo venv đã activate
python bot/main.py
```

Nếu thành công, bạn sẽ thấy:
```
INFO - Starting bot...
```

### 9. Test Bot

1. Mở Telegram
2. Tìm bot của bạn (username đã đặt)
3. Gửi `/start`
4. Bot sẽ chào bạn và hỏi ngôn ngữ!

## 🎯 Common Issues & Solutions

### Issue 1: `python` command not found

**Solution:**
- Windows: Dùng `py` thay vì `python`
- Linux/Mac: Dùng `python3`

### Issue 2: venv activate không work

**Windows PowerShell:**
```powershell
# Nếu bị lỗi execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Sau đó:
venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
venv\Scripts\activate.bat
```

### Issue 3: Import error khi chạy bot

**Solution:**
```bash
# Deactivate venv
deactivate

# Xóa venv cũ
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows

# Tạo lại
python -m venv venv
source venv/bin/activate  # hoặc venv\Scripts\activate
pip install -r requirements.txt
```

### Issue 4: Bot không kết nối được Trading System

**Check:**
1. Trading System có đang chạy không?
   ```bash
   curl http://localhost:8000/api/system/status
   ```
2. URL trong `.env` đúng chưa?
3. API key đúng chưa?
4. Firewall có block không?

**Solution:**
- Check logs của Trading System
- Test API bằng curl/Postman trước
- Verify `.env` config

### Issue 5: Telegram "Unauthorized" error

**Solution:**
- Check `TELEGRAM_BOT_TOKEN` trong `.env`
- Tạo bot mới với BotFather nếu cần
- Đảm bảo không có space/newline trong token

### Issue 6: Bot không trả lời

**Check:**
1. User ID có trong `ALLOWED_USER_IDS` không?
   ```bash
   # Verify
   cat .env | grep ALLOWED_USER_IDS
   ```
2. Check logs xem có error không

**Solution:**
- Thêm User ID vào whitelist
- Restart bot sau khi sửa `.env`

## 📝 Daily Workflow

### Start working:
```bash
# 1. Activate venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 2. Update code (nếu có)
git pull

# 3. Install new dependencies (nếu có)
pip install -r requirements.txt

# 4. Run bot
python bot/main.py
```

### Stop bot:
- Press `Ctrl + C` trong terminal
- Hoặc: `docker-compose down` (nếu dùng Docker)

### Update bot:
```bash
# Stop bot (Ctrl + C)

# Pull new code
git pull

# Install new deps
pip install -r requirements.txt

# Restart bot
python bot/main.py
```

## 🐳 Alternative: Docker Setup

Nếu không muốn setup venv, dùng Docker:

👉 Xem [DOCKER.md](DOCKER.md) để biết thêm chi tiết.

Quick start:
```bash
# 1. Config .env
cp .env.example .env
# Edit .env

# 2. Run
docker-compose up -d

# 3. View logs
docker-compose logs -f
```

## 📚 Next Steps

- [Commands Guide](../README.md#commands) - Danh sách lệnh
- [Features](FEATURES.md) - Feature checklist
- [Docker Guide](DOCKER.md) - Deploy với Docker
- Trading System API docs - API endpoints cần thiết

## 🆘 Need Help?

1. Check bot logs
2. Check Trading System logs
3. Verify `.env` config
4. Test API connection với curl
5. Check [Troubleshooting](DOCKER.md#troubleshooting)
