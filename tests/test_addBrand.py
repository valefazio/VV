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



    



# Test adding a brand with no Cart
def test_addBrand_noCart(capsys):
    clear_data()
    addBrand("Apple","BrandY")
    captured = capsys.readouterr()

    assert "Error: Product not found in cart." in captured.out


# Test adding a brand
def test_addBrand(setup_data):
    addBrand("Apple","BrandY")
    
    assert any(brand.ProductName == "Apple" and brand.Brand == "BrandY"  for brand in Brands)


def test_addBrand_sameBrand(setup_data,capsys):

    addBrand("Apple","BrandX")
    captured = capsys.readouterr()

    assert "Error: Brand already exists for this product." in captured.out



# I get 95% because it always enters the last branch , 
# just take out the last if statement

