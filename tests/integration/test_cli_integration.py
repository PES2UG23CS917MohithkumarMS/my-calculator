"""
Integration Tests - CLI + Calculator Working Together
"""

import subprocess
import sys
import pytest
from click.testing import CliRunner
from src.cli import calculate


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Helper method to run CLI and capture output"""
        runner = CliRunner()
        result = runner.invoke(calculate, list(args))
        return result

    def test_cli_add_integration(self):
        """Test CLI can perform addition"""
        result = self.run_cli("add", "5", "3")
        assert result.exit_code == 0
        assert result.output.strip() == "8"

    def test_cli_subtract_integration(self):
        """Test CLI can perform subtraction"""
        result = self.run_cli("subtract", "5", "3")
        assert result.exit_code == 0
        assert result.output.strip() == "2"

    def test_cli_subtract_missing_operand_error(self):
        """Test CLI handles missing operand for subtraction gracefully"""
        # Call subtract with only one operand; CLI should exit with non-zero and print an error
        result = self.run_cli("subtract", "5")
        assert result.exit_code == 1
        # CLI prints a generic unexpected error message for this case
        assert result.output.strip().startswith("Unexpected error:")

    def test_cli_multiply_integration(self):
        """Test CLI can perform multiplication"""
        result = self.run_cli("multiply", "5", "3")
        assert result.exit_code == 0
        assert result.output.strip().endswith("15")

    def test_cli_divide_integration(self):
        """Test CLI can perform division"""
        result = self.run_cli("divide", "5", "3")
        assert result.exit_code == 0
        assert result.output.strip().endswith("1.67")
