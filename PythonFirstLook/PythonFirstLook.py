import datetime

# Create an abstract class Shop with general parameters


class Shop():

    def __init__(self, name, type_of, price, barcode, pack_date, exp_date):
        self.type_of = type_of
        self.name = name
        self.price = price
        self.barcode = barcode
        self.pack_date = pack_date
        self.exp_date = exp_date

        
    def show_info(self):
        pass
     
#Create a class Egg that inherits inteface Shop

class Egg(Shop):

    def __init__(self, name, type_of, size,amount_in_pac, price, barcode, pack_date, exp_date):

        super().__init__(type_of, name, price, barcode, pack_date, exp_date)
        self.size = size
        self.amount_in_pac = amount_in_pac

    def show_info(self):
        print(f"Type of this product: {self.type_of}\n" +
              f"Name of this product: {self.name}\n" +
              f"Price of this product: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Size of eggs: {self.size}\n" +
              f"Amount in one pack: {self.amount_in_pac}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n")
        

#Create a class Cheese that inherits inteface Shop

class Cheese(Shop):

     def __init__(self, name, type_of, weight, price, barcode, pack_date, exp_date):

         super().__init__(type_of, name, price, barcode, pack_date, exp_date)
         self.weight = weight

     def show_info(self):
        print(f"Type of this product: {self.type_of}\n" +
              f"Name of this product: {self.name}\n" +
              f"Price of this product: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Weight: {self.weight}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n")


#Create a class Drink that inherits inteface Shop

class Drink(Shop):   

    def __init__(self, is_alcoholic, type_of, name, volume, price, barcode, pack_date, exp_date):
        super().__init__(name, type_of, price, barcode, pack_date, exp_date)
        self.is_alcoholic = is_alcoholic
        self.volume = volume

    def show_info(self):
        print(f"Is drink alcoholic: {bool(self.is_alcoholic)}\n" +
              f"Type of this drink: {self.type_of}\n" +
              f"Name of this drink: {self.name}\n" +
              f"Volume of this drink: {self.volume}\n" +
              f"Price of this drink: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n") 

#Create a class Meat that inherits inteface Shop

class Meat(Shop):

    def __init__(self, name, type_of, weight, price, barcode, pack_date, exp_date):

        super().__init__(type_of, name, price, barcode, pack_date, exp_date)
        self.weight = weight

    def show_info(self):
        print(f"Type of meat: {self.type_of}\n" +
              f"Name of meat: {self.name}\n" +
              f"Price of meat: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Weight: {self.weight}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n")
   

#Create a class BakeryProduct that inherits inteface Shop

class BakeryProduct(Shop):

    def __init__(self, name, type_of, amount, price, barcode, pack_date, exp_date):

        super().__init__(type_of, name, price, barcode, pack_date, exp_date)
        self.amount = amount

    def show_info(self):
        print(f"Type of this product: {self.type_of}\n" +
              f"Name of this product: {self.name}\n" +
              f"Price of this product: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Amount of product: {self.amount}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n")
        


#Create a class Produce that inherits inteface Shop

class Produce(Shop):    # Generic word for fruits and vegetables

    def __init__(self, name, type_of, weight, price, barcode, pack_date, exp_date):

        super().__init__(type_of, name, price, barcode, pack_date, exp_date)
        self.weight = weight

    def show_info(self):
        print(f"Type of this product: {self.type_of}\n" +
              f"Name of this product: {self.name}\n" +
              f"Price of this product: {self.price}\n" +
              f"Barcode: {self.barcode}\n" +
              f"Weight of product: {self.weight}\n" +
              f"Packing date: {self.pack_date}\n" +
              f"Expiry date: {self.exp_date}\n")

                                                        # Create objects for our classes

chicken_eggs = Egg("Chicken eggs", "Cluckin'nBell eggs", 'M', 10, 7.99, "415717",datetime.date(2023,3,5), datetime.date(2023,12,5))
print(f"\t\t{chicken_eggs.name}:\n")
chicken_eggs.show_info()

