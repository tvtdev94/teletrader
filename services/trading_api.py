import httpx
from typing import Dict, Any, Optional
from config.settings import TRADING_API_URL, TRADING_API_KEY


class TradingAPI:
    def __init__(self):
        self.base_url = TRADING_API_URL
        self.headers = {"X-API-Key": TRADING_API_KEY}

    async def _request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make HTTP request to Trading System"""
        async with httpx.AsyncClient(timeout=30.0) as client:
            url = f"{self.base_url}{endpoint}"
            response = await client.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()

    # Actions
    async def scan_now(self) -> Dict[str, Any]:
        """Trigger Discord scan immediately"""
        return await self._request("POST", "/scan/now")

    async def execute_auto(self) -> Dict[str, Any]:
        """Execute all auto signals"""
        return await self._request("POST", "/execute/auto")

    async def execute_signal(self, signal_id: str) -> Dict[str, Any]:
        """Execute specific signal"""
        return await self._request("POST", f"/execute/signal/{signal_id}")

    async def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """Cancel order"""
        return await self._request("POST", f"/orders/cancel/{order_id}")

    async def close_position(self, position_id: str) -> Dict[str, Any]:
        """Close position"""
        return await self._request("POST", f"/positions/close/{position_id}")

    async def pause_trading(self) -> Dict[str, Any]:
        """Pause auto trading"""
        return await self._request("POST", "/system/pause")

    async def resume_trading(self) -> Dict[str, Any]:
        """Resume auto trading"""
        return await self._request("POST", "/system/resume")

    # Queries
    async def get_balance(self) -> Dict[str, Any]:
        """Get account balance"""
        return await self._request("GET", "/account/balance")

    async def get_orders(self) -> Dict[str, Any]:
        """Get active orders"""
        return await self._request("GET", "/orders")

    async def get_positions(self) -> Dict[str, Any]:
        """Get open positions"""
        return await self._request("GET", "/positions")

    async def get_signals(self, limit: int = 10) -> Dict[str, Any]:
        """Get recent signals"""
        return await self._request("GET", f"/signals/recent?limit={limit}")

    async def get_status(self) -> Dict[str, Any]:
        """Get system status"""
        return await self._request("GET", "/system/status")

    async def get_stats(self, period: str = "today") -> Dict[str, Any]:
        """Get P&L statistics"""
        return await self._request("GET", f"/stats?period={period}")


# Global instance
trading_api = TradingAPI()
