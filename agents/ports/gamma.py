from abc import ABC, abstractmethod
from typing import List

from agents.utils.types import Market, PolymarketEvent


class GammaPort(ABC):
    @abstractmethod
    def get_all_current_markets(self) -> List[Market]:
        pass

    @abstractmethod
    def get_all_tradeable_events(self) -> List[PolymarketEvent]:
        pass

    @abstractmethod
    def get_market_by_id(self, market_id: str) -> Market:
        pass

    # Add other methods as needed from GammaMarketClient