goose_eggs = Egg("Goose eggs", "Gus'nBell eggs", 'L', 10, 9.20, "315756", datetime.date(2023,3,7), datetime.date(2023,10,6))
print(f"\t\t{goose_eggs.name}:\n")
goose_eggs.show_info()

white_cheese = Cheese("White cheese", "Mozzarella Mlekovita", 0.7, 11, "675422", datetime.date(2023,3,2), datetime.date(2023,4,2))
print(f"\t\t{white_cheese.name}:\n")
white_cheese.show_info()

cheddar_mlekovita = Cheese("Yellow cheese", "Cheddar Mlekovita", 1.2, 15, "294165", datetime.date(2023,3,8), datetime.date(2023,4,12))
print(f"\t\t{cheddar_mlekovita.name}:\n")
cheddar_mlekovita.show_info()

milk_mlekovita = Drink(False, "Milk", "Milk \"Mlekovita\"", 1, 4.99, "167354",datetime.date(2023,3,6), datetime.date(2023,3,20)) # - I create milk like a class Drink. At first i wanted add Cheese to Milk and create class - Milk products, but they are measured in different units

print(f"\t\t{milk_mlekovita.name}:\n")
milk_mlekovita.show_info()

beef_premium = Meat("Beef meat","Premium Rap Beef", 1, 30, "898545", datetime.date(2023,3,2), datetime.date(2023,3,13))
print(f"\t\t{beef_premium.name}:\n")
beef_premium.show_info()

water_kropla_beskidu = Drink(False, "Mineral water", "Mineral water \"Kropla Beskidu", 0.5, 3, "735901", datetime.date(2023,3,7), datetime.date(2023,8,20))
print(f"\t\t{water_kropla_beskidu.name}:\n")
water_kropla_beskidu.show_info()

white_bread = BakeryProduct("White bread", "Group Chleb", 1, 3.20, "151784", datetime.date(2023,3,9), datetime.date(2023,3,10))
print(f"\t\t{white_bread.name}:\n")
white_bread.show_info()

bulka_kajzerka = BakeryProduct("Kajzerka", "Kajzerka Polska", 1, 3.80, "446322", datetime.date(2023,3,9), datetime.date(2023,3,11))
print(f"\t\t{bulka_kajzerka.name}:\n")
bulka_kajzerka.show_info()

radishes = Produce("Vegetable", "Rzodkievka luz", 1, 3.99, "552637", datetime.date(2023,3,9), datetime.date(2023,3,14))
print(f"\t\t{radishes.name}:\n")
radishes.show_info()

cucubmers = Produce("Vegatable", "Green Cucumber Rick", 1, 4.20, "666453", datetime.date(2023,3,9), datetime.date(2023,3,15))
print(f"\t\t{cucubmers.name}\n")
cucubmers.show_info()

apples_red = Produce("Fruit", "Red apples Tim Cook", 1, 4.70, "107642", datetime.date(2023,3,9), datetime.date(2023,3,10))
print(f"\t\t{apples_red.name}:\n")
apples_red.show_info()

onions_luz = Produce("Vegatable", "Onions Pringles", 1, 1.90, "995541", datetime.date(2023,3,9), datetime.date(2023,5,16))
print(f"\t\t {onions_luz.name}\n")
onions_luz.show_info()




                                                                        # Task 2 (Clothes)

# Create an abstract class ShowRoom with general parameters

class ShowRoom():

    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size):
      self.clothes_type = clothes_type
      self.brand = brand
      self.name = name
      self.w_or_m_clothes = w_or_m_clothes
      self.size = size
        
    def info_about_clothes(self):
        pass


#Create a class Accessories that inherits inteface ShowRoom

class Accessories(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, part_of_body):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.part_of_body = part_of_body

    def info_about_clothes(self):
        print(f"Type of thing: {self.clothes_type}\n" +
              f"Name of thing: {self.name}\n" +
              f"Brand of thing: {self.brand}\n" +
              f"Man or woman accesories: {self.w_or_m_clothes}\n" +
              f"Size of thing: {self.size}\n" +
              f"Body Part Accessory: {self.part_of_body}\n")
        
