import pytest
from dataclasses import dataclass
from micarrito import (
    Product, PricexStore, Brand, Cart, Stores, StorePrices, Brands,
    addProd, remvProd, editUrg, editQuantity, editPrice, addStore, remvStore,
    findCheapestStore, pricesProd, showUrg
)

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
def test_add_product(setup_data):
    assert len(Cart) == 2
    addProd("Orange", "MEDIUM", 3, "BrandZ", 0.8, "StoreA")
    assert len(Cart) == 3
    assert Cart[2].ProductName == "Orange"
    assert Cart[2].UrgencyLevel == "MEDIUM"

# Test removing a product from the cart
def test_remove_product(setup_data):
    remvProd("Apple")
    assert len(Cart) == 1
    assert Cart[0].ProductName == "Banana"

# Test editing the urgency level of a product
def test_edit_urgency(setup_data):
    editUrg("Apple", "LOW")
    assert Cart[0].UrgencyLevel == "LOW"

# Test editing the quantity of a product
def test_edit_quantity(setup_data):
    editQuantity("Banana", 20)
    assert Cart[1].Quantity == 20

# Test editing the price of a product in a store
def test_edit_price(setup_data):
    editPrice("Apple", "StoreA", 0.9)
    prices = pricesProd("Apple")
    assert any(price[0] == 0.9 for price in prices)

# Test finding the cheapest store for a product
def test_find_cheapest_store(setup_data):
    cheapest_store = findCheapestStore("Apple")
    assert cheapest_store[1] == "StoreB"
    assert cheapest_store[0] == 1.0

# Test adding a store
def test_add_store():
    addStore("StoreC")
    assert "StoreC" in Stores

# Test removing a store
def test_remove_store(setup_data):
    remvStore("StoreA")
    assert "StoreA" not in Stores

# Test showing products by urgency level
def test_show_by_urgency(setup_data, capsys):
    showUrg("HIGH")
    captured = capsys.readouterr()
    assert "Apple" in captured.out
    assert "Banana" not in captured.out
