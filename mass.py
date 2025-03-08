# converters/mass_converter.py
# def mass_conversion():
def kg_to_g(kg):
   return kg * 1000

def g_to_kg(g):
   return g / 1000

def kg_to_lb(kg):
   return kg * 2.20462

def lb_to_kg(lb):
   return lb / 2.20462

def g_to_oz(g):
   return g / 28.3495

def oz_to_g(oz):
   return oz*28.3495



from mass import kg_to_g, g_to_kg, kg_to_lb, lb_to_kg, g_to_oz, oz_to_g

def mass_conversion():
 
 print("\"Welcome to the Unit Converter for Mass\"")
 print("Select the type of conversion:")
 print("1. Kilograms to Grams")
 print("2. Grams to Kilograms")
 print("3. Kilograms to Pounds")
 print("4. Pounds to Kilograms")
 print("5. Grams to Ounces")
 print("6. Ounces to Grams")

#  value_mass = eval(input("Enter the mass value: "))
 choice_mass = int(input("Enter choice (1/2/3/4/5/6) "))

 value_mass = float(input("Enter the mass value = "))

 if choice_mass == 1:
    print(kg_to_g(value_mass),"g")
 elif choice_mass == 2:
    print (g_to_kg(value_mass),"kg")
 elif choice_mass == 3:
    print (kg_to_lb(value_mass),"lb")
 elif choice_mass == 4:
    print (lb_to_kg(value_mass),"kg")
 elif choice_mass == 5:
    print (g_to_oz(value_mass), "oz")
 elif choice_mass == 6:
    print (oz_to_g (value_mass), "g")
 else:
    print("Invalid choice")