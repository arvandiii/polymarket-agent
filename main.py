from polymarket_agent.adapters.clob_mock import ClobMockAdapter
from polymarket_agent.adapters.gamma_mock import GammaMockAdapter
from polymarket_agent.adapters.news_mock import NewsMockAdapter
from polymarket_agent.adapters.search_mock import SearchMockAdapter
from polymarket_agent.application.orchestrator import Orchestrator
from polymarket_agent.application.trader import Trader

if __name__ == "__main__":
    print("Starting mocked application...")

    # Initialize mock adapters
    news_mock = NewsMockAdapter()
    search_mock = SearchMockAdapter()
    gamma_mock = GammaMockAdapter()
    clob_mock = ClobMockAdapter()

    # Initialize orchestrator and trader with mock adapters
    orchestrator = Orchestrator(
        news_adapter=news_mock, search_adapter=search_mock, gamma_adapter=gamma_mock
    )
    trader = Trader(clob_adapter=clob_mock)

    # Application flow using mock data
    print("\n--- Gathering Data ---")
    markets, events, news_articles, search_results = orchestrator.gather_all_data()
    print(f"Markets collected: {len(markets)}")
    print(f"Events collected: {len(events)}")
    print(f"News articles collected: {len(news_articles)}")
    print(f"Search results collected: {len(search_results)}")

    print("\n--- Generating Trade Rules ---")
    trade_rules = orchestrator.generate_trading_rules()
    print(f"Generated {len(trade_rules)} trade rules:")
    for rule in trade_rules:
        print(f"- {rule}")

    print("\n--- Executing Trade Rules ---")
    trader.execute_trade_rules(trade_rules)

    print("Mocked application finished.")
