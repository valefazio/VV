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

def test_editUrg_noData(setup_data, capsys):
    clear_data()
    editUrg("Apple","LOW")
    captured = capsys.readouterr()
    assert "Error: Product not found in cart." in captured.out




# show urgency level with incorrect input
def test_editUrg_wrongUrg(setup_data, capsys):
    editUrg("Apple","ANTO")
    captured = capsys.readouterr()
    assert "Error: Invalid urgency level." in captured.out