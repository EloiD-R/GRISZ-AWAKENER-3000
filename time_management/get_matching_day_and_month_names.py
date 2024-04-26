"""
Ugly but necessary matching code
"""

"""GLOBAL VARIABLES"""
# Necessary tables
month_names_and_numbers = [1, "january", 2, "february", 3, "march", 4, "april", 5, "may", 6, "june", 7, "july", 8, "august", 9, "september", 10, "october", 11, "november", 12, "december"]
day_names_and_numbers = [1, "monday", 2, "tuesday", 3, "wednesday", 4, "thursday", 5, "friday", 6, "saturday", 7, "sunday"]

"""FUNCTIONS"""
def get_day_name_based_on_day_number(number):
    for index in range(len(day_names_and_numbers)):
        if number == day_names_and_numbers[index]:
            return day_names_and_numbers[index + 1]

def get_month_name_based_on_month_number(number):
    for index in range(len(month_names_and_numbers)):
        if number == month_names_and_numbers[index]:
            return month_names_and_numbers[index + 1]


"""CODE"""
if __name__ == "__main__":
    for day_number in range(8):
        print(get_day_name_based_on_day_number(day_number), end=" ")

    print("\n")

    for month_number in range(13):
        print(get_month_name_based_on_month_number(month_number), end=" ")
