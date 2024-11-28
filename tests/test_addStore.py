import pytest
from dataclasses import dataclass
from project.micarrito import *  # Import functions from the file where they are defined
from tests.utils import *
from io import StringIO

"""
# Test empty ProductName
def test_add_product_empty_product_name():
    clear_data()
    addStore("StoreA")
    addProd("", "MEDIUM", 3, "BrandZ", 0.8, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test empty UrgencyLevel
def test_add_product_empty_urgency_level():
    clear_data()
    addStore("StoreA")
    addProd("Apple", "", 5, "BrandY", 1.2, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test empty Quantity
def test_add_product_empty_quantity():
    clear_data()
    addStore("StoreA")
    addProd("Banana", "LOW", "", "BrandX", 0.5, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test empty BrandName
def test_add_product_empty_brand_name():
    clear_data()
    addStore("StoreA")
    addProd("Grapes", "HIGH", 10, "", 2.5, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test empty Price
def test_add_product_empty_price():
    clear_data()
    addStore("StoreA")
    addProd("Mango", "MEDIUM", 4, "BrandW", "", "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test empty StoreName
def test_add_product_empty_store_name():
    clear_data()
    addStore("StoreA")
    addProd("Peach", "LOW", 2, "BrandV", 1.5, "")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test invalid UrgencyLevel
@pytest.mark.parametrize("invalid_urgency", ["URGENT", "NORMAL", ""])
def test_add_product_invalid_urgency_level(invalid_urgency):
    clear_data()
    addStore("StoreA")
    addProd("Cherry", invalid_urgency, 5, "BrandU", 3.0, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test negative Quantity
def test_add_product_negative_quantity():
    clear_data()
    addStore("StoreA")
    addProd("Strawberry", "HIGH", -1, "BrandT", 2.0, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test negative Price
def test_add_product_negative_price():
    clear_data()
    addStore("StoreA")
    addProd("Blueberry", "MEDIUM", 3, "BrandS", -0.5, "StoreA")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test Store not found
def test_add_product_store_not_found():
    clear_data()
    addStore("StoreA")
    addProd("Pineapple", "LOW", 2, "BrandR", 4.0, "StoreB")
    assert len(Cart) == 0
    assert len(StorePrices) == 0
    assert len(Brands) == 0

# Test adding a product that already exists in the cart
def test_add_existing_product_in_cart():
    clear_data()
    addStore("StoreA")
    addProd("Apple", "LOW", 2, "BrandY", 1.0, "StoreA")
    addProd("Apple", "HIGH", 5, "BrandY", 1.2, "StoreA")
    assert len(Cart) == 1
    assert Cart[0].ProductName == "Apple"
    assert Cart[0].UrgencyLevel == "HIGH"
    assert Cart[0].Quantity == 5
    assert len(StorePrices) == 1
    assert StorePrices[0].Price == 1.2
    assert len(Brands) == 1  # Brand should not duplicate

# Test updating StorePrices when store exists
def test_update_store_prices_existing_store():
    clear_data()
    addStore("StoreA")
    addProd("Banana", "MEDIUM", 3, "BrandX", 0.5, "StoreA")
    addProd("Banana", "MEDIUM", 3, "BrandX", 0.6, "StoreA")
    assert len(StorePrices) == 1
    assert StorePrices[0].Price == 0.6

# Test updating StorePrices when adding a new store for the same product
def test_update_store_prices_new_store():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addProd("Cherry", "HIGH", 10, "BrandU", 3.0, "StoreA")
    addProd("Cherry", "HIGH", 10, "BrandU", 3.5, "StoreB")
    assert len(StorePrices) == 2
    assert any(sp.StoreName == "StoreA" and sp.Price == 3.0 for sp in StorePrices)
    assert any(sp.StoreName == "StoreB" and sp.Price == 3.5 for sp in StorePrices)

# Test updating Brands when adding a new brand for the same product
def test_update_brands_new_brand():
    clear_data()
    addStore("StoreA")
    addProd("Grapes", "LOW", 4, "BrandV", 2.5, "StoreA")
    addProd("Grapes", "LOW", 4, "BrandW", 2.5, "StoreA")
    assert len(Brands) == 2
    assert any(b.Brand == "BrandV" for b in Brands)
    assert any(b.Brand == "BrandW" for b in Brands)

# Test Brands are not duplicated when adding the same brand again
def test_update_brands_existing_brand():
    clear_data()
    addStore("StoreA")
    addProd("Mango", "HIGH", 5, "BrandW", 1.5, "StoreA")
    addProd("Mango", "HIGH", 5, "BrandW", 1.5, "StoreA")
    assert len(Brands) == 1

# Test adding multiple products
def test_add_multiple_products():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addProd("Apple", "LOW", 2, "BrandY", 1.0, "StoreA")
    addProd("Banana", "MEDIUM", 5, "BrandX", 0.5, "StoreA")
    addProd("Cherry", "HIGH", 10, "BrandU", 3.0, "StoreB")
    assert len(Cart) == 3
    assert len(StorePrices) == 3
    assert len(Brands) == 3

# Test adding a product with multiple brands
def test_add_product_multiple_brands():
    clear_data()
    addStore("StoreA")
    addProd("Peach", "MEDIUM", 3, "BrandV", 1.5, "StoreA")
    addProd("Peach", "MEDIUM", 3, "BrandW", 1.5, "StoreA")
    addProd("Peach", "MEDIUM", 3, "BrandV", 1.5, "StoreA")  # Duplicate brand
    assert len(Brands) == 2  # Should only have two unique brands

# Test adding a product with multiple stores and brands
def test_add_product_multiple_stores_brands():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addProd("Orange", "HIGH", 4, "BrandZ", 0.8, "StoreA")
    addProd("Orange", "HIGH", 4, "BrandY", 0.9, "StoreB")
    assert len(Cart) == 1
    assert Cart[0].ProductName == "Orange"
    assert Cart[0].UrgencyLevel == "HIGH"
    assert Cart[0].Quantity == 4
    assert len(StorePrices) == 2
    assert len(Brands) == 2

# Test adding a product with zero quantity and price
def test_add_product_zero_quantity_price():
    clear_data()
    addStore("StoreA")
    addProd("Kiwi", "LOW", 0, "BrandQ", 0.0, "StoreA")
    assert len(Cart) == 1
    assert Cart[0].Quantity == 0
    assert len(StorePrices) == 1
    assert StorePrices[0].Price == 0.0
    assert len(Brands) == 1

# Test adding a product with different urgency levels
def test_add_product_different_urgency_levels():
    clear_data()
    addStore("StoreA")
    addProd("Lemon", "LOW", 1, "BrandP", 0.3, "StoreA")
    addProd("Lemon", "MEDIUM", 2, "BrandP", 0.35, "StoreA")
    addProd("Lemon", "HIGH", 3, "BrandP", 0.4, "StoreA")
    assert len(Cart) == 1
    assert Cart[0].UrgencyLevel == "HIGH"
    assert Cart[0].Quantity == 3
    assert len(StorePrices) == 1
    assert StorePrices[0].Price == 0.4
    assert len(Brands) == 1

# Test adding a product with different brands and stores
def test_add_product_different_brands_stores():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addStore("StoreC")
    addProd("Papaya", "MEDIUM", 2, "BrandO", 1.8, "StoreA")
    addProd("Papaya", "MEDIUM", 2, "BrandN", 1.9, "StoreB")
    addProd("Papaya", "MEDIUM", 2, "BrandO", 2.0, "StoreC")
    assert len(Cart) == 1
    assert len(StorePrices) == 3
    assert len(Brands) == 2

# Test adding a product with existing store but different price
def test_add_product_existing_store_different_price():
    clear_data()
    addStore("StoreA")
    addProd("Watermelon", "LOW", 1, "BrandM", 3.0, "StoreA")
    addProd("Watermelon", "LOW", 1, "BrandM", 3.5, "StoreA")
    assert len(StorePrices) == 1
    assert StorePrices[0].Price == 3.5

# Test adding a product with existing product but new store and new brand
def test_add_product_existing_product_new_store_brand():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addProd("Pear", "MEDIUM", 4, "BrandL", 1.2, "StoreA")
    addProd("Pear", "MEDIUM", 4, "BrandK", 1.3, "StoreB")
    assert len(Cart) == 1
    assert Cart[0].ProductName == "Pear"
    assert len(StorePrices) == 2
    assert len(Brands) == 2

# Test adding multiple products with overlapping brands and stores
def test_add_multiple_products_overlapping_brands_stores():
    clear_data()
    addStore("StoreA")
    addStore("StoreB")
    addStore("StoreC")
    addProd("Apple", "LOW", 2, "BrandY", 1.0, "StoreA")
    addProd("Banana", "MEDIUM", 5, "BrandX", 0.5, "StoreA")
    addProd("Apple", "HIGH", 3, "BrandZ", 1.1, "StoreB")
    addProd("Banana", "HIGH", 6, "BrandX", 0.55, "StoreB")
    addProd("Cherry", "LOW", 10, "BrandU", 3.0, "StoreC")
    assert len(Cart) == 3
    assert len(StorePrices) == 5  # Apple in StoreA and StoreB, Banana in StoreA and StoreB, Cherry in StoreC
    assert len(Brands) == 3  # BrandY, BrandX, BrandZ, BrandU (but BrandX repeated)


# Test adding a product to the cart without stores
def test_add_product_noStore():
    clear_data()
    addProd("Orange", "MEDIUM", 3, "BrandZ", 0.8, "StoreA")
    assert len(Cart) == 0
"""