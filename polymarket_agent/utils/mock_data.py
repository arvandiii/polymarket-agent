from polymarket_agent.utils.types import (
    Article,
    Market,
    OrderBookSummary,
    PolymarketEvent,
    SearchResult,
    TradeRule,
)

# Mock data for GammaAdapter
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

# Mock data for NewsAdapter
mock_news_articles = [
    Article(title="Mock News 1: Event A likely", description="... details ..."),
    Article(title="Mock News 2: Impact on Market Z", description="... details ..."),
]

# Mock data for SearchAdapter
mock_search_results = [
    SearchResult(content="Web search result about political candidate 1."),
    SearchResult(content="Historical data for similar market events."),
]

# Mock data for ClobAdapter
mock_order_book = OrderBookSummary(
    market="mock_market_id",
    asset_id="token_A",
    bids=[{"price": "0.55", "size": "100"}],
    asks=[{"price": "0.60", "size": "100"}],
)

mock_usdc_balance = 1000.0

# Mock data for TradeRules generation
mock_trade_rules = [
    TradeRule(
        market_id="m1",
        predicted_price=0.58,
        action="BUY",
        size_percentage=0.1,
    )
]