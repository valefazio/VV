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
    addProd("Orange", "LOW", 10, "BrandY", 0.5, "StoreB")
    return


# Test removing a store to get full branch cov
def test_remove_store():
    remvProd("Apple")
    remvProd("Orange")
    remvStore("StoreB")
    assert "StoreB" not in Stores


# Test removing a store which is no present
def test_remove_store_notPresent(capsys):
    remvStore("StoreC")
    captured = capsys.readouterr()
    assert "Error: Store not found." in captured.out



# Test removing a store with proct
def test_remove_store_withProducts(setup_data,capsys):
    remvStore("StoreA")
    captured = capsys.readouterr()
    assert "Error: Store has products in cart." in captured.out    

