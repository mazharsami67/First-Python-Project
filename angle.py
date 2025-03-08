# angle
def degrees_to_radians(degrees):
    return degrees * (3.141592653589793 / 180)

def radians_to_degrees(radians):
    return radians * (180 / 3.141592653589793)

from angle import degrees_to_radians, radians_to_degrees

def angle_conversion():

    print("\"Welcome to the Unit Converter for Time\"")
    print("Select the type of conversion:")
    print ("1. degree to radian")
    print ("2. radian to degree")

    choice_angle = int(input("enter choice 1/2"))

    value_angle = float(input("enter the value of angle"))

    if choice_angle == 1:
        print (degrees_to_radians(value_angle), "radians")
    elif choice_angle == 2:
        print (radians_to_degrees(value_angle), "degrees")
    else:
        print ("invalid choice ")

    