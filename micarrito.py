import sys
from dataclasses import dataclass

@dataclass
class Product:
    ProductName: str
    UrgencyLevel: {"LOW", "MEDIUM", "HIGH"}
    Quantity: int
    Price: float
    Brand: str = None
    
Cart = []
Stores = []

def show (CartName):
    print(CartName)

#def showUrg (UrgencyLevel): #shows all the products that are in the cart based on the urgency level specified
    
def addProf (ProductName, UrgencyLevel, Quantity, Price): #Brand????
    """ #DO WE TAKE CARE OF THIS?
    if(ProductName == ""):
        print("Error: Product name is empty.")
    elif(UrgencyLevel == ""):
        print("Error: Urgency level is empty.")
    elif(Quantity == ""):
        print("Error: Quantity is empty.")
    elif(Price == ""):
        print("Error: Price is empty.")"""
    if(UrgencyLevel != "LOW" and UrgencyLevel != "MEDIUM" and UrgencyLevel != "HIGH"):
        print("Error: Invalid urgency level.")  #ERROR NOT DEFINED
    elif(Quantity < 0):
        print("Error: Invalid quantity.")   #ERROR NOT DEFINED
    elif(Price < 0):
        print("Error: Invalid price.")  #ERROR NOT DEFINED
    
    for i in range(len(Cart)):	#check if the product is already in the cart
        if(ProductName == Cart[i].ProductName):
            Cart[i].Quantity += Quantity
            Cart[i].UrgencyLevel = UrgencyLevel
            return
    Cart.append(Product(ProductName, UrgencyLevel, Quantity, Price))

def remvProd (ProductName):
	for i in range(len(Cart)):
		if(ProductName == Cart[i].ProductName):
			Cart.pop(i)
			return
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
					"addProd": addProf(command[4:]),
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
