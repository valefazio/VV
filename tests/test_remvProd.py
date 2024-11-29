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




# Test adding a product to the cart
def test_show_noCart():
    clear_data()
    findCheapestStore("APPLE")
    assert len(Cart) == 0


# Test adding a product to the cart
def test_show(setup_data):
    findCheapestStore("APPLE")
    assert cheapest_store[1] == "StoreB"
    assert cheapest_store[0] == 1.0



