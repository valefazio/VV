import pytest
from dataclasses import dataclass
from project.micarrito import *  # Import functions from the file where they are defined



def clear_data():
    Cart.clear()
    Stores.clear()
    StorePrices.clear()
    Brands.clear()
