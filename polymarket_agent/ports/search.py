from abc import ABC, abstractmethod
from typing import List

from polymarket_agent.utils.types import SearchResult


class SearchPort(ABC):
    @abstractmethod
    def search_context(self, query: str) -> List[SearchResult]:
        pass
