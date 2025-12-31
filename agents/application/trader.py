from typing import List

from agents.ports.clob import ClobPort
from agents.utils.types import TradeRule


class Trader:
    def __init__(self, clob_adapter: ClobPort):
        self.clob_adapter = clob_adapter

    def execute_trade_rules(self, rules: List[TradeRule]):
        for rule in rules:
            print(f"Trader: Attempting to execute rule: {rule}")
            # For simplicity, let's assume market_id is clob_token_id for mock
            market_id = rule.market_id  # You might need to map this to clob_token_id
            amount_to_trade = (
                self.clob_adapter.get_usdc_balance() * rule.size_percentage
            )
            response = self.clob_adapter.execute_market_order(
                market_id, amount_to_trade, rule.action
            )
            print(f"Trade execution response: {response}")
