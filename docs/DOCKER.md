# Docker Deployment Guide 🐳

Hướng dẫn chi tiết cách deploy Telegram Trading Bot bằng Docker.

## 📋 Prerequisites

- Docker installed
- Docker Compose installed (optional)
- `.env` file đã config

## 🚀 Quick Start

### 1. Config Environment

```bash
# Copy template
cp .env.example .env

# Edit config
nano .env
```

`.env` cần có:
```env
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...
ALLOWED_USER_IDS=123456789
TRADING_API_URL=http://trading-system:8000/api
TRADING_API_KEY=your_api_key
DEFAULT_LANGUAGE=vi
```

### 2. Run với Docker Compose (Recommended)

```bash
# Start bot
docker-compose up -d

# View logs
docker-compose logs -f telegram-bot

# Stop bot
docker-compose down

# Restart bot
docker-compose restart
```

### 3. Hoặc Run với Docker CLI

```bash
# Build image
docker build -t telegram-trading-bot .

# Run container
docker run -d \
  --name telegram-bot \
  --env-file .env \
  --network trading-network \
  telegram-trading-bot

# View logs
docker logs -f telegram-bot

# Stop
docker stop telegram-bot
docker rm telegram-bot
```

## 🔗 Network Configuration

### Nếu Trading System cũng chạy Docker:

#### Option 1: Shared Network

```bash
# Tạo network
docker network create trading-network

# Bot sẽ tự động join network (xem docker-compose.yml)
# Trading System cũng phải join network này

# Trong .env, dùng container name:
TRADING_API_URL=http://trading-system:8000/api
```

#### Option 2: Host Network

```bash
# Sửa docker-compose.yml:
services:
  telegram-bot:
    network_mode: "host"

# Trong .env:
TRADING_API_URL=http://localhost:8000/api
```

### Nếu Trading System chạy local (không Docker):

```bash
# Linux/Mac - dùng host.docker.internal
TRADING_API_URL=http://host.docker.internal:8000/api

# Hoặc dùng IP thực của máy
TRADING_API_URL=http://192.168.1.100:8000/api
```

## 📦 Docker Commands Cheatsheet

### Build & Run
```bash
# Build image
docker build -t telegram-trading-bot .

# Build with tag
docker build -t telegram-trading-bot:v1.0 .

# Run detached
docker-compose up -d

# Run with build
docker-compose up -d --build
```

### Logs & Debug
```bash
# View logs
docker-compose logs -f

# View logs (specific service)
docker-compose logs -f telegram-bot

# View last 100 lines
docker-compose logs --tail=100 telegram-bot

# Check container status
docker-compose ps
```

### Manage
```bash
# Stop
docker-compose down

# Restart
docker-compose restart

# Update code & restart
docker-compose down
docker-compose up -d --build

# Remove all (including volumes)
docker-compose down -v
```

### Cleanup
```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove all unused data
docker system prune -a
```

## 🔧 Troubleshooting

### Bot không kết nối được Trading System

**Check 1: Network**
```bash
# Vào container
docker exec -it telegram-bot sh

# Test connection
ping trading-system
curl http://trading-system:8000/api/system/status
```

**Check 2: URL config**
```bash
# Verify .env
docker exec telegram-bot env | grep TRADING_API_URL
```

**Fix:**
- Đảm bảo cùng network
- Check URL đúng (hostname/IP)
- Check API key

### Bot restart liên tục

**Check logs:**
```bash
docker-compose logs telegram-bot
```

**Common issues:**
- Sai TELEGRAM_BOT_TOKEN
- API URL không accessible
- Missing dependencies

### Update code

```bash
# Pull new code
git pull

# Rebuild & restart
docker-compose down
docker-compose up -d --build
```

## 📊 Monitoring

### View resource usage
```bash
# Real-time stats
docker stats telegram-bot

# Container info
docker inspect telegram-bot
```

### Health check
```bash
# Check if running
docker ps | grep telegram-bot

# Check logs for errors
docker logs telegram-bot | grep -i error
```

## 🔐 Security Notes

- ✅ `.env` file trong `.gitignore` - không commit
- ✅ `.env` file trong `.dockerignore` - không build vào image
- ✅ Dùng `--env-file` để inject secrets at runtime
- ✅ Chỉ whitelist user IDs cần thiết
- ✅ Rotate API keys thường xuyên

## 📝 Production Deployment

### Docker Compose Production

```yaml
# docker-compose.prod.yml
version: '3.8'

services:
  telegram-bot:
    build: .
    container_name: telegram-trading-bot
    env_file:
      - .env.production
    restart: always  # Auto restart on crash
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"
    networks:
      - trading-network

networks:
  trading-network:
    external: true
```

Run:
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Auto-restart on server reboot

```bash
# Update restart policy
docker update --restart=always telegram-bot
```

## 🔄 CI/CD Example

```bash
# build.sh
#!/bin/bash
git pull
docker-compose down
docker-compose build
docker-compose up -d
docker-compose logs --tail=50 -f
```

Make executable:
```bash
chmod +x build.sh
./build.sh
```

## 📱 Multi-Bot Setup

Nếu muốn chạy nhiều bot instances:

```yaml
# docker-compose.yml
version: '3.8'

services:
  bot-1:
    build: .
    env_file: .env.bot1
    container_name: telegram-bot-1

  bot-2:
    build: .
    env_file: .env.bot2
    container_name: telegram-bot-2
```

## 🆘 Support

Nếu gặp vấn đề:
1. Check logs: `docker-compose logs -f`
2. Check network: `docker network ls`
3. Check containers: `docker ps -a`
4. Rebuild: `docker-compose up -d --build`
