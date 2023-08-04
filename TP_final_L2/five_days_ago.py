# five_days_ago.py

from datetime import datetime, timedelta


def calculate_five_days_ago():
    # Calculate the current date minus 5 days.
    current_date = datetime.now()
    five_days_ago = current_date - timedelta(days=5)

    # Obtain the timestamp (dt) of the calculated date.
    timestamp_five_days_ago = int(five_days_ago.timestamp())

    # Get the time stamps for the last 5 days in epoch.
    timestamps = [int((five_days_ago + timedelta(days=i)).timestamp())
                  for i in range(5)]

    return current_date, five_days_ago, timestamp_five_days_ago, timestamps
