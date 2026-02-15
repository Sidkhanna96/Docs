"""
Tax Calculation Business Logic Layer for Stock Simulations
"""

from typing import List, Dict, Any

from domain.models import Portfolio, Transaction
from utils.constants import EXEMPTION_THRESHOLD, TAX_RATE, Action


def _update_stock_quantity(action: str, total_quantity: int, quantity: int) -> int:
    """
    Update stock quantity based on buy or sell action.

    Args:
        action (str): Type of operation - 'buy' or 'sell' (case-insensitive)
        total_quantity (int): Current total stock quantity owned
        quantity (int): Number of stocks to buy or sell

    Returns:
        int: Updated total stock quantity after the operation

    Raises:
        ValueError: If action is not 'buy' or 'sell'
    """
    if action.lower() == Action.BUY.value:
        return total_quantity + quantity
    if action.lower() == Action.SELL.value:
        return total_quantity - quantity
    else:
        raise ValueError("Provided Action is invalid")


def _updateweighted_average_price(
    action: str,
    total_stock_quantity: int,
    current_weighted_average_price: float,
    new_quantity: int,
    new_price: int,
):
    """
    Calculate the mean buy price for the total number of stocks when the operation is a buy

    Only updates on buy operations. Weighted average is used to calculate
    capital gains/losses when selling.

    Args:
        action (str): Type of operation - 'buy' or 'sell' (case-insensitive)
        total_stock_quantity (int): Current number of stocks owned
        current_weighted_average_price (float): Current weighted average price per stock
        new_quantity (int): Number of stocks being bought/sold
        new_price (float): Price per stock for this operation

    Returns:
        float: Updated weighted average price (unchanged if action is 'sell')
    """
    if action.lower() != Action.BUY.value:
        return current_weighted_average_price

    return round(
        (
            (total_stock_quantity * current_weighted_average_price)
            + (new_quantity * new_price)
        )
        / (total_stock_quantity + new_quantity),
        2,
    )


def _apply_transaction(portfolio: Portfolio, transaction: Transaction) -> Portfolio:
    """
    For each operation in a simulation update the portfolio performance

    Handles:
    - Stock quantity and weighted average price updates
    - Capital gains/losses calculation
    - Tax calculation based on profit and exemption threshold
    - Loss carryover for future tax deductions

    Args:
        portfolio (Portfolio): Current portfolio state
        transaction (Transaction): Buy or sell transaction to apply

    Returns:
        Portfolio: New portfolio state after transaction (immutable - returns new instance)
    """
    new_weighted_average = _updateweighted_average_price(
        transaction.action,
        portfolio.total_stock_quantity,
        portfolio.weighted_average_price,
        transaction.quantity,
        transaction.price,
    )

    try:
        new_stock_quantity = _update_stock_quantity(
            transaction.action,
            portfolio.total_stock_quantity,
            transaction.quantity,
        )
    except ValueError:
        print(f"Invalid action type provided {transaction.action}")

    tax = 0.0
    total_loss = portfolio.total_loss
    if transaction.action == Action.SELL.value:
        operationCost = transaction.quantity * transaction.price
        capital_gain = (
            operationCost - transaction.quantity * portfolio.weighted_average_price
        )

        if capital_gain < 0:
            total_loss += -capital_gain
        else:
            if operationCost > EXEMPTION_THRESHOLD:
                profit_after_deduction = max(0, capital_gain - portfolio.total_loss)
                total_loss = max(portfolio.total_loss - capital_gain, 0)
                tax = profit_after_deduction * TAX_RATE

    return Portfolio(
        total_stock_quantity=new_stock_quantity,
        weighted_average_price=new_weighted_average,
        total_loss=total_loss,
        tax=tax,
    )


def tax_calculation(simulation: List[Dict[str, Any]]) -> List[Dict[str, float]]:
    """
    Calculate Taxes for each Simulation (Each Simulation contains stream of operations)

    Processes a sequence of buy/sell operations in order and returns
    the tax owed for each operation.

    Args:
        simulation (List[Dict[str, Any]]): List of operations, each containing:
            - operation (str): 'buy' or 'sell'
            - unit-cost (float): Price per stock (two decimal places)
            - quantity (int): Number of stocks

    Returns:
        List[Dict[str, float]]: List of tax results, one per operation:
            - Each element: {"tax": amount_owed}
    """
    operation_history = []
    portfolio_performance = Portfolio(0, 0.0, 0.0, 0.0)

    for operation in simulation:
        action, price, quantity = (
            operation["operation"].lower(),
            float(operation["unit-cost"]),
            operation["quantity"],
        )

        transaction = Transaction(action, price, quantity)

        if (
            transaction.action == Action.SELL.value
            and transaction.quantity > portfolio_performance.total_stock_quantity
        ):
            raise ValueError("attempt to sell more shares than owned.")

        portfolio_performance = _apply_transaction(portfolio_performance, transaction)

        operation_history.append(
            {
                "transaction": {
                    "action": transaction.action,
                    "price": transaction.price,
                    "quantity": transaction.quantity,
                },
                "portfolio": {
                    "total_stock_quantity": portfolio_performance.total_stock_quantity,
                    "weighted_average_price": portfolio_performance.weighted_average_price,
                    "total_loss": portfolio_performance.total_loss,
                    "tax": portfolio_performance.tax,
                },
            },
        )

    response = []
    for history in operation_history:
        response.append({"tax": history["portfolio"]["tax"]})

    return response
