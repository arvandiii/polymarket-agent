from typing import Any, Dict

from polymarket_agent.ports.clob import ClobPort
from polymarket_agent.utils.types import OrderBookSummary

mock_order_book = OrderBookSummary(
    market="mock_market_id",
    asset_id="token_A",
    bids=[{"price": "0.55", "size": "100"}],
    asks=[{"price": "0.60", "size": "100"}],
)

mock_usdc_balance = 1000.0


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