#Create a class Headwear that inherits inteface ShowRoom

class Headwear(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, is_worm):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.is_worm = is_worm

    def info_about_clothes(self):

        print(f"Type of thing: {self.clothes_type}\n" +
              f"Name of thing: {self.name}\n" +
              f"Brand of thing: {self.brand}\n" +
              f"Man or woman headwear: {self.w_or_m_clothes}\n" +
              f"Size of thing: {self.size}")
        if(self.is_worm is True):
            print("This hat is for cool weather\n")
        else:
            print("This hat is for hot or warm weather\n")


#Create a class Footwear that inherits inteface ShowRoom

class Footwear(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, what_season_of_year):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.what_season_of_year = what_season_of_year
    
    def info_about_clothes(self):
        def switch(what_season_of_year):
            if what_season_of_year == "Winter":
                print("These footwear are for winter\n")
            elif what_season_of_year == "Summer":
                print("These footwear are for summer\n")
            elif what_season_of_year == "Autumn":
                print("These footwear are for autumn\n")
            elif what_season_of_year == "Spring":
                print("These footwear are for spring\n")
            elif what_season_of_year == "All seasons":
                print("These footwear are for all seasons\n")

        print(f"Type of shoes: {self.clothes_type}\n" +
              f"Man or woman shoes: {self.w_or_m_clothes}\n" +
              f"Name of shoes: {self.name}\n" +
              f"Brand of shoes: {self.brand}\n" +
              f"Size of shoes: {self.size}")
        print(switch(self.what_season_of_year))





       
        
        
                
#Create a class Outwear that inherits inteface ShowRoom
           
class Outwear(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, what_season_of_year, material):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.what_season_of_year = what_season_of_year
        self.material = material
    
    def info_about_clothes(self):
        def switch(what_season_of_year):
            if what_season_of_year == "Winter":
                print("These outwear are for winter\n")
            elif what_season_of_year == "Summer":
                print("These outwear are for summer\n")
            elif what_season_of_year == "Autumn":
                print("These outwear are for autumn\n")
            elif what_season_of_year == "Spring":
                print("These outwear are for spring\n")
            elif what_season_of_year == "All seasons":
                print("These outwear are for all seasons\n")

        print(f"Type of outwear: {self.clothes_type}\n" +
              f"Name of outwear: {self.name}\n" +
              f"Man or woman outwear: {self.w_or_m_clothes}\n" +
              f"Brand of outwear: {self.brand}\n" +
              f"Size of outwear: {self.size}\n" +
              f"Material of outwear: {self.material}")
        print(switch(self.what_season_of_year))


#Create a class UpperBody that inherits inteface ShowRoom

class UpperBody(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, is_formal_d_code):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.is_formal_d_code = is_formal_d_code
    
    def info_about_clothes(self):

        print(f"Type of outwear: {self.clothes_type}\n" +
              f"Name of outwear: {self.name}\n" +
              f"Man or woman upper body: {self.w_or_m_clothes}\n" +
              f"Brand of outwear: {self.brand}\n" +
              f"Size of outwear: {self.size}")

        if(self.is_formal_d_code is True):
            print("This body wear is formal style\n")
        else:
            print("This body wear is casual style\n")

#Create a class LowerBody that inherits inteface ShowRoom

class LowerBody(ShowRoom):
    def __init__(self, clothes_type, brand, name, w_or_m_clothes, size, is_formal_d_code, material):
        super().__init__(clothes_type, brand, name, w_or_m_clothes, size)
        self.is_formal_d_code = is_formal_d_code
        self.material = material

    def info_about_clothes(self):

        print(f"Type of lower body: {self.clothes_type}\n" +
              f"Name of lower body: {self.name}\n" +
              f"Man or lower body: {self.w_or_m_clothes}\n" +
              f"Brand of lower body: {self.brand}\n" +
              f"Material of lower body: {self.material}\n" +
              f"Size of lower body: {self.size}")

        if(self.is_formal_d_code is True):
            print("This body wear is formal style\n")
        else:
            print("This body wear is casual style\n")

                                                                                        # Create objects for our classes

