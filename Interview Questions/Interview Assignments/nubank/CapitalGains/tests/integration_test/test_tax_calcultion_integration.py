import pytest
import json
from pathlib import Path

from app_svc.tax_calculation import tax_calculation

pytestmark = pytest.mark.integration


def load_simulations_from_file() -> list:
    """Load all simulation test cases from data.txt"""
    data_file = Path(__file__).parent.parent.parent / "repos" / "data.txt"

    simulations = []
    with open(data_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                simulations.append(json.loads(line))

    return simulations


# Expected results for each simulation in data.txt
EXPECTED_RESULTS = [
    [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}],
    [{"tax": 0.0}, {"tax": 10000.0}, {"tax": 0.0}],
    [{"tax": 0.0}, {"tax": 0.0}, {"tax": 1000.0}],
    [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}],
    [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 10000.0}],
    [{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}, {"tax": 3000.0}],
    [
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 3000.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 3700.0},
        {"tax": 0.0},
    ],
    [{"tax": 0.0}, {"tax": 80000.0}, {"tax": 0.0}, {"tax": 60000.0}],
    [
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 0.0},
        {"tax": 1000.0},
        {"tax": 2400.0},
    ],
]

SIMULATIONS = load_simulations_from_file()


class TestTaxCalculationIntegration:
    """Integration tests using data from data.txt"""

    @pytest.mark.parametrize(
        "simulation,expected",
        list(zip(SIMULATIONS, EXPECTED_RESULTS)),
        ids=[f"simulation_{i}" for i in range(len(SIMULATIONS))],
    )
    def test_data_txt_simulations_match_expected(self, simulation, expected):
        """
        Test all simulations from data.txt and assert results equal expected outputs.
        """
        result = tax_calculation(simulation)

        # Verify result length matches simulation
        assert len(result) == len(simulation), (
            f"Expected {len(simulation)} results, got {len(result)}"
        )

        # Verify result matches expected output exactly
        assert result == expected, f"Expected: {expected} Got: {result}"
