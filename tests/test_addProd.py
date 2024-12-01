import pytest
from dataclasses import dataclass
from project.micarrito import addProd, Cart, Stores, StorePrices, Brands, addStore
from tests.utils import clear_data



# Sample data setup for testing
@pytest.fixture
def setup_data():
    clear_data()  # Ensure all global lists are empty before each test

    # Add initial stores
    addStore("StoreA")
    addStore("StoreB")

    # Add initial products
    addProd("Apple", "HIGH", 5, "BrandX", 1.2, "StoreA")
    addProd("Apple", "HIGH", 5, "BrandX", 1.0, "StoreB")
    addProd("Banana", "LOW", 10, "BrandY", 0.5, "StoreA")

    return

# Test for empty ProductName
def test_addProd_empty_ProductName(setup_data, capsys):
    addProd("", "HIGH", 5, "BrandX", 1.2, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid Product Name." in captured.out

# Test for empty UrgencyLevel
def test_addProd_empty_UrgencyLevel(setup_data, capsys):
    addProd("Orange", "", 5, "BrandZ", 0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid urgency level." in captured.out

# Test for empty Quantity
def test_addProd_empty_Quantity(setup_data, capsys):
    addProd("Orange", "MEDIUM", "", "BrandZ", 0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid quantity." in captured.out

# Test for empty BrandName
def test_addProd_empty_BrandName(setup_data, capsys):
    addProd("Orange", "MEDIUM", 5, "", 0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid brand." in captured.out

# Test for empty Price
def test_addProd_empty_Price(setup_data, capsys):
    addProd("Orange", "MEDIUM", 5, "BrandZ", "", "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid price." in captured.out

# Test for empty StoreName
def test_addProd_empty_StoreName(setup_data, capsys):
    addProd("Orange", "MEDIUM", 5, "BrandZ", 0.8, "")
    captured = capsys.readouterr()
    assert "Error: Invalid store name." in captured.out

# Test for invalid UrgencyLevel
def test_addProd_invalid_UrgencyLevel(setup_data, capsys):
    addProd("Orange", "URGENT", 5, "BrandZ", 0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid urgency level." in captured.out

# Test for negative Quantity
def test_addProd_negative_Quantity(setup_data, capsys):
    addProd("Orange", "LOW", -5, "BrandZ", 0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid quantity." in captured.out

# Test for negative Price
def test_addProd_negative_Price(setup_data, capsys):
    addProd("Orange", "LOW", 5, "BrandZ", -0.8, "StoreA")
    captured = capsys.readouterr()
    assert "Error: Invalid price." in captured.out

# Test for Store not found
def test_addProd_store_not_found(setup_data, capsys):
    addProd("Orange", "LOW", 5, "BrandZ", 0.8, "StoreC")
    captured = capsys.readouterr()
    assert "Error: Store not found." in captured.out

# Test adding a new product successfully
def test_addProd_success(setup_data):
    addProd("Orange", "MEDIUM", 7, "BrandZ", 0.8, "StoreA")
    assert any(prod.ProductName == "Orange" for prod in Cart)
    assert any(store == "StoreA" for store in Stores)
    assert any(sp.ProductName == "Orange" and sp.StoreName == "StoreA" and sp.Price == 0.8 for sp in StorePrices)
    assert any(brand.ProductName == "Orange" and brand.Brand == "BrandZ" for brand in Brands)

# Test updating an existing product in the cart
def test_addProd_update_existing_product(setup_data):
    addProd("Apple", "MEDIUM", 10, "BrandX", 1.3, "StoreA")
    # Check if the Cart has updated quantity and urgency
    for prod in Cart:
        if prod.ProductName == "Apple":
            assert prod.Quantity == 10
            assert prod.UrgencyLevel == "MEDIUM"
    # Check if the StorePrices have been updated
    for sp in StorePrices:
        if sp.ProductName == "Apple" and sp.StoreName == "StoreA":
            assert sp.Price == 1.3

# Test adding a new store price when store is the same
def test_addProd_update_storeprice_same_store(setup_data):
    addProd("Banana", "LOW", 10, "BrandY", 0.6, "StoreA")
    # Check if the price is updated
    for sp in StorePrices:
        if sp.ProductName == "Banana" and sp.StoreName == "StoreA":
            assert sp.Price == 0.6

# Test adding a new store price when store is different
def test_addProd_add_new_storeprice_different_store(setup_data):
    addProd("Banana", "LOW", 10, "BrandY", 0.55, "StoreB")
    # Check if the new store price is added
    assert any(sp.ProductName == "Banana" and sp.StoreName == "StoreB" and sp.Price == 0.55 for sp in StorePrices)


# Test not adding duplicate brand for an existing product
def test_addProd_no_duplicate_brand(setup_data):
    addProd("Apple", "HIGH", 5, "BrandX", 1.2, "StoreA")
    # Count how many times BrandX for Apple exists
    count = sum(1 for brand in Brands if brand.ProductName == "Apple" and brand.Brand == "BrandX")
    assert count == 1

# Test adding a product to the cart when it's not already there
def test_addProd_add_new_product_to_cart(setup_data):
    addProd("Grapes", "LOW", 15, "BrandZ", 2.0, "StoreA")
    # Check if the product is added to the cart
    assert any(prod.ProductName == "Grapes" for prod in Cart)
    # Check if the store price is added
    assert any(sp.ProductName == "Grapes" and sp.StoreName == "StoreA" and sp.Price == 2.0 for sp in StorePrices)
    # Check if the brand is added
    assert any(brand.ProductName == "Grapes" and brand.Brand == "BrandZ" for brand in Brands)

# Test adding a product with multiple stores and brands
def test_addProd_multiple_stores_brands(setup_data,capsys):
    addProd("Apple", "LOW", 8, "BrandY", 1.5, "StoreC")  # Assuming StoreC is not added yet
    # First, should fail because StoreC does not exist
    captured = capsys.readouterr()
    assert "Error: Store not found." in captured.out

    # Now, add StoreC and try again
    addStore("StoreC")
    addProd("Apple", "LOW", 8, "BrandY", 1.5, "StoreC")
    # Check if the new store price and brand are added
    assert any(sp.ProductName == "Apple" and sp.StoreName == "StoreC" and sp.Price == 1.5 for sp in StorePrices)
    assert any(brand.ProductName == "Apple" and brand.Brand == "BrandY" for brand in Brands)



# 99% because one branch enters always
# Because if that branch is false is going to return before entering