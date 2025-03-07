import sys
from dataclasses import dataclass

@dataclass
class Product:
    ProductName: str
    UrgencyLevel: {"LOW", "MEDIUM", "HIGH"}
    Quantity: int

@dataclass
class PricexStore:
	ProductName: str
	StoreName: str
	Price: float

@dataclass
class Brand:
	ProductName: str
	Brand: str
    
Cart = []	#list of Products in the cart
Stores = []	#list of Store Names
StorePrices = []	#list of Prices of products in different stores
Brands = []	#list of Brands of products in the cart

def pricesProd (ProductName):	#returns a list of prices of the product in different stores
	pricesIn = []
	for i in range(len(StorePrices)):
		if(ProductName == StorePrices[i].ProductName):
			pricesIn.append([StorePrices[i].Price, StorePrices[i].StoreName])
	return pricesIn

def findCheapestStore (ProductName):	#returns the store with the cheapest price for the product
	pricesIn = pricesProd(ProductName)
	if(len(pricesIn) == 0):
		print("Error: Product not found in any store.")
		return
	min = [pricesIn[0][0], pricesIn[0][1]]
	for i in range(1, len(pricesIn)):
		if(pricesIn[i][0] < min[0]):
			min = [pricesIn[i][0], pricesIn[i][1]]
	return min

def show (CartName):
	if(len(CartName) == 0):
		print("Cart is empty.")
		return
	totalPrice = 0.0
	for i in range(len(Cart)):
		print(f"Product: {Cart[i].ProductName}, Urgency Level: {Cart[i].UrgencyLevel}, Quantity: {Cart[i].Quantity}")
		min = findCheapestStore(Cart[i].ProductName)
		print(f"Cheapest price: € {min[0]} at {min[1]}")
		totalPrice += min[0] * Cart[i].Quantity
		print("Product available in the following brands:")
		for j in range(len(Brands)):
			if(Cart[i].ProductName == Brands[j].ProductName):
				print(f"{Brands[j].Brand}")
	print(f"Total price: € {totalPrice}")

def showUrg (UrgencyLevel): #shows all the products that are in the cart based on the urgency level specified
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
		return
	count = 0
	for i in range(len(Cart)):
		if(UrgencyLevel == Cart[i].UrgencyLevel):
			print(f"Product: {Cart[i].ProductName}, Quantity: {Cart[i].Quantity}")
			min = findCheapestStore(Cart[i].ProductName)
			print(f"Cheapest price: € {min[0]} at {min[1]}")
			count += 1
			print("Product available in the following brands:")
			for j in range(len(Brands)):
				if(Cart[i].ProductName == Brands[j].ProductName):
					print(f"{Brands[j].Brand}")
	if(count == 0):
		print("No products found with the specified urgency level.")
    
def addProd (ProductName, UrgencyLevel, Quantity, BrandName, Price, StoreName):
	if(ProductName == ""):
		print("Error: Product name is empty.")
		return
	elif(UrgencyLevel == ""):
		print("Error: Urgency level is empty.")
		return
	elif(Quantity == ""):
		print("Error: Quantity is empty.")
		return
	elif(BrandName == ""):
		print("Error: Brand is empty.")
		return
	elif(Price == ""):
		print("Error: Price is empty.")
		return
	elif(StoreName == ""):
		print("Error: Store name is empty.")
		return
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
	elif(Quantity < 0):
		print("Error: Invalid quantity.")
	elif(Price < 0):
		print("Error: Invalid price.")
	elif(Stores.count(StoreName) == 0):
		print("Error: Store not found.")
		return
    
	for i in range(len(Cart)):	#check if the product is already in the cart
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity = Quantity
			Cart[i].UrgencyLevel = UrgencyLevel

			found = 0
			for j in range(len(StorePrices)):
				#check if the product is already in the StorePrices list and the store is the same -> update the price
				if(ProductName == StorePrices[j].ProductName):
					if(StoreName == StorePrices[j].StoreName):
						StorePrices[j].Price = Price
						return
					else:
						found = 1
			if(found == 1):
				StorePrices.append(PricexStore(ProductName, StoreName, Price))

			found = 0
			for j in range(len(Brands)):
				#check if the product is already in the Brands list -> add the brand
				if(ProductName == Brands[j].ProductName and BrandName != Brands[j].Brand):
					found = 1
			if(found == 1):
				Brands.append(Brand(ProductName, BrandName))
			return
	#add the product to the cart (if it is not already there)
	Cart.append(Product(ProductName, UrgencyLevel, Quantity))
	StorePrices.append(PricexStore(ProductName, StoreName, Price))
	Brands.append(Brand(ProductName, BrandName))

def remvProd (ProductName):
	count = 0
	for i in range(len(Cart)):	#remove the product from the cart
		if(ProductName == Cart[i].ProductName):
			Cart.pop(i)
			count += 1
			break
	if(count == 0):	#product not found in the cart
		print("Error: Product not found in cart.")
	for i in range(len(StorePrices)):	#remove the product from the StorePrices list
		if(ProductName == StorePrices[i].ProductName):
			StorePrices.pop(i)
	for i in range(len(Brands)):	#remove the product from the Brands list
		if(ProductName == Brands[i].ProductName):
			Brands.pop(i)

