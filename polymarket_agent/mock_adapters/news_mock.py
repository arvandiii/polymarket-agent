from typing import List

from polymarket_agent.ports.news import NewsPort
from polymarket_agent.utils.mock_data import mock_news_articles
from polymarket_agent.utils.types import Article


class NewsMockAdapter(NewsPort):
    def get_articles_by_keywords(self, keywords: List[str]) -> List[Article]:
        print(f"MockNews: Fetching articles for keywords: {keywords}")
        return mock_news_articles
