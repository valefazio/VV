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

def show (CartName):
	if(CartName.size() == 0):
		print("Cart is empty.")
		return
	#for i in range(len(Cart)):
		

#def showUrg (UrgencyLevel): #shows all the products that are in the cart based on the urgency level specified
    
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
    
	for i in range(len(Cart)):	#check if the product is already in the cart
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity += Quantity
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
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart.pop(i)
			break
	for i in range(len(StorePrices)):
		if(ProductName == StorePrices[i].ProductName):
			StorePrices.pop(i)
			break
	for i in range(len(Brands)):
		if(ProductName == Brands[i].ProductName):
			Brands.pop(i)
	print("Error: Product not found in cart.")  #ERROR NOT DEFINED

def editUrg (ProductName, UrgencyLevel):
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].UrgencyLevel = UrgencyLevel
			return
	print("Error: Product not found in cart.")  #ERROR NOT DEFINED

def editQuantity (ProductName, Quantity):
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].Quantity = Quantity
			return
	print("Error: Product not found in cart.")  #ERROR NOT DEFINED

#def editPrice (ProductName, StoreName, Price):

def addStore (StoreName):
	for i in range(len(Stores)):
		if(StoreName == Stores[i]):
			print("Error: Store already exists.")  #ERROR NOT DEFINED
			return
	Stores.append(StoreName)

def remvStore (StoreName):
	for i in range(len(Stores)):
		if(StoreName == Stores[i]):
			Stores.pop(i)
			return
	print("Error: Store not found.")  #ERROR NOT DEFINED

#def findCheapestStore():
	"""if(len(Stores) == 0):
		print("Error: No stores available.")  #ERROR NOT DEFINED
		return
	minPrice = 0
	minStore = ""
	for i in range(len(Stores)):
		totalPrice = 0
		for j in range(len(Cart)):
			totalPrice += Cart[j].Price
		if(totalPrice < minPrice):
			minPrice = totalPrice
			minStore = Stores[i]
	print(f"Cheapest store: {minStore}") """
      
def addBrand (ProductName, Brand):
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart[i].Brand = Brand
			return
	print("Error: ")  #ERROR NOT DEFINED

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
					"findCheapestStore": findCheapestStore()
                    }
                switcher.get(command[:4], lambda: print("Error: Invalid command '{}'.".format(command[:4]))())	#Error: Invalid command '<CommandName>'

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: micarrito <input-file>")  #ERROR NOT DEFINED
        return
    input_file = sys.argv[1]
    process_commands(input_file)

if __name__ == "__main__":
    main()
