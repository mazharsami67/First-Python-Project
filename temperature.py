# temperature 
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

def k_to_c(k):
    return k - 273.15

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

from temperature import c_to_f, f_to_c, c_to_k, k_to_c, f_to_k, k_to_f

def temperature_conversion():
    
    print("\"Welcome to the Unit Converter for Temperature\"")
    print ("------------------------------------------------------")
    print("Select the type of conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")

    # value_temp = float(input("Enter the temperature value: "))
    choice_temp = int(input("Enter choice (1/2/3/4/5/6): "))

    value_temp = float(input("Enter the temperature value = "))
    
    if choice_temp == 1:
        print (c_to_f(value_temp), "F")
    elif choice_temp == 2:
       print (f_to_c(value_temp), "C")
    elif choice_temp == 3:
        print (c_to_k(value_temp), "K")
        
    elif choice_temp == 4:
        print (k_to_c(value_temp), "C")
    
    elif choice_temp == 5:
        print (f_to_k(value_temp), "K")
        
    elif choice_temp == 6:
        print (k_to_f(value_temp), "F")
    else:
        print("Invalid choice")