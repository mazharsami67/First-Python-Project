# time

def s_to_min(seconds):
    return seconds / 60

def min_to_s(minutes):
    return minutes * 60

def hr_to_min(hours):
    return hours * 60

def min_to_hr(minutes):
    return minutes / 60

def day_to_hr(days):
    return days * 24

def hr_to_day(hours):
    return hours / 24

from time_con import s_to_min, min_to_s, hr_to_min, min_to_hr, day_to_hr, hr_to_day

def time_conversion():
    
    print("\"Welcome to the Unit Converter for Time\"")
    print("Select the type of conversion:")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    print("3. Hours to Minutes")
    print("4. Minutes to Hours")
    print("5. Days to Hours")
    print("6. Hours to Days")
    print("7. Exit")
    # value_time = float(input("enter time value"))
    choice_time = int(input("Enter choice (1/2/3/4/5/6/7): "))

    value_time = float(input("enter time value = "))

    if choice_time == 1:
        print (s_to_min(value_time), "min")
    elif choice_time == 2:
       print (min_to_s(value_time), "s")
    elif choice_time == 3:
       print (hr_to_min(value_time), "min")
    elif choice_time == 4:
       print (min_to_hr(value_time), "hrs")
    elif choice_time == 5:
       print (day_to_hr(value_time), "hrs")
    elif choice_time == 6:
       print (hr_to_day(value_time), "day")
    elif choice_time == 7:
        print("Goodbye!")
    else:
        print("Invalid choice")