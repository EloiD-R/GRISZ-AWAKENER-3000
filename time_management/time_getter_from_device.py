"""
Here, we use the system date and time instead of an external API.
"""

"""IMPORTS"""
from datetime import datetime
from get_matching_day_and_month_names import *


"""GLOBAL VARIABLES (kind of)"""
specific_data_from_worldtimeapi_flags = [1, "Y", # Year
                                          2, "m", # Month
                                            3, "d", # Day (of month)
                                              4, "H", # Hour
                                                5, "M", # Minute
                                                  6, "S", # Second
                                                    7, "day_of_week_number",
                                                        8, "day_name",
                                                            9, "month_name"]

"""Functions"""
# Fetch and Parse
def fetch_time_from_system():
    try:
        now = datetime.now()
        current_time = now.isoformat()
        current_day_of_week_number = now.weekday() + 1  # Weekday() returns 0 for Monday, so we adjust by adding 1
        return current_time, current_day_of_week_number

    except Exception as error:
        print(f"An error occurred: {error}")
        return None, None

def parse_time_from_system(current_time):
    # In case of errors from before
    if current_time is None:
        return None
    else:
        return datetime.fromisoformat(current_time)

# Just infos available with the datetime module, for month and day name, refer to get_matching_day_and_month_names
def get_specific_data_from_system(*flags):
    all_data, day_number_of_week = fetch_time_from_system()  # Call API, not on the loops below so it is only called once
    parsed_data = parse_time_from_system(all_data)  # Parse the datetime data so it is available for data extraction
    return_data = []  # Making an iterable object to return because we don't know how much info will be returned

    if error_chain_check(all_data, day_number_of_week, parsed_data) is None:
        for flag in flags:
            return None
    else:
        # Iterate this loop for every flag given to the function
        for flag in flags:
            for index in range(len(specific_data_from_worldtimeapi_flags)):
                if specific_data_from_worldtimeapi_flags[index] == flag:
                    # If flag designates day_number_of_week (it is on another field in the response from API)
                    if flag == 7:
                        return_data.append(day_number_of_week)
                    elif flag == 8:
                        return_data.append(get_day_name_based_on_day_number(day_number_of_week))
                    elif flag == 9:
                        return_data.append(get_month_name_based_on_month_number(int(parsed_data.strftime("%m"))))
                    else:
                        # If it is basic data
                        specific_data = int(parsed_data.strftime(f"%{specific_data_from_worldtimeapi_flags[index + 1]}"))
                        return_data.append(prettify_specific_data(specific_data))

        return return_data if len(flags) > 1 else return_data[0]


def error_chain_check(*vars_to_check):
    for var in vars_to_check:
        if var is None:
            return None
        else:
            return True


def prettify_specific_data(*specific_data):
    for data in specific_data:
        # In case of errors from before
        if error_chain_check(data) is None:
            return None
        elif int(data) < 10:
            return f"0{data}"
        else:
            return str(data)


"""CODE"""
if __name__ == "__main__":

    # Get and store the infos, so it is easier for printing
    # All available infos from system datetime field
    year1, month_number1, day_number_of_month1, hour1, minute1, second1, day_number_of_week1, day_name1, month_name1 = get_specific_data_from_system(1, 2, 3, 4, 5, 6, 7, 8, 9)


    year2 = get_specific_data_from_system(1)
    month_number2 = get_specific_data_from_system(2)
    day_number_of_month2 = get_specific_data_from_system(3)
    hour2 = get_specific_data_from_system(4)
    minute2 = get_specific_data_from_system(5)
    second2 = get_specific_data_from_system(6)
    day_number_of_week2 = get_specific_data_from_system(7)
    day_name2 = get_specific_data_from_system(8)
    month_name2 = get_specific_data_from_system(9)

    # Print the time in all possible formats somebody would like to have
    print(f"{hour1}:{minute1}:{second1}")
    print(f"{day_number_of_month1}-{month_number1}-{year1}")
    print(f"{day_name1} {day_number_of_month1} of {month_name1} {year1}")
    print()
    print(f"{hour2}:{minute2}:{second2}")
    print(f"{day_number_of_month2}-{month_number2}-{year2}")
    print(f"{day_name2} {day_number_of_month2} of {month_name2} {year2}")
