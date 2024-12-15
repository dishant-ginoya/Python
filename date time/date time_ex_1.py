# #  1.) You have two lists of dictionaries. One contains event details, and the other contains employee
# #  shift schedules. You need to filter and join these datasets based on date and time using lambda
# #  functions and Python's datetime module.
# #  NOTE : use : from datetime import datetime
# #   events = [
# #     {"event_id": 1, "event_name": "Team Meeting", "event_date": "2024-08-15T09:00:00"},
# #     {"event_id": 2, "event_name": "Project Deadline", "event_date": "2024-08-16T17:00:00"},
# #     {"event_id": 3, "event_name": "Annual Review", "event_date": "2024-08-17T14:00:00"}
# #  ]
# #   shifts = [
# #     {"shift_id": 1, "employee_id": 101, "shift_start": "2024-08-15T08:00:00", "shift_end": "2024-08-15T16:00:00"},
# #     {"shift_id": 2, "employee_id": 102, "shift_start": "2024-08-16T09:00:00", "shift_end": "2024-08-16T17:00:00"},
# #     {"shift_id": 3, "employee_id": 103, "shift_start": "2024-08-17T12:00:00", "shift_end": "2024-08-17T20:00:00"}
# #   ]
# #  Objective:
# #    2.) Filter the shifts to include only those that overlap with events (i.e., the shift end time is after the event
# #        start time, and the shift start time is before the event end time).
#      3.) Join these filtered shifts with the events
# #    4.) based on the date of the event and the shift overlap. Use lambda functions to perform the filtering and joining.
# #
# #  Output:
# #    Event: Team Meeting, Date: 2024-08-15 09:00:00
# #         Shift ID: 1, Start: 2024-08-15 08:00:00, End: 2024-08-15 16:00:00
# #    Event: Project Deadline, Date: 2024-08-16 17:00:00
# #         Shift ID: 2, Start: 2024-08-16 09:00:00, End: 2024-08-16 17:00:00
# #    Event: Annual Review, Date: 2024-08-17 14:00:00
# #         Shift ID: 3, Start: 2024-08-17 12:00:00, End: 2024-08-17 20:00:00

# # ====================================================================================================================== # #


from datetime import datetime

events = [
    {"event_id": 1, "event_name": "Team Meeting", "event_date": "2024-08-15T09:00:00"},
    {"event_id": 2, "event_name": "Project Deadline", "event_date": "2024-08-16T17:00:00"},
    {"event_id": 3, "event_name": "Annual Review", "event_date": "2024-08-17T14:00:00"}
]

shifts = [
    {"shift_id": 1, "employee_id": 101, "shift_start": "2024-08-15T08:00:00", "shift_end": "2024-08-15T16:00:00"},
    {"shift_id": 2, "employee_id": 102, "shift_start": "2024-08-16T09:00:00", "shift_end": "2024-08-16T17:00:00"},
    {"shift_id": 3, "employee_id": 103, "shift_start": "2024-08-17T12:00:00", "shift_end": "2024-08-17T20:00:00"}
]

for event in events:
    event['event_date'] = datetime.fromisoformat(event['event_date'])

for shift in shifts:
    shift['shift_start'] = datetime.fromisoformat(shift['shift_start'])
    shift['shift_end'] = datetime.fromisoformat(shift['shift_end'])

# result = []
# for event in events:
#     overlapping_shifts = list(
#         filter(lambda shift: shift['shift_end'] >= event['event_date'] and shift['shift_start'] <= event['event_date'], shifts))
#     [result.append({'event':event,'shift':shift}) for shift in overlapping_shifts]


overlapping_shifts = list(map(lambda event: {'event': event,'shift' :list(filter(lambda shift: shift['shift_end'] > event['event_date'] and shift['shift_start'] < event['event_date'], shifts))}, events))

for entry in overlapping_shifts:
    event = entry['event']
    print(f"Event: {event['event_name']}, Date: {event['event_date'].strftime('%Y-%m-%d %H:%M:%S')}")
    for shift in entry['shift']:
        print(f" --> Shift ID: {shift['shift_id']}, Start: {shift['shift_start'].strftime('%Y-%m-%d %H:%M:%S')}, End: {shift['shift_end'].strftime('%Y-%m-%d %H:%M:%S')}")