# This function will take string's time data, convert them it to int and return a list hour and minutes
def time_converter(string_time):
    # Lets transform the string_time in a list of hours and minutes by splitting it form :
    splitted_time = string_time.split(":")
    return [int(splitted_time[0]), int(splitted_time[1])]

# The function that will take input execute some kind of algorithm on that input and return the result


def add_time(start_time, duration_time, starting_day=""):
    # we start by cleaning our data and make them usable
    # Let's clean data by removing the AM or PM element and assign it to an variable
    splitted_start_time = start_time.split(" ")
    day_part = splitted_start_time[1]

    # Cleaning and converting time into a 24 hour format in order to do the calculations more easily
    start_time_hours_minutes = time_converter(splitted_start_time[0])
    start_hours = start_time_hours_minutes[0]
    start_minutes = start_time_hours_minutes[1]

    # Let's call time_converter and get back durations hours and minutes
    duration_time_hours_minutes = time_converter(duration_time)
    duration_hours = duration_time_hours_minutes[0]
    duration_minutes = duration_time_hours_minutes[1]

    # Converting to 24 hour format, we check if the day part is PM, if so we add 12 to start_hours
    if day_part == "PM":
        start_hours += 12

    # As we have already a 24 hours format, Let's sum the start with the duration time
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    # Check if minutes > 60 we will add to hours and save the rest to the minutes variable
    if total_minutes > 59:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

    # add days
    days_number = 0

    # if hours is > 24 then we will add to days and save the rest to the hour variable
    if total_hours > 24:
        days_number = total_hours // 24
        total_hours = total_hours % 24

    # Let's go back to the 12 hour format
    # if hours is > the 12, we substract 12
    final_day_part = "AM"

    hours_before = total_hours

    if total_hours > 12:
        final_day_part = "PM"
        total_hours -= 12
    if total_hours == 12:
        final_day_part = "PM"
    if hours_before == 0:
        final_day_part = "AM"
        total_hours = 12

    # Check if it's the next day or many days later
    days_later = ""
    if days_number == 1:
        days_later = " (next day)"
    if days_number > 1:
        days_later = " ({} days later)".format(days_number)

    # Check if the number of minutes is < 10 then add 0 before it
    # Convert them in str
    total_minutes = str(total_minutes)

    if len(total_minutes) < 2:
        total_minutes = "0"+total_minutes

    # Adding days name for days later
    week_days = ["Monday", "Tuesday", "Wednesday",
                 "Thursday", "Friday", "Saturday", "Sunday"]

    if starting_day:
        weeks = days_number // 7
        i = week_days.index(starting_day.lower().capitalize()
                            ) + (days_number - 7 * weeks)
        if i > 6:
            i -= 7
        day = ", " + week_days[i]
    else:
        day = ""

    solution = str(total_hours) + ":" + total_minutes + \
        " " + final_day_part + day + days_later

    return solution


#print(add_time("11:40 AM", "0:25"))
