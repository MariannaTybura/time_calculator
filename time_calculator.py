def add_time(start, duration, starting_day=None):
    week_days = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    if starting_day is not None:
        starting_day = starting_day.lower().capitalize()
        if starting_day not in week_days:
            return "Invalid day name"

    (start_time, am_pm) = start.split()
    is_afternoon = (am_pm == "PM")
    (start_hour, start_minutes) = map(int, start_time.split(":"))
    (duration_hour, duration_minutes) = map(int, duration.split(":"))

    count_days = 0
    new_time_hour = start_hour
    new_time_minutes = start_minutes + duration_minutes
    if new_time_minutes >= 60:
        new_time_hour = new_time_hour + 1
        new_time_minutes = new_time_minutes - 60
        if new_time_hour >= 12 > start_hour:
            if is_afternoon:
                count_days = count_days + 1
            is_afternoon = not is_afternoon

    while duration_hour > 0:
        if duration_hour < 12:
            previous_hour = new_time_hour
            new_time_hour = new_time_hour + duration_hour
            if previous_hour < 12 <= new_time_hour:
                if is_afternoon:
                    count_days = count_days + 1
                is_afternoon = not is_afternoon
            if new_time_hour != 12:
                new_time_hour = new_time_hour % 12
            break
        else:
            if is_afternoon:
                count_days = count_days + 1
            is_afternoon = not is_afternoon
            duration_hour = duration_hour - 12

    new_time = f"{new_time_hour}:{new_time_minutes:02d} "
    if is_afternoon:
        new_time = new_time + "PM"
    else:
        new_time = new_time + "AM"

    if starting_day is not None:
        day_number = (count_days + week_days[starting_day]) % 7
        day_name = None
        for name, number in week_days.items():
            if number == day_number:
                day_name = name
                break
        new_time = new_time + f", {day_name}"

    if count_days == 1:
        new_time = new_time + " (next day)"
    elif count_days > 1:
        new_time = new_time + f" ({count_days} days later)"
    return new_time


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)

