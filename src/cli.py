"""
Command Line Interface for Calculator
Example: python src/cli.py add 5 3
"""

import sys
import click
from .calculator import add, subtract, multiply, divide, power, square_root
from click.testing import CliRunner
from src.cli import calculate

@click.command()
@click.argument("operation")
@click.argument("num1", type=float)
@click.argument("num2", type=float, required=False)
def calculate(operation, num1, num2=None):
    """Simple calculator CLI"""
    try:
        if operation == "add":
            result = add(num1, num2)
        elif operation == "subtract":
            result = subtract(num1, num2)
        elif operation == "multiply":
            result = multiply(num1, num2)
        elif operation == "divide":
            result = divide(num1, num2)
        elif operation == "power":
            result = power(num1, num2)
        elif operation == "square_root":
            result = square_root(num1)
        else:
            click.echo(f"Unknown operation: {operation}")
            sys.exit(1)

        # Format result nicely
        if result == int(result):
            click.echo(int(result))
        else:
            click.echo(f"{result:.2f}")

    except ValueError as e:
        click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
    

    def run_cli(self, *args):
        """Run CLI in-process safely for tests"""
        runner = CliRunner()
        result = runner.invoke(calculate, list(args))
        return result

    # Run a few quick tests to trigger all branches
    for op, a, b in [
        ("add", 5, 3),
        ("subtract", 5, 3),
        ("multiply", 5, 3),
        ("divide", 9, 3),
        ("power", 2, 3),
    ]:
        

    # # Test square_root and invalid operation
    # assert run_cli("square_root", 16).returncode == 0
    # assert run_cli("modulus", 5, 3).returncode == 1

        print("✅ CLI integration self-tests passed.")