def editUrg (ProductName, UrgencyLevel):
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
		return
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].UrgencyLevel = UrgencyLevel
			return
	print("Error: Product not found in cart.")

def editQuantity (ProductName, Quantity):
	if(Quantity < 0):
		print("Error: Invalid quantity.")
		return
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity = Quantity
			return
	print("Error: Product not found in cart.")

def editPrice (ProductName, StoreName, Price):
	if(Price < 0):
		print("Error: Invalid price.")
		return
	if(Stores.count(StoreName) == 0):
		print("Error: Store not found.")
		return
	for i in range(len(StorePrices)):
		if(ProductName == StorePrices[i].ProductName and StoreName == StorePrices[i].StoreName):
			StorePrices[i].Price = Price
			return
	StorePrices.append(PricexStore(ProductName, StoreName, Price))

def addStore (StoreName):
	for i in range(len(Stores)):
		if(StoreName == Stores[i]):
			print("Error: Store already exists.")
			return
	Stores.append(StoreName)

def storesAt (ProductName):	#returns a list of stores that have the product
	storesIn = []
	for i in range(len(StorePrices)):
		if(ProductName == StorePrices[i].ProductName):
			storesIn.append(StorePrices[i].StoreName)
	return storesIn

def remvStore (StoreName):
	if(Stores.count(StoreName) == 0):
		print("Error: Store not found.")
		return
	for i in range(len(Stores)):
		if(StoreName == Stores[i]):
			for j in range(len(Cart)):
				if(storesAt(Cart[j].ProductName).count(StoreName) > 0):
					print("Error: Store has products in cart.")
					return
			Stores.pop(i)
			return
	print("Error: Store not found.")
      
def addBrand (ProductName, BrandName):
	found = 0
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			if(BrandName == Brands[i].Brand):
				print("Error: Brand already exists for this product.")
				return
			found = 1
	if(found == 0):
		print("Error: Product not found in cart.")
		return
	if(found == 1):
		Brands.append(Brand(ProductName, BrandName))

import sys

def process_commands(file_name):
	try:
		with open(file_name, 'r') as file:
			commands = file.readlines()

			for command in commands:
				# Strip whitespace and split into command and arguments
				command_parts = command.strip().split()
				if not command_parts:
					continue  # Skip empty lines
                
				cmd_name = command_parts[0]
				cmd_args = command_parts[1:]

				# Define the command-to-function mapping
				switcher = {
                    "show": show,
                    "addProd": addProd,
                    "showUrg": showUrg,
                    "remvProd": remvProd,
                    "editUrg": editUrg,
                    "editQuantity": editQuantity,
                    "editPrice": editPrice,
                    "addStore": addStore,
                    "remvStore": remvStore,
					"findCheapestStore": findCheapestStore,
					"addBrand": addBrand
				}

				# Get the function from the switcher
				func = switcher.get(cmd_name)
				if func:
					try:
						# Call the function with unpacked arguments
						if cmd_name == "show" or cmd_name == "showUrg":
							func(Cart)
						elif cmd_name == "findCheapestStore":
							func(*cmd_args)
						elif cmd_name == "addProd":
							# Parse arguments: ProductName, UrgencyLevel, Quantity, Brand, Price, StoreName
							try:
								product_name = cmd_args[0]
								urgency_level = cmd_args[1].upper()  # Ensure urgency level is uppercase
								quantity = int(cmd_args[2])
								brand = cmd_args[3]
								price = float(cmd_args[4])
								store_name = cmd_args[5]
								func(product_name, urgency_level, quantity, brand, price, store_name)
							except (ValueError, IndexError) as e:
								print(f"Error: Incorrect arguments for command '{cmd_name}'. {e}")
						elif cmd_name == "editUrg":
							# Parse arguments: ProductName, UrgencyLevel
							product_name = cmd_args[0]
							urgency_level = cmd_args[1].upper()
							func(product_name, urgency_level)
						elif cmd_name == "editQuantity":
							# Parse arguments: ProductName, Quantity
							product_name = cmd_args[0]
							quantity = int(cmd_args[1])
							func(product_name, quantity)
						elif cmd_name == "editPrice":
							# Parse arguments: ProductName, StoreName, Price
							product_name = cmd_args[0]
							store_name = cmd_args[1]
							price = float(cmd_args[2])
							func(product_name, store_name, price)
						elif cmd_name == "addStore" or cmd_name == "remvStore":
							# Parse arguments: StoreName
							store_name = cmd_args[0]
							func(store_name)
						elif cmd_name == "addBrand":
							# Parse arguments: ProductName, Brand
							product_name = cmd_args[0]
							brand = cmd_args[1]
							func(product_name, brand)
					except TypeError as e:
						print(f"Error: Incorrect arguments for command '{cmd_name}'. {e}")
				else:
					print(f"Error: Invalid command '{cmd_name}'.")

	except FileNotFoundError:
		print(f"Error: File '{file_name}' not found.")
	except Exception as e:
		print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: micarrito <input-file>")
        return
    input_file = sys.argv[1]
    process_commands(input_file)

if __name__ == "__main__":
    main()
