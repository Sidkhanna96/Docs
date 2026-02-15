import pytest

from domain.models import Portfolio, Transaction
from app_svc.tax_calculation import (
    _update_stock_quantity,
    _updateweighted_average_price,
    _apply_transaction,
    tax_calculation,
)

pytestmark = pytest.mark.unit


class TestUpdateStockQuantity:
    """Test stock quantity updates for buy/sell operations"""

    def test_buy_increases_quantity(self):
        result = _update_stock_quantity("buy", 100, 50)
        assert result == 150

    def test_sell_decreases_quantity(self):
        result = _update_stock_quantity("sell", 100, 30)
        assert result == 70

    def test_buy_case_insensitive(self):
        result = _update_stock_quantity("BUY", 100, 50)
        assert result == 150

    def test_sell_case_insensitive(self):
        result = _update_stock_quantity("SELL", 100, 30)
        assert result == 70

    def test_sell_to_zero(self):
        result = _update_stock_quantity("sell", 100, 100)
        assert result == 0

    def test_invalid_action_raises_value_error(self):
        with pytest.raises(ValueError, match="Provided Action is invalid"):
            _update_stock_quantity("invalid_op", 100, 30)


class TestUpdateWeightedAveragePrice:
    """Test weighted average price calculation"""

    def test_buy_updates_weighted_average(self):
        # Start: 10 stocks @ $20
        # Buy: 5 stocks @ $10
        # Expected: (10*20 + 5*10) / (10+5) = 250/15 = 16.67
        result = _updateweighted_average_price("buy", 10, 20.0, 5, 10)
        assert result == 16.67

    def test_sell_keeps_weighted_average(self):
        # Selling does not change weighted average
        result = _updateweighted_average_price("sell", 100, 20.0, 50, 25)
        assert result == 20.0

    def test_first_buy_sets_weighted_average(self):
        # First buy: 0 stocks, buy 10 @ $20
        result = _updateweighted_average_price("buy", 0, 0.0, 10, 20)
        assert result == 20.0

    def test_multiple_buys(self):
        # Buy 10 @ $20 = $200
        # Buy 10 @ $30 = $300
        # Expected: 500 / 20 = $25
        wap = _updateweighted_average_price("buy", 10, 20.0, 10, 30)
        assert wap == 25.0


class TestApplyTransaction:
    """Test applying transactions to portfolio"""

    def test_buy_transaction_updates_quantity_and_wap(self):
        portfolio = Portfolio(0, 0.0, 0.0, 0.0)
        transaction = Transaction("buy", 10.0, 100)

        result = _apply_transaction(portfolio, transaction)

        assert result.total_stock_quantity == 100
        assert result.weighted_average_price == 10.0
        assert result.tax == 0.0

    def test_sell_with_profit_below_exemption_no_tax(self):
        # Buy 100 @ $100 = $10,000
        portfolio = Portfolio(100, 100.0, 0.0, 0.0)
        # Sell 50 @ $150 = $7,500 (below $20,000 threshold)
        transaction = Transaction("sell", 150.0, 50)

        result = _apply_transaction(portfolio, transaction)

        assert result.total_stock_quantity == 50
        assert result.tax == 0.0  # Below exemption threshold

    def test_sell_with_profit_above_exemption_pays_tax(self):
        # Buy 1000 @ $10 = $10,000
        portfolio = Portfolio(1000, 10.0, 0.0, 0.0)
        # Sell 1000 @ $30 = $30,000 (above $20,000 threshold)
        # Capital gain = $30,000 - $10,000 = $20,000
        # Tax = $20,000 * 0.2 = $4,000
        transaction = Transaction("sell", 30.0, 1000)

        result = _apply_transaction(portfolio, transaction)

        assert result.total_stock_quantity == 0
        assert result.tax == 4000.0

    def test_sell_with_loss_no_tax(self):
        # Buy 100 @ $20 = $2,000
        portfolio = Portfolio(100, 20.0, 0.0, 0.0)
        # Sell 100 @ $10 = $1,000 (loss of $1,000)
        transaction = Transaction("sell", 10.0, 100)

        result = _apply_transaction(portfolio, transaction)

        assert result.total_stock_quantity == 0
        assert result.tax == 0.0
        assert result.total_loss == 1000.0  # Loss accumulated

    def test_loss_deducted_from_future_profit(self):
        # Buy 100 @ $20, sell @ $10 (loss $1,000)
        portfolio = Portfolio(100, 20.0, 0.0, 0.0)
        transaction1 = Transaction("sell", 10.0, 100)
        result1 = _apply_transaction(portfolio, transaction1)

        # Buy 1000 @ $20 = $20,000
        portfolio2 = Portfolio(0, 0.0, result1.total_loss, 0.0)
        transaction2 = Transaction("buy", 20.0, 1000)
        result2 = _apply_transaction(portfolio2, transaction2)

        # Sell 1000 @ $30 = $30,000 (profit $10,000)
        # But deduct loss: $10,000 - $1,000 = $9,000 taxable profit
        # Tax = $9,000 * 0.2 = $1,800
        transaction3 = Transaction("sell", 30.0, 1000)
        result3 = _apply_transaction(result2, transaction3)

        assert result3.total_stock_quantity == 0
        assert result3.tax == 1800.0
        assert result3.total_loss == 0.0


