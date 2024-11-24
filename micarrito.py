import sys
from dataclasses import dataclass

@dataclass
class Product:
    ProductName: str
    UrgencyLevel: {"LOW", "MEDIUM", "HIGH"}
    Quantity: int

class PricexStore:
	ProductName = str
	StoreName = str
	Price = float

class Brand:
	ProductName = str
	Brand = str
    
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
	if(CartName.size() == 0):
		print("Cart is empty.")
		return
	totalPrice = 0.0
	for i in range(len(Cart)):
		print(f"Product: {Cart[i].ProductName}, Urgency Level: {Cart[i].UrgencyLevel}, Quantity: {Cart[i].Quantity}")
		min = findCheapestStore(Cart[i].ProductName)
		print(f"Cheapest price: {min[0]} at {min[1]}")
		totalPrice += min[0] * Cart[i].Quantity
		print("Product available in the following brands:")
		for j in range(len(Brands)):
			if(Cart[i].ProductName == Brands[j].ProductName):
				print(f"{Brands[j].Brand}")
	print(f"Total price: {totalPrice}")

def showUrg (UrgencyLevel): #shows all the products that are in the cart based on the urgency level specified
	if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
		print("Error: Invalid urgency level.")
		return
	count = 0
	for i in range(len(Cart)):
		if(UrgencyLevel == Cart[i].UrgencyLevel):
			print(f"Product: {Cart[i].ProductName}, Quantity: {Cart[i].Quantity}")
			min = findCheapest(Cart[i].ProductName)
			print(f"Cheapest price: {min[0]} at {min[1]}")
			count += 1
			print("Product available in the following brands:")
			for j in range(len(Brands)):
				if(Cart[i].ProductName == Brands[j].ProductName):
					print(f"{Brands[j].Brand}")
	if(count == 0):
		print("No products found with the specified urgency level.")
    
def addProd (ProductName, UrgencyLevel, Quantity, Brand, Price, StoreName):
	if(ProductName == ""):
		print("Error: Product name is empty.")
		return
	elif(UrgencyLevel == ""):
		print("Error: Urgency level is empty.")
		return
	elif(Quantity == ""):
		print("Error: Quantity is empty.")
		return
	elif(Brand == ""):
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
				if(ProductName == Brands[j].ProductName and Brand != Brands[j].Brand):
					found = 1
			if(found == 1):
				Brands.append(Brand(ProductName, Brand))
			return
	#add the product to the cart (if it is not already there)
	Cart.append(Product(ProductName, UrgencyLevel, Quantity, Price))

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
      
def addBrand (ProductName, Brand):
	found = 0
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			if(Brand == Brands[i].Brand):
				print("Error: Brand already exists for this product.")
				return
			found = 1
	if(found == 0):
		print("Error: Product not found in cart.")
		return
	if(found == 1):
		Brands.append(Brand(ProductName, Brand))

def process_commands(file_name):
    try:
        with open(file_name, 'r') as file:
            commands = file.readlines()
            for command in commands:
                switcher = {
                    "show": show(command[5:]),
					"addProd": addProd(command[4:]),
					"showUrg": showUrg(command[6:]),
					"remvProd": remvProd(command[7:]),
					"editUrg": editUrg(command[7:]),
					"editQuantity": editQuantity(command[12:]),
					"editPrice": editPrice(command[9:]),
					"addStore": addStore(command[8:]),
					"remvStore": remvStore(command[9:]),
					"findCheapestStore": findCheapestStore(command[17:]),
                    }
                switcher.get(command[:4], lambda: print("Error: Invalid command '{}'.".format(command[:4]))())	#Error: Invalid command '<CommandName>'

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
