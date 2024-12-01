import sys
from dataclasses import dataclass

@dataclass
class Product:
    ProductName: str
    UrgencyLevel: str
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
	print(f"\tCheapest store for {ProductName} is {min[1]} that sells it at € {min[0]}")
	return min

def show (CartName):
	if(len(CartName) == 0):
		print("Cart is empty.")
		return
	print("CART:")
	totalPrice = 0.0
	for i in range(len(Cart)):
		print(f"Product: {Cart[i].ProductName}, Urgency Level: {Cart[i].UrgencyLevel}, Quantity: {Cart[i].Quantity}")
		min = findCheapestStore(Cart[i].ProductName)
		#print(f"\tCheapest price: € {min[0]} at {min[1]}")
		totalPrice += min[0] * Cart[i].Quantity
		print("\tProduct available in the following brands:")
		for j in range(len(Brands)):
			if(Cart[i].ProductName == Brands[j].ProductName):
				print(f"\t* {Brands[j].Brand}")
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
			#print(f"\tCheapest price: € {min[0]} at {min[1]}")
			count += 1
			print("\tProduct available in the following brands:")
			for j in range(len(Brands)):
				if(Cart[i].ProductName == Brands[j].ProductName):
					print(f"\t* {Brands[j].Brand}")
	if(count == 0):
		print("No products found with the specified urgency level.")
    
def addProd (ProductName, UrgencyLevel, Quantity, BrandName, Price, StoreName):
	if(ProductName == ""):
		print("Error: Invalid Product Name.")
		return
	elif(BrandName == ""):
		print("Error: Invalid brand.")
		return
	elif(Price == "" or Price < 0):
		print("Error: Invalid price.")
		return
	elif(StoreName == ""):
		print("Error: Invalid store name.")
		return
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
		return
	elif(Quantity == "" or Quantity < 0 or type(Quantity) != int):
		print("Error: Invalid quantity.")
		return
	elif(Stores.count(StoreName) == 0):
		print("Error: Store not found.")
		return
    
	for i in range(len(Cart)):	#check if the product is already in the cart
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity = Quantity
			Cart[i].UrgencyLevel = UrgencyLevel
			
			#check if the product is already in the StorePrices list and the store is the same
			found = 0
			for j in range(len(StorePrices)):
				if(ProductName == StorePrices[j].ProductName):
					if(StoreName == StorePrices[j].StoreName):
						StorePrices[j].Price = Price
						print(f"Price of {ProductName} at {StoreName} correctly updated.")
						break
					else:
						found = 1
			if(found == 1):
				StorePrices.append(PricexStore(ProductName, StoreName, Price))

			#check if the product is already in the Brands list and the brand is the same
			found = 0
			for j in range(len(Brands)):
				if(ProductName == Brands[j].ProductName):
					if(BrandName != Brands[j].Brand):
						found = 1
					else:
						#print("Error: Brand already exists for this product.")
						break
			if(found == 1):
				Brands.append(Brand(ProductName, BrandName))
			print(f"Product {ProductName} correctly updated in cart.")
			return
	#add the product to the cart (if it is not already there)
	Cart.append(Product(ProductName, UrgencyLevel, Quantity))
	StorePrices.append(PricexStore(ProductName, StoreName, Price))
	Brands.append(Brand(ProductName, BrandName))
	print(f"Product {ProductName} correctly added to cart.")

def remvProd (ProductName):
	count = 0
	for item in Cart[:]:	#remove the product from the cart
		if(ProductName == item.ProductName):
			Cart.remove(item)
			count += 1
			break
	if(count == 0):	#product not found in the cart
		print("Error: Product not found in cart.")
		return
	for item in StorePrices[:]:	#remove the product from the StorePrices list
		if(ProductName == item.ProductName):
			StorePrices.remove(item)
	for item in Brands[:]:	#remove the product from the Brands list
		if(ProductName == item.ProductName):
			Brands.remove(item)
	print(f"Product {ProductName} correctly removed from cart.")

def editUrg (ProductName, UrgencyLevel):
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
		return
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].UrgencyLevel = UrgencyLevel
			print(f"Urgency level of {ProductName} correctly updated.")
			return
	print("Error: Product not found in cart.")

