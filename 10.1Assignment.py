#10.1 Assignment
#Phi Nguyen
#CSE 20
class Property(): #Property Class that has properties as objects and classifies them by price, square footage, number of bath, bedrooms
    def __init__(self ,squarefootage, bedrooms, bathrooms, price):
        self.getid = 'This is a property'
        self.squarefootage = squarefootage
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price

    def get_square_footage(self): #returns square footage
        return(self.squarefootage)

    def get_bedrooms(self): #returns the number of bedrooms
        return(self.bedrooms)

    def get_bathrooms(self): #returns the number of bathrooms
        return(self.bathrooms)

    def calculate_price_per_sq_ft(self): #calculates price per square footage (most home buying websites have this feature)
        a = str(self.price/self.squarefootage)
        print("$"+a+' per square feet')

    def calculate_price_per_bedroom(self):
        b = str(self.price/self.bedrooms)
        print("$"+b+' per bedroom')
    
    def show_details(self): #shows the details about the home
        print("Property Details")
        print(self.getid)
        print(str(self.squarefootage)+' square feet')
        print(str(self.bedrooms)+' bedrooms')
        print(str(self.bathrooms)+' bathrooms')
        print('$'+str(self.price))
    
        
class Apartment(Property): #first and most common/basic property 
    def __init__(self, squarefootage, bedrooms, bathrooms, price):
        super().__init__(squarefootage, bedrooms, bathrooms, price)
        self.getid = 'This is an Apartment'
a = Apartment(800, 4, 3, 1234000)

#a.show_details()
#print(a.calculate_price_per_sq_ft())


class House(Property): #this property might include a backyard or a pool
    def __init__(self, squarefootage, bedrooms, bathrooms, price, backyard, pool):
        super().__init__(squarefootage, bedrooms, bathrooms, price)
        self.getid = 'This is a House'
        self.backyard = backyard
        self.pool = pool
    
    def show_details_house(self): #house only function
        if self.backyard == "YES":
            print('There is a backyard')
        elif self.backyard == "NO":
            print('There is no backyard')
        else:
            print("invalid input")
        if self.pool == "YES":
            print('There is a pool')
        elif self.pool == "NO":
            print('There is no pool')
        else:
            print('invalid input')

house = House(4000, 4, 3, 13000000, "YES", "YES")


#house.show_details()
#house.show_details_house() 
#rint(house.calculate_price_per_sq_ft())


class BeachHouse(Property):
    def __init__(self, squarefootage, bedrooms, bathrooms, price, beachfront):
        super().__init__(squarefootage, bedrooms, bathrooms, price)
        self.getid = 'This is a Beach House'
        self.beachfront = beachfront

    def show_details_beach_house(self): #beach house onlyfunction
        if self.beachfront == "YES":
            print("The House has is a beachfront property")
        elif self.beachfront == "NO":
            print("The House is not a beachfront property")
        else:
            print('invalid input')

Beach_House = BeachHouse(2500, 3, 2, 15000000, 'YES')

#Beach_House.show_details()
#Beach_House.show_details_beach_house
#print(Beach_House.calculate_price_per_sq_ft())

class MultiFamilyHome(Property):
    def __init__(self, squarefootage, bedrooms, bathrooms, price, units):
        super().__init__(squarefootage, bedrooms, bathrooms, price)
        
        self.getid = 'This is a Multifamily Home'
        self.units = units
    
    def show_details_multifamily(self): #multi family only function
        return('Price per Units $'+str(self.price/self.units))
multifamily = MultiFamilyHome(6000, 10, 5, 400000, 5)

#multifamily.show_details()
#print(multifamily.show_details_multifamily())


#DEMO PROGRAM

fourthreetwo_rexford_drive = Apartment(1500, 2, 1, 800000)

fourthreetwo_rexford_drive.show_details()
fourthreetwo_rexford_drive.calculate_price_per_sq_ft()

ninesevenfive_crescent_drive = MultiFamilyHome(3000, 8, 4, 2000000, 4)
ninesevenfive_crescent_drive.show_details()
ninesevenfive_crescent_drive.calculate_price_per_sq_ft()