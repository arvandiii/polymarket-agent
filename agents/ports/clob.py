from abc import ABC, abstractmethod
from typing import Any, Dict

from agents.utils.types import OrderBookSummary


class ClobPort(ABC):
    @abstractmethod
    def get_order_book(self, token_id: str) -> OrderBookSummary:
        pass

    @abstractmethod
    def get_usdc_balance(self) -> float:
        pass

    @abstractmethod
    def execute_market_order(
        self, market_id: str, amount: float, side: str
    ) -> Dict[str, Any]:
        pass
