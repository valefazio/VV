import pytest
from dataclasses import dataclass
from project.micarrito import *  # Import functions from the file where they are defined
from tests.utils import *



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




# Test editing the quantity of a product
def test_edit_quantity_noProduct(setup_data,capsys):
    editQuantity("asas", 20)
    captured = capsys.readouterr()
    assert "Error: Product not found in cart." in captured.out



# Test adding a product to the cart
def test_editQuantity_noData(capsys):
    editQuantity("Banana", -20)
    captured = capsys.readouterr()

    assert "Error: Invalid quantity." in captured.out


