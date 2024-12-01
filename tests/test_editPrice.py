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


# Test editing the price of a product in a store
def test_editPrice(setup_data):
    editPrice("Apple", "StoreA", 0.9)
    prices = pricesProd("Apple")
    price = "" # string that represent price in the store (in this case "StoreA")
    for el in (prices):
        if el[1] == "StoreA":
            price = el[0]
            break

    assert (price == 0.9)


# Test editing the price with negative price
def test_editPrice_negativePrice(setup_data,capsys):
    editPrice("Banana","StoreA", -1)
    captured = capsys.readouterr()
    assert "Error: Invalid price." in captured.out


# Test editing the price with invalid store
def test_editPrice_invalidStore(setup_data,capsys):
    editPrice("Banana","StoreC",22)
    captured = capsys.readouterr()
    assert "Error: Store not found." in captured.out


# Test editing the price of a non existing product
def test_edit_price_noProduct(setup_data):
    editPrice("Orange", "StoreA", 0.9)
    assert any(storePrice.ProductName == "Orange" for storePrice in StorePrices)