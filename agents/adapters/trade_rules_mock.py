from typing import List

from agents.utils.types import Article, Market, PolymarketEvent, SearchResult, TradeRule


class TradeRulesMockAdapter:
    def generate_trade_rules(
        self,
        markets: List[Market],
        events: List[PolymarketEvent],
        news: List[Article],
        search_results: List[SearchResult],
    ) -> List[TradeRule]:
        print("TradeRulesMock: Generating mock trade rules.")
        # Based on the static mock data, generate some predefined rules
        if markets and events:
            # Example: Always buy market "m1" if it exists
            return [
                TradeRule(
                    market_id="m1",
                    predicted_price=0.58,
                    action="BUY",
                    size_percentage=0.1,
                )
            ]
        return []
