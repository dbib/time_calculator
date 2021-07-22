# This function will take string's time datas, convert them it to int and return a dictionnary of theme labeled, hour and minutes
def time_converter(string_time):
    # Lets transform the string_time in a list of hours and minutes by splitting it form :
    splitted_time = string_time.split(":")
    return {"hours": int(splitted_time[0]), "minutes": int(splitted_time[1])}

# This function take 2 dicts as parameter and return the sum of them
# The function will do the addition for us


def dict_additionned(dict1, dict2):
    additionned_hours = dict1["hours"] + dict2["hours"]
    additionned_minutes = dict1["minutes"] + dict2["minutes"]
    return [additionned_hours, additionned_minutes]

# The function that will take input execute some kind of algorithm on that input and return the result


def add_time(start_time, duration_time=0):
    # we start by cleaning our datas and make them usable
    # Let's clean data by removing the AM or PM element and assign it to an variable
    splitted_start_time = start_time.split(" ")
    day_part = splitted_start_time[1]
    start_time_cleaned = time_converter(splitted_start_time[0])
    duration_time_cleaned = time_converter(duration_time)

    # Let's sum the cleaned values
    additionned = dict_additionned(start_time_cleaned, duration_time_cleaned)

    # Let's converter back to a string the result and add up the day part
    converted_back = "{}:{} {}".format(
        str(additionned[0]), str(additionned[1]), day_part)

    return converted_back


print(add_time("3:00 PM", "3:10"))
