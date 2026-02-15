"""
Handle Stdin/StdOut
"""

import json
from typing import List

from app_svc.tax_calculation import tax_calculation


def read_simulations_from_stdin() -> List[List[dict]]:
    """Read JSON simulation arrays, one per non-empty line, until EOF."""
    sims = []
    # interactive: accept lines until user submits an empty line
    try:
        while True:
            line = input().strip()
            if not line:  # blank Enter finishes input
                break
            sims.append(json.loads(line))
    except EOFError:
        pass

    return sims


def run_cli() -> None:
    """CLI entry: read all input, process with tax_calculation, print JSON results."""
    simulations = read_simulations_from_stdin()
    for sim in simulations:
        result = tax_calculation(sim)
        print(json.dumps(result))


if __name__ == "__main__":
    print("Running Capital Gains")
    run_cli()
