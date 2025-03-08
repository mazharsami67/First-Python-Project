
from mass import mass_conversion

from length import length_conversion

from time_con import time_conversion
    
from temperature import temperature_conversion

from angle import angle_conversion


# Main program
print("Welcome to the Unit Converter")
print ("------------------------------------------------------")
print("Select the type of conversion you want to perform:")
print("1. Mass")
print("2. Length")
print ("3. Time")
print ("4. Temperature")
print ("5. Angle")


choice_select = input("Enter choice (1/2/3/4/5): ")
if choice_select == "1":
    mass_conversion()
elif choice_select == "2":
    length_conversion()
elif choice_select == "3":
    time_conversion()
elif choice_select == "4":
    temperature_conversion()
elif choice_select == "5":
    angle_conversion()

else:
    print("Invalid choice")

