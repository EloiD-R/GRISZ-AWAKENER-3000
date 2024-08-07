import time_getter_from_api
import time_getter_from_device
import subprocess


def ping_api():
    try:
        subprocess.run(["ping","-c", "4", "worldtimeapi.org"], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        return False

def get_time(*flags):
    if ping_api() == True:
        return time_getter_from_api.get_specific_data_from_worldtimeapi(*flags)
    else:
        return time_getter_from_device.get_specific_data_from_system(*flags)

def get_api_time(*flags):
    return time_getter_from_api.get_specific_data_from_worldtimeapi(*flags)

def get_device_time(*flags):
    return time_getter_from_device.get_specific_data_from_system(*flags)


if __name__ == "__main__":
    a, b, c, d, e, f, g ,h, i = get_time(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #a, b, c, d, e, f, g ,h, i = get_api_time(1, 2, 3, 4, 5, 6, 7, 8, 9)
    #a, b, c, d, e, f, g ,h, i = get_device_time(1, 2, 3, 4, 5, 6, 7, 8, 9)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)