from typing import List

from polymarket_agent.ports.gamma import GammaPort
from polymarket_agent.utils.mock_data import (
    mock_events_data,
    mock_markets_data,
)
from polymarket_agent.utils.types import Market, PolymarketEvent


class GammaMockAdapter(GammaPort):
    def get_all_current_markets(self) -> List[Market]:
        print("MockGamma: Getting all current markets.")
        return mock_markets_data

    def get_all_tradeable_events(self) -> List[PolymarketEvent]:
        print("MockGamma: Getting all tradeable events.")
        return mock_events_data

    def get_market_by_id(self, market_id: str) -> Market:
        print(f"MockGamma: Getting market by ID: {market_id}")
        for market in mock_markets_data:
            if market.id == market_id:
                return market
        raise ValueError(f"Mock market with ID {market_id} not found.")
