from typing import Any, Dict

from polymarket_agent.ports.clob import ClobPort
from polymarket_agent.utils.mock_data import (
    mock_order_book,
    mock_usdc_balance,
)
from polymarket_agent.utils.types import OrderBookSummary


class ClobMockAdapter(ClobPort):
    def get_order_book(self, token_id: str) -> OrderBookSummary:
        print(f"MockClob: Getting order book for {token_id}")
        return mock_order_book

    def get_usdc_balance(self) -> float:
        print("MockClob: Getting USDC balance.")
        return mock_usdc_balance

    def execute_market_order(
        self, market_id: str, amount: float, side: str
    ) -> Dict[str, Any]:
        print(
            f"MockClob: Executing market order for market {market_id}, amount "
            f"{amount}, side {side}"
        )
        return {"status": "success", "order_id": "mock_order_123"}