def editQuantity (ProductName, Quantity):
	if(Quantity < 0 or type(Quantity) != int):
		print("Error: Invalid quantity.")
		return
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity = Quantity
			print(f"Quantity of {ProductName} correctly updated.")
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
			print(f"Price of {ProductName} at {StoreName} correctly updated.")
			return
	StorePrices.append(PricexStore(ProductName, StoreName, Price))
	print(f"Price of {ProductName} at {StoreName} correctly added.")

def addStore (StoreName):
	for i in range(len(Stores)):
		if(StoreName == Stores[i]):
			print("Error: Store already exists.")
			return
	Stores.append(StoreName)
	print(f"Store {StoreName} correctly added.")

def remvStore(StoreName):
	if(Stores.count(StoreName) == 0):
		print("Error: Store not found.")
		return
	for i in Stores[:]:
		if(StoreName == i):
			#for j in range(len(Cart)):
			if any(price.StoreName == StoreName for price in StorePrices):
				print("Error: Store has products in cart.")
				return
			Stores.remove(i)
			print(f"Store {StoreName} correctly removed.")
			#return
		
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
	else:
		Brands.append(Brand(ProductName, BrandName))
		print(f"Brand {BrandName} correctly added to product {ProductName}.")

def process_commands(file_name):
    try:
        with open(file_name, 'r') as file:
            commands = file.readlines()

            for line_number, command in enumerate(commands, start=1):
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
                    #try:
                        # Call the function with unpacked arguments
                        if cmd_name == "show":
                            func(Cart)
                        elif cmd_name == "showUrg":
                            # Expecting one argument: UrgencyLevel
                            if len(cmd_args) != 1 and cmd_args[0]!="":
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            urgency_level = cmd_args[0].upper()
                            func(urgency_level)
                        elif cmd_name == "findCheapestStore":
                            if len(cmd_args) != 1 and cmd_args[0]!="":
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            func(cmd_args[0])
                        elif cmd_name == "addProd":
                            # Expecting six arguments: ProductName, UrgencyLevel, Quantity, Brand, Price, StoreName
                            if len(cmd_args) != 6:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            try:
                                product_name = cmd_args[0]
                                urgency_level = cmd_args[1].upper()  # Ensure urgency level is uppercase
                                quantity = int(cmd_args[2])
                                brand = cmd_args[3]
                                price = float(cmd_args[4])
                                store_name = cmd_args[5]
                                func(product_name, urgency_level, quantity, brand, price, store_name)
                            except ValueError as e:
                                print(f"Error: Invalid argument types for command '{cmd_name}' on line {line_number}. {e}")
                        elif cmd_name == "editUrg":
                            # Expecting two arguments: ProductName, UrgencyLevel
                            if len(cmd_args) != 2:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            product_name = cmd_args[0]
                            urgency_level = cmd_args[1].upper()
                            func(product_name, urgency_level)
                        elif cmd_name == "editQuantity":
                            # Expecting two arguments: ProductName, Quantity
                            if len(cmd_args) != 2:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            product_name = cmd_args[0]
                            try:
                                quantity = int(cmd_args[1])
                                func(product_name, quantity)
                            except ValueError as e:
                                print(f"Error: Invalid quantity for command '{cmd_name}'.")
                        elif cmd_name == "editPrice":
                            # Expecting three arguments: ProductName, StoreName, Price
                            if len(cmd_args) != 3:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            product_name = cmd_args[0]
                            store_name = cmd_args[1]
                            try:
                                price = float(cmd_args[2])
                                func(product_name, store_name, price)
                            except ValueError as e:
                                print(f"Error: Invalid price for command '{cmd_name}'.")
                        elif cmd_name in ["addStore", "remvStore"]:
                            # Expecting one argument: StoreName
                            if len(cmd_args) != 1 and cmd_args[0]!="":
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            store_name = cmd_args[0]
                            func(store_name)
                        elif cmd_name == "addBrand":
                            # Expecting two arguments: ProductName, BrandName
                            if len(cmd_args) != 2:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            product_name = cmd_args[0]
                            brand = cmd_args[1]
                            func(product_name, brand)
                        #elif cmd_name == "remvProd":
                        else: 
						    # Expecting one argument: ProductName
                            if len(cmd_args) != 1:
                                print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                                continue
                            product_name = cmd_args[0]
                            func(product_name)
                    #except TypeError as e:
                        #print(f"Error: Incorrect number of arguments for command '{cmd_name}'.")
                else:
                    print(f"Error: Invalid command '{cmd_name}'.", end="")
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
