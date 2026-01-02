from typing import List

from polymarket_agent.mock_adapters.trade_rules_mock import TradeRulesMockAdapter
from polymarket_agent.ports.gamma import GammaPort
from polymarket_agent.ports.news import NewsPort
from polymarket_agent.ports.search import SearchPort
from polymarket_agent.utils.types import (
    Article,
    Market,
    PolymarketEvent,
    SearchResult,
    TradeRule,
)


class Orchestrator:
    def __init__(
        self,
        news_adapter: NewsPort,
        search_adapter: SearchPort,
        gamma_adapter: GammaPort,
    ):
        self.news_adapter = news_adapter
        self.search_adapter = search_adapter
        self.gamma_adapter = gamma_adapter
        self.trade_rules_generator = (
            TradeRulesMockAdapter()
        )  # Using the mock generator for now

    def gather_all_data(
        self,
    ) -> tuple[List[Market], List[PolymarketEvent], List[Article], List[SearchResult]]:
        markets = self.gamma_adapter.get_all_current_markets()
        events = self.gamma_adapter.get_all_tradeable_events()
        news = self.news_adapter.get_articles_by_keywords(["general", "market"])
        search_results = self.search_adapter.search_context("current market conditions")
        return markets, events, news, search_results

    def generate_trading_rules(self) -> List[TradeRule]:
        markets, events, news, search_results = self.gather_all_data()
        return self.trade_rules_generator.generate_trade_rules(
            markets, events, news, search_results
        )
