#length

def m_to_km(m):
    return m / 1000

def km_to_m(km):
    return km * 1000

def m_to_ft(m):
    return m * 3.28084

def ft_to_m(ft):
    return ft / 3.28084

def mi_to_km(mi):
    return mi * 1.60934

def km_to_mi(km):
    return km / 1.60934

from length import m_to_km, km_to_m, m_to_ft, ft_to_m, mi_to_km, km_to_mi 

def length_conversion():
 print("\"Welcome to the unit convertor for Length\"")
 print ("select the type of conversion: ")
 print("1. Meters to Kilometers")
 print("2. Kilometers to Meters")
 print("3. Meters to Feet")
 print("4. Feet to Meters")
 print("5. Miles to Kilometers")
 print("6. Kilometers to Miles")
#  value_length = (input("Enter the length value: "))
 choice_length = int(input("Enter choice (1/2/3/4/5/6): "))

 value_length = float(input("Enter the length value = "))

 if choice_length == 1:
    print (m_to_km (value_length),"km")
 elif  choice_length == 2:
    print (km_to_m(value_length),"m")
 elif  choice_length == 3:
    print (m_to_ft(value_length), "ft")
 elif  choice_length == 4:
    print (ft_to_m(value_length), "m")
 elif  choice_length == 5:
    print (mi_to_km(value_length), "km")
 elif  choice_length == 6:
    print (km_to_mi(value_length),"mi")
 else:
    print("Invalid choice")