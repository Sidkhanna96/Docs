from enum import Enum

TAX_RATE = float("0.2")
EXEMPTION_THRESHOLD = float("20000")


class Action(Enum):
    BUY = "buy"
    SELL = "sell"
