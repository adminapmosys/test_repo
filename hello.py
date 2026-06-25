#!/usr/bin/env python3
import sys
import datetime
import getpass

def greet_user():
    # Get current username
    try:
        username = getpass.getuser()
    except Exception:
        username = "Developer"

    # Get local time and format it
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    date_str = now.strftime("%A, %B %d, %Y")

    # Determine morning/afternoon/evening
    hour = now.hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print("=" * 50)
    print(f" {greeting}, {username}! ".center(50, "*"))
    print("=" * 50)
    print(f"Current Time: {time_str}")
    print(f"Current Date: {date_str}")
    print(f"Python Version: {sys.version.split()[0]}")
    print("=" * 50)
    print("Welcome to your new Python script in this repository.")
    print("Feel free to edit this file to build your application!")
    print("=" * 50)

if __name__ == "__main__":
    greet_user()
