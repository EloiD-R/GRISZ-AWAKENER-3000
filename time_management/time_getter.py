"""
Here I use the worldtimeapi, even if it is overkilled for this use case,
it'll be better than getting the system date because it can't be modified,
I just like to have the exact time.

Also, when using the code, if any function returns None, it means that there was an error.
"""


"""IMPORTS"""
import time
import requests


"""GLOBAL VARIABLES"""
specific_data_from_worldtimeapi_flags = [1, "Y", 2, "m", 3, "d", 4, "H", 5, "M", 6, "S", 7, "day_of_week_number_number"]

"""Functions"""
# Fetch and Parse
def fetch_time_from_worldtimeapi():
    try:
        response = requests.get("https://worldtimeapi.org/api/ip")

        if response.status_code == 200:
            time = response.json()
            current_time = time['datetime']
            current_day_of_week_number = time['day_of_week']
            return current_time, current_day_of_week_number

        else:
            print(f"Failed to fetch time. Status code: {response.status_code}")
            return None, None # Generate the beginning of the error chain

    except Exception as error:
        print(f"An error occurred: {error}")
        return None, None

def parse_time_from_worldtimeapi(current_time):
    # In case of errors from before
    if current_time is None:
        return None
    else:
        return time.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f%z")


# Just infos available with the api, for month and day name, refer to get_matching_day_and_month_names
def get_specific_data_from_worldtimeapi(*flags):
    all_data, day_number_of_week = fetch_time_from_worldtimeapi() # Call API, not on the loops below so it is only called once
    parsed_data = parse_time_from_worldtimeapi(all_data) # Parse the datetime data so it is available for data extraction
    return_data = []     # Making an iterable object to return because we don't know how much info will be returned

    if error_chain_check(all_data, day_number_of_week, parsed_data) is None:
        for flag in flags:
            return_data.append(None)
    else:
        # Iterate this loop for every flag given to the function
        for flag in flags:
            # If flag designates day_number_of_week ( it is on another field in the response from API)
            if flag == specific_data_from_worldtimeapi_flags[12]:
                return_data.append(prettify_specific_data(day_number_of_week))

            # Otherwise (If flag designates something within the datetime field from API response)
            for index in range(len(specific_data_from_worldtimeapi_flags)):
                if specific_data_from_worldtimeapi_flags[index] == flag:
                    # Getting only the data we want and return it.
                    specific_data = int(time.strftime(f"%{specific_data_from_worldtimeapi_flags[index + 1]}", parsed_data))
                    return_data.append(prettify_specific_data(specific_data))

    return return_data


def error_chain_check(*vars_to_check):
    for var in vars_to_check:
        if var is None:
            return None
        else:
            return True


def prettify_specific_data(*specific_data):
    for data in specific_data:
        # In case of errors from before
        if error_chain_check(data) is None: return None
        elif int(data) < 10:
            return f"0{data}"
        else:
            return str(data)



"""CODE"""
# For debugging/testing
if __name__ == "__main__":
    from get_matching_day_and_month_names import *

    # Get and store the infos, so it is easier for printing
    # All available infos from worldtimeapi datetime field
    year = get_specific_data_from_worldtimeapi(flag=1)
    month_number = get_specific_data_from_worldtimeapi(flag=2)
    day_number_of_month = get_specific_data_from_worldtimeapi(flag=3)
    hour = get_specific_data_from_worldtimeapi(flag=4)
    minute = get_specific_data_from_worldtimeapi(flag=5)
    second = get_specific_data_from_worldtimeapi(flag=6)
    day_number_of_week = get_specific_data_from_worldtimeapi(flag=7)

    # Data not available from worldtimeapi
    month_name = get_month_name_based_on_month_number(month_number)
    day_name = get_day_name_based_on_day_number(day_number_of_week)


    # Print the time in all possible formats somebody would like to have
    print(f"{hour}:{minute}:{second}")
    print(f"{day_number_of_month}-{month_number}-{year}")
    print(f"{day_name} {day_number_of_month} of {month_name} {year}")
