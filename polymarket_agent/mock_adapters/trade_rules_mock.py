from typing import List

from polymarket_agent.utils.types import (
    Article,
    Market,
    PolymarketEvent,
    SearchResult,
    TradeRule,
)


from polymarket_agent.utils.mock_data import mock_trade_rules


class TradeRulesMockAdapter:
    def generate_trade_rules(
        self,
        markets: List[Market],
        events: List[PolymarketEvent],
        news: List[Article],
        search_results: List[SearchResult],
    ) -> List[TradeRule]:
        print("TradeRulesMock: Generating mock trade rules.")
        return mock_trade_rules
