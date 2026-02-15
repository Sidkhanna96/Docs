"""
Store Classes And Interface Structure
Frozen Classes to Maintain Referrential Transparency
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    action: str
    price: float
    quantity: int


@dataclass(frozen=True)
class Portfolio:
    total_stock_quantity: int
    weighted_average_price: float
    total_loss: float
    tax: float
