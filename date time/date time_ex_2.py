# #   -------- Calculating Elapsed Time Across Time Zones --------
# #  Objective:
# #  1.) Compute the time elapsed between two events occurring in different time zones.
# #  2.) Convert the elapsed time into various formats (hours, minutes, seconds).
# #  3.) Handle cases where the events span across multiple time zones.
# #
# #  You have two events with their start and end times in different time zones. Your tasks include calculating the
# #  duration between these events and converting this duration into different units.
# #  NOTE : Install and Import Required Libraries: Ensure pytz is installed *** pip install pytz ***
# #
# #  4.) NOTE :  use : Import the necessary libraries: from datetime import datetime import pytz
# #  shift schedules. You need to filter and join these datasets based on date and time using lambda
# #  functions and Python's datetime module.
# #   event1 = {
# #       "event_name": "Start of Project",
# #       "start_time": "2024-08-15T09:00:00",
# #       "timezone": "America/New_York"
# #    }
# #    event2 = {
# #       "event_name": "End of Project",
# #       "end_time": "2024-08-15T17:00:00",
# #       "timezone": "Europe/London"
# #    }
# #
# #  Explanation:
# #    5.) Convert to UTC:
# #        We convert both event times from their respective time zones to UTC to make them comparable.
# #    6.) Calculate Elapsed Time:
# #        We compute the difference between the end and start times.
# #    7.)Convert to Various Formats:Convert to Various Formats:
# #        We convert the elapsed time from the timedelta object into hours, minutes, and seconds.

# # ====================================================================================================================== # #


from datetime import datetime
import pytz

event1 = {
    'event_name': 'Start of Project',
    'start_time': '2024-08-14T09:00:00',
    'timezone': 'America/New_York'
}
event2 = {
    'event_name': 'End of Project',
    'end_time': '2024-08-14T17:00:00',
    'timezone': 'Europe/London'
}


def convert_to_utc(event):
    local_tz = pytz.timezone(event['timezone'])
    local_time = local_tz.localize(
        datetime.fromisoformat(event['start_time'] if 'start_time' in event else event['end_time']))
    utc_time = local_time.astimezone(pytz.utc)
    return utc_time


def convert_elapsed_time(time):
    total_seconds = int(time.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds


start_time_utc = convert_to_utc(event1)
end_time_utc = convert_to_utc(event2)

elapsed_time = end_time_utc - start_time_utc

# total_seconds = int(elapsed_time.total_seconds())
# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

hour, minute, second = convert_elapsed_time(elapsed_time)

print(f'''Event Start Time (UTC) :- {start_time_utc.strftime("%d-%b, %Y  %I:%M:%S %p")}
Event End Time (UTC) :- {end_time_utc.strftime("%d-%b, %Y  %I:%M:%S %p")}

Elapsed Time :- {hour} hours, {minute} minutes, {second} seconds ''')




