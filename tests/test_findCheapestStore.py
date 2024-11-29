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
    addStore("StoreC")
    addProd("Apple", "HIGH", 5, "BrandX", 1.2, "StoreA")
    addProd("Apple", "HIGH", 5, "BrandX", 1.0, "StoreB")
    addProd("Apple", "HIGH", 5, "BrandX", 1.4, "StoreC")
    addProd("Banana", "LOW", 10, "BrandY", 0.5, "StoreA")
    return




# Test adding a product to the cart
def test_findCheapest(setup_data):
    min = findCheapestStore("Apple")

    assert min[1] == "StoreB"
    assert min[0] == 1.0



# Test adding a product to the cart
def test_findCheapest_noData():
    clear_data()
    min = findCheapestStore("Apple")
    assert min is None



