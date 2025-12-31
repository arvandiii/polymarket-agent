from typing import List

from agents.ports.news import NewsPort
from agents.utils.types import Article

mock_news_articles = [
    Article(title="Mock News 1: Event A likely", description="... details ..."),
    Article(title="Mock News 2: Impact on Market Z", description="... details ..."),
]


class NewsMockAdapter(NewsPort):
    def get_articles_by_keywords(self, keywords: List[str]) -> List[Article]:
        print(f"MockNews: Fetching articles for keywords: {keywords}")
        return mock_news_articles
