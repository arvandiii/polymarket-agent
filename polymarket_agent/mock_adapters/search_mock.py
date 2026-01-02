from typing import List

from polymarket_agent.ports.search import SearchPort
from polymarket_agent.utils.mock_data import mock_search_results
from polymarket_agent.utils.types import SearchResult


class SearchMockAdapter(SearchPort):
    def search_context(self, query: str) -> List[SearchResult]:
        print(f"MockSearch: Searching for query: {query}")
        return mock_search_results
