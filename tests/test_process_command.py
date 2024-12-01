import pytest
from dataclasses import dataclass
from project.micarrito import (
    process_commands,
    Cart,
    Stores,
    StorePrices,
    Brands,
    addStore,
    addProd,
    editUrg,
    editQuantity,
    editPrice,
    remvProd,
    remvStore,
    findCheapestStore,
    addBrand,
    show,
    showUrg,
)
from tests.utils import clear_data

# Fixture to clear data before each test
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Code that will run before each test
    clear_data()
    yield
    # Code that will run after each test
    clear_data()

# Helper function to simulate 'show' and 'showUrg' outputs
def mock_show(cart):
    for prod in cart:
        print(f"Product: {prod.ProductName}, Urgency: {prod.UrgencyLevel}, Quantity: {prod.Quantity}")

def mock_showUrg(cart):
    for prod in cart:
        print(f"Product: {prod.ProductName}, Urgency: {prod.UrgencyLevel}")

# Test processing a valid command file
def test_process_commands_valid(tmp_path, capsys):
    # Create a temporary command file
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    show
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    # Process the commands
    process_commands(str(command_file))

    # Capture output
    captured = capsys.readouterr()

    # Assertions
    # Check that the store was added
    assert any(store == "StoreA" for store in Stores)

    # Check that the product was added to the cart
    assert any(prod.ProductName == "Apple" for prod in Cart)

    # Check that the 'show' command output includes 'Apple'
    assert "Apple" in captured.out
    assert "HIGH" in captured.out
    assert "5" in captured.out

# Test processing a file that does not exist
def test_process_commands_file_not_found(capsys):
    # Try to process a non-existent file
    process_commands("nonexistent_file.txt")

    # Capture output
    captured = capsys.readouterr()

    # Assertion
    assert "Error: File 'nonexistent_file.txt' not found." in captured.out


# Test processing a file that does not exist
def test_process_commands_file_not_found(capsys):
    # Try to process a non-existent file
    process_commands("nonexistent_file.txt")

    # Capture output
    captured = capsys.readouterr()

    # Assertion
    assert "Error: File 'nonexistent_file.txt' not found." in captured.out

