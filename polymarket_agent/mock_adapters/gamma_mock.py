from typing import List

from polymarket_agent.ports.gamma import GammaPort
from polymarket_agent.utils.types import Market, PolymarketEvent

# Define your mock_markets_data and mock_events_data here,
# ensuring they match the structure of Market and PolymarketEvent Pydantic models.
mock_markets_data = [
    Market(
        id="m1",
        question="Will A win?",
        endDate="2025-01-01",
        description="Mock market A.",
        outcomes=["Yes", "No"],
        outcomePrices=["0.6", "0.4"],
        clobTokenIds=["token_A"],
    ),
    Market(
        id="m2",
        question="Will B win?",
        endDate="2025-02-01",
        description="Mock market B.",
        outcomes=["Yes", "No"],
        outcomePrices=["0.3", "0.7"],
        clobTokenIds=["token_B"],
    ),
]
mock_events_data = [
    PolymarketEvent(
        id="e1",
        title="Election 2024",
        description="Big election event.",
        markets=["m1"],
    ),
    PolymarketEvent(
        id="e2",
        title="Tech Conference",
        description="Annual tech event.",
        markets=["m2"],
    ),
]


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
