from icalendar import Calendar, Event
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

# Create a new calendar
cal = Calendar()

# Set the time zone to Eastern Time
eastern = ZoneInfo("America/New_York")

# Set the start date for the first event
start_date = datetime(2024, 9, 23, tzinfo=eastern)

for num in range(12, 51):
    # Create an event
    event = Event()
    event.add('summary', f'Aligners {num}')

    # Set as an all-day event in Eastern Time
    end_date = start_date + timedelta(days=1)
    event.add('dtstart', start_date.date())
    event.add('dtend', end_date.date())

    event.add('description', f'Change aligners {num}')

    # Add the event to the calendar
    cal.add_component(event)

    # Move the start date for the next event (5 days later)
    start_date += timedelta(days=4)

# Write the calendar to a file
with open('events_numbered_every.ics', 'wb') as f:
    f.write(cal.to_ical())
