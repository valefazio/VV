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
