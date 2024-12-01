import pytest
from dataclasses import dataclass
from project.micarrito import *  # Import functions from the file where they are defined
from tests.utils import *
from unittest.mock import patch




# Sample data setup for testing
@pytest.fixture
def setup_data():
    # Clear global lists before each test
    Cart.clear()
    Stores.clear()
    StorePrices.clear()
    Brands.clear()

    # Add initial stores and products
    addStore("StoreA")
    addStore("StoreB")
    addProd("Apple", "HIGH", 5, "BrandX", 1.2, "StoreA")
    addProd("Apple", "HIGH", 5, "BrandX", 1.0, "StoreB")
    addProd("Banana", "LOW", 10, "BrandY", 0.5, "StoreA")
    return




def test_main_correct_arguments(monkeypatch, capsys):
    test_args = ["micarrito", "commands.txt"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with patch('project.micarrito.process_commands') as mock_process_commands:
        main()
        mock_process_commands.assert_called_once_with("commands.txt")
    
    # Ensure no usage message is printed
    captured = capsys.readouterr()
    assert captured.out == ""

# Test main() with no arguments
def test_main_no_arguments(monkeypatch, capsys):
    test_args = ["micarrito"]  # Only the script name
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with patch('project.micarrito.process_commands') as mock_process_commands:
        main()
        mock_process_commands.assert_not_called()
    
    # Check that usage message is printed
    captured = capsys.readouterr()
    assert "Usage: micarrito <input-file>" in captured.out

# Test main() with too many arguments
def test_main_too_many_arguments(monkeypatch, capsys):
    test_args = ["micarrito", "commands.txt", "extra_arg"]
    monkeypatch.setattr(sys, 'argv', test_args)
    
    with patch('project.micarrito.process_commands') as mock_process_commands:
        main()
        mock_process_commands.assert_not_called()
    
    # Check that usage message is printed
    captured = capsys.readouterr()
    assert "Usage: micarrito <input-file>" in captured.out


import subprocess
import sys
import os
from pathlib import Path

# Assuming your script is named 'micarrito.py' and is located in the 'project' directory
SCRIPT_DIR = Path(__file__).resolve().parent.parent / 'project'
SCRIPT_NAME = 'micarrito.py'

def test_main_execution(tmp_path):
    # Create a temporary command file
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    show
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    # Build the path to the script
    script_path = SCRIPT_DIR / SCRIPT_NAME

    # Ensure the script exists
    assert script_path.exists(), f"Script not found at {script_path}"

    # Run the script as a subprocess with the command file as an argument
    result = subprocess.run(
        [sys.executable, str(script_path), str(command_file)],
        capture_output=True,
        text=True
    )

    # Check that the script executed successfully
    assert result.returncode == 0

    # Capture the output
    output = result.stdout

    # Assertions to verify the output
    assert "Store StoreA correctly added." in output
    assert "Product Apple correctly added to cart." in output
    assert "Apple" in output
    assert "HIGH" in output
    assert "5" in output