socks = Footwear("Socks","Nike","Black socks Nike", "Man","39-41","Winter")
print(f"\t\t{socks.name}\n")
socks.info_about_clothes()

adidas_sneakers = Footwear("boots", "Adidas", "Adidas TurboFlex", "Woman", 40, "All seasons")
print(f"\t\t{adidas_sneakers.name}\n")
adidas_sneakers.info_about_clothes()

bandana_kizaru = Headwear("Bandana", "Kizaru", "Kizaru Bandana 2", "Man", "S", False)
print(f"\t\t{bandana_kizaru.name}\n")
bandana_kizaru.info_about_clothes()

shawl_cocoshawel = Headwear("Shawl", "CoCo Shawl", "CoCo Shawel V2", "Woman", "XL", True)
print(f"\t\t{shawl_cocoshawel.name}\n")
shawl_cocoshawel.info_about_clothes()

cap_stoneisland = Headwear("Cap", "Stone Island", "Stone Island cap for Gigachads", "Man", "M", True)
print(f"\t\t{cap_stoneisland.name}\n")
cap_stoneisland.info_about_clothes()

gloves_cropp = Outwear("Gloves", "CROPP", "Sport gloves Rick'n'Morty", "Man", 15, "Winter", "Wool")
print(f"\t\t{gloves_cropp.name}\n")
gloves_cropp.info_about_clothes()

trousers_stoneisland = LowerBody("Pants", "Stone Island", "Trousers Stone Island", "Man", 25, True, "Cotton")
print(f"\t\t{trousers_stoneisland.name}\n")
trousers_stoneisland.info_about_clothes()

dress_luisvetron = UpperBody("Dress","Luis Vetron", "Luis Vetron Deluxe Dress", "Woman", "XS", True)
print(f"\t\t{dress_luisvetron.name}\n")
dress_luisvetron.info_about_clothes()

skirt_diand = LowerBody("Skirt", "Diand", "Skirt for little skiny girls", "Woman", "XS", True, "Cotton")
print(f"\t\t{skirt_diand.name}\n")
skirt_diand.info_about_clothes()

coat_pickyblinders = Outwear("Coat", "Picky Blinders", "Tomas Shelby's coat", "Man", "L", "All seasons", "Wool")
print(f"\t\t{coat_pickyblinders.name}\n")
coat_pickyblinders.info_about_clothes()

shirt_for_programmers = UpperBody("Shirt", "C# clothes", "Shirt for real programmers", "Unisex", "M", True)
print(f"\t\t{shirt_for_programmers.name}\n")
shirt_for_programmers.info_about_clothes()

t_shirt_piwozawr = UpperBody("T-Shirt", "Piwo Inc.", "Piwozawrs army t-shirt", "Man", "L", False)
print(f"\t\t{t_shirt_piwozawr.name}\n")
t_shirt_piwozawr.info_about_clothes()

glasses_Gussi = Accessories("Glasses", "Gussi", "Gussi Tir 1 glasses", "Unisex", "S", "Head (eyes)")
print(f"\t\t{glasses_Gussi.name}\n")
glasses_Gussi.info_about_clothes()

headband_4f = Accessories("Headband", "4F", "4F Headband for training", "Unisex", "L", "Head")
print(f"\t\t{headband_4f.name}\n")
headband_4f.info_about_clothes()

scarf_versasi = Outwear("Scarf", "VerSaSSi", "Scarf from VerSaSSi", "Woman", "XS", "Spring", "Wool")
print(f"\t\t{scarf_versasi.name}\n")
scarf_versasi.info_about_clothes()

hoodie_navi = UpperBody("Hoodie", "Puma", "NaVi x Puma hoodie collaboration", "Unisex", "XL", False)
print(f"\t\t{hoodie_navi.name}\n")
hoodie_navi.info_about_clothes()

sweter_zara = UpperBody("Sweter", "Zara", "Wool Black sweter", "Man", "S", True)
print(f"\t\t{sweter_zara.name}\n")
sweter_zara.info_about_clothes()
        


      
    
    