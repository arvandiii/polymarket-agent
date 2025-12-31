from typing import List

from agents.ports.search import SearchPort
from agents.utils.types import SearchResult

mock_search_results = [
    SearchResult(content="Web search result about political candidate 1."),
    SearchResult(content="Historical data for similar market events."),
]


class SearchMockAdapter(SearchPort):
    def search_context(self, query: str) -> List[SearchResult]:
        print(f"MockSearch: Searching for query: {query}")
        return mock_search_results
