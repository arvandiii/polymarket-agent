from abc import ABC, abstractmethod
from typing import List

from agents.utils.types import Article


class NewsPort(ABC):
    @abstractmethod
    def get_articles_by_keywords(self, keywords: List[str]) -> List[Article]:
        pass

    # Add other methods as needed, e.g., get_top_headlines_for_market