def test_process_commands_addProd_invalid_argument_types(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple HIGH five BrandX 1.2 StoreA
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # The expected error message includes the line number and exception message
    assert "invalid literal for int() with base 10: 'five'" in captured.out


# Test case to trigger the general Exception
def test_process_commands_general_exception(tmp_path, capsys):
    commands = """
    addStore
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    # This should cause an IndexError when accessing cmd_args[0], which is not handled explicitly
    process_commands(str(command_file))
    captured = capsys.readouterr()

    # The unhandled IndexError should be caught by the general Exception handler
    assert "An error occurred: list index out of range" in captured.out


# Test processing a file with an invalid command
def test_process_commands_invalid_command(tmp_path, capsys):
    commands = """
    invalidCommand
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Invalid command 'invalidCommand'." in captured.out

# Test processing a file with incorrect arguments for 'addProd'
def test_process_commands_incorrect_arguments_addProd(tmp_path, capsys):
    commands = """
    addProd Apple HIGH 5 BrandX 1.2
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Incorrect number of arguments for command 'addProd'." in captured.out

# Test processing a file with incorrect arguments for 'editUrg'
def test_process_commands_editUrg_incorrect_arguments(tmp_path, capsys):
    commands = """
    editUrg Apple
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Adjusted to check for the error message containing the expected prefix
    assert "Error: Incorrect number of arguments for command 'editUrg'." in captured.out

# Test processing a file with incorrect arguments for 'showUrg'
def test_process_commands_showUrg_incorrect_arguments(tmp_path, capsys):
    commands = """
    showUrg HIGH APPLE
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Adjusted to check for the error message containing the expected prefix
    assert "Error: Incorrect number of arguments for command 'showUrg'." in captured.out

# Test processing multiple commands
def test_process_commands_multiple_commands(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    addStore StoreB
    addProd Banana LOW 10 BrandY 0.5 StoreB
    editQuantity Apple 10
    editUrg Banana MEDIUM
    show
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    # Capture output
    captured = capsys.readouterr()

    # Assertions
    # Check that both stores were added
    assert any(store == "StoreA" for store in Stores)
    assert any(store == "StoreB" for store in Stores)

    # Check that both products are in the cart with updated values
    apple = next((prod for prod in Cart if prod.ProductName == "Apple"), None)
    banana = next((prod for prod in Cart if prod.ProductName == "Banana"), None)

    assert apple is not None
    assert apple.Quantity == 10
    assert apple.UrgencyLevel == "HIGH"

    assert banana is not None
    assert banana.UrgencyLevel == "MEDIUM"
    assert banana.Quantity == 10

    # Check that the 'show' command output includes the updated products
    assert "Apple" in captured.out
    assert "10" in captured.out  # Updated quantity
    assert "Banana" in captured.out
    assert "MEDIUM" in captured.out

# Test processing a file with unknown command
def test_process_commands_unknown_command(tmp_path, capsys):
    commands = """
    unknownCommand
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Invalid command 'unknownCommand'." in captured.out

# Test processing 'editQuantity' with invalid quantity
def test_process_commands_editQuantity_invalid_quantity(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    editQuantity Apple ten
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Store StoreA correctly added.\nProduct Apple correctly added to cart.\nError: Invalid quantity for command 'editQuantity'." in captured.out

# Test processing 'editPrice' with incorrect arguments
def test_process_commands_editPrice_incorrect_arguments(tmp_path, capsys):
    commands = """
    editPrice Apple StoreA
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Incorrect number of arguments for command 'editPrice'." in captured.out

# Test processing 'remvProd' for a product not in cart
def test_process_commands_remvProd_product_not_found(tmp_path, capsys):
    commands = """
    remvProd NonexistentProduct
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Product not found in cart." in captured.out

# Test processing 'addBrand' with correct arguments
def test_process_commands_addBrand(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    addBrand Apple BrandY
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    # Check that the new brand is added
    assert any(brand.ProductName == "Apple" and brand.Brand == "BrandY" for brand in Brands)

# Test processing a file with empty lines and comments
def test_process_commands_empty_lines_and_comments(tmp_path, capsys):
    commands = """
    # This is a comment
    addStore StoreA

    # Another comment
    addProd Apple HIGH 5 BrandX 1.2 StoreA

    show
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Check that the 'show' command output includes 'Apple'
    assert "Apple" in captured.out
    assert "StoreA" in captured.out

# Test processing 'addStore' with extra arguments causing TypeError
def test_process_commands_addStore_type_error(tmp_path, capsys):
    commands = """
    addStore StoreA ExtraArg
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Incorrect number of arguments for command 'addStore'." in captured.out

# Test processing 'editPrice' with invalid price
def test_process_commands_editPrice_invalid_price(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    editPrice Apple StoreA invalidPrice
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    assert "Error: Invalid price for command 'editPrice'." in captured.out
    
# Test processing 'findCheapestStore' with product not in any store
def test_process_commands_findCheapestStore_product_not_found(tmp_path, capsys):
    commands = """
    findCheapestStore NonexistentProduct
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Assuming the function prints an error if the product is not found
    assert "Error: Product not found in any store." in captured.out


def test_process_commands_findCheapestStore_incorrect_arguments(tmp_path, capsys):
    commands = """
    findCheapestStore Apple StoreA
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Expecting error message about incorrect number of arguments
    assert "Error: Incorrect number of arguments for command 'findCheapestStore'." in captured.out

def test_process_commands_remvProd_incorrect_arguments(tmp_path, capsys):
    commands = """
    remvProd Apple StoreA
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Expecting error message about incorrect number of arguments
    assert "Error: Incorrect number of arguments for command 'remvProd'." in captured.out

def test_process_commands_remvStore_incorrect_arguments(tmp_path, capsys):
    commands = """
    remvStore StoreA ExtraArg
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Expecting error message about incorrect number of arguments
    assert "Error: Incorrect number of arguments for command 'remvStore'." in captured.out


def test_process_commands_showUrg_correct_arguments(tmp_path, capsys):
    commands = """
    addStore StoreA
    addStore StoreB
    addProd Apple HIGH 5 BrandX 1.2 StoreA
    addProd Banana LOW 5 BrandX 1.0 StoreB
    showUrg Apple
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Check that 'Apple' is shown as HIGH urgency
    assert "Apple" in captured.out

def test_process_commands_editPrice_correct_arguments(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple LOW 5 BrandX 1.2 StoreA
    editPrice Apple StoreA 1.5
    findCheapestStore Apple
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Check that 'Apple' price is updated to 1.5
    assert "StoreA" in captured.out
    assert "1.5" in captured.out


def test_process_commands_editUrg_invalid_urgency_level(tmp_path, capsys):
    commands = """
    addStore StoreA
    addProd Apple LOW 5 BrandX 1.2 StoreA
    editUrg Apple URGENT
    show
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Assuming `editUrg` function prints "Error: Invalid urgency level."
    assert "Error: Invalid urgency level." in captured.out

    # Ensure that 'Apple' urgency remains unchanged
    assert "LOW" in captured.out
    assert "URGENT" not in captured.out


def test_process_commands_addBrand_incorrect_arguments(tmp_path, capsys):
    commands = """
    addBrand Apple BrandX ExtraArg
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    # Expecting error message about incorrect number of arguments
    assert "Error: Incorrect number of arguments for command 'addBrand'." in captured.out


# Test processing a file with multiple errors
def test_process_commands_multiple_errors(tmp_path, capsys):
    commands = """
    addProd
    editQuantity
    unknownCommand
    """
    command_file = tmp_path / "commands.txt"
    command_file.write_text(commands.strip())

    process_commands(str(command_file))

    captured = capsys.readouterr()

    errors = captured.out.strip().split('\n')
    assert len(errors) == 3
    assert "Error: Incorrect number of arguments for command 'addProd'." in errors[0]
    assert "Error: Incorrect number of arguments for command 'editQuantity'." in errors[1]
    assert "Error: Invalid command 'unknownCommand'." in errors[2]


