from typing import Dict, List

from pydantic import BaseModel


class Market(BaseModel):
    id: str
    question: str
    endDate: str
    description: str
    outcomes: List[str]
    outcomePrices: List[str]
    clobTokenIds: List[str]


class PolymarketEvent(BaseModel):
    id: str
    title: str
    description: str
    markets: List[str]


class OrderBookSummary(BaseModel):
    market: str
    asset_id: str
    bids: List[Dict[str, str]]
    asks: List[Dict[str, str]]


class Trade(BaseModel):
    price: str
    size: str
    side: str
    market_id: str


class Article(BaseModel):
    title: str
    description: str


class SearchResult(BaseModel):
    content: str


class TradeRule(BaseModel):
    market_id: str
    predicted_price: float
    action: str  # "BUY" or "SELL"
    size_percentage: float