class TestTaxCalculation:
    """Integration tests for full tax calculation"""

    def test_simple_buy_sell_with_profit(self):
        simulation = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 20.00, "quantity": 5000},
        ]

        result = tax_calculation(simulation)

        assert len(result) == 2
        assert result[0]["tax"] == 0.0  # Buy has no tax
        assert (
            result[1]["tax"] == 10000.0
        )  # Sell profit: (5000*20 - 5000*10)*0.2 = 50000*0.2

    def test_buy_sell_with_loss(self):
        simulation = [
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},
        ]

        result = tax_calculation(simulation)

        assert len(result) == 2
        assert result[0]["tax"] == 0.0
        assert result[1]["tax"] == 0.0  # Loss, no tax

    def test_multiple_operations_with_loss_carryover(self):
        simulation = [
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {"operation": "sell", "unit-cost": 10.00, "quantity": 5000},  # Loss $50,000
            {"operation": "buy", "unit-cost": 20.00, "quantity": 10000},
            {
                "operation": "sell",
                "unit-cost": 30.00,
                "quantity": 10000,
            },  # Profit $100,000, loss deducted
        ]

        result = tax_calculation(simulation)

        assert len(result) == 4
        assert result[0]["tax"] == 0.0
        assert result[1]["tax"] == 0.0
        assert result[2]["tax"] == 0.0
        assert result[3]["tax"] == 10000.0  # (100,000 - 50,000) * 0.2

    def test_sell_more_than_owned_raises_error(self):
        simulation = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
            {
                "operation": "sell",
                "unit-cost": 20.00,
                "quantity": 200,
            },  # Sell more than owned
        ]

        with pytest.raises(ValueError, match="attempt to sell more shares than owned"):
            tax_calculation(simulation)

    def test_case_insensitive_operations(self):
        simulation = [
            {"operation": "BUY", "unit-cost": 10.00, "quantity": 100},
            {"operation": "SELL", "unit-cost": 20.00, "quantity": 100},
        ]

        result = tax_calculation(simulation)

        assert len(result) == 2
        assert result[1]["tax"] == 0.0

    def test_empty_simulation(self):
        simulation = []
        result = tax_calculation(simulation)
        assert result == []

    def test_only_buy_operations(self):
        simulation = [
            {"operation": "buy", "unit-cost": 10.00, "quantity": 100},
            {"operation": "buy", "unit-cost": 20.00, "quantity": 100},
        ]

        result = tax_calculation(simulation)

        assert len(result) == 2
        assert result[0]["tax"] == 0.0
        assert result[1]["tax"] == 0.0
