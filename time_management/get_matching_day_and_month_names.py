"""
This file is used both on and off line
"""

"""GLOBAL VARIABLES (kinda)"""
month_names = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
day_names = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


"""FUNCTIONS"""
def get_day_name_based_on_day_number(number):
    number = format_time_from_time_getter(number)
    return day_names[number - 1]


def get_month_name_based_on_month_number(number):
    number = format_time_from_time_getter(number)
    return month_names[number - 1]

# Using time_getter you get a str so we need to deal with it
def format_time_from_time_getter(number_to_format):
    if type(number_to_format) is str:
        number_to_format = int(number_to_format)
    
    return number_to_format


"""CODE"""
if __name__ == "__main__":
    for day_number in range(1, 8):
        print(get_day_name_based_on_day_number(day_number), end=" ")

    print("\n")

    for month_number in range(1, 13):
        print(get_month_name_based_on_month_number(month_number), end=" ")

    print("\n")
