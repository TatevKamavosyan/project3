import time


def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds

    while total_seconds > 0:
        hours_remaining, remainder = divmod(total_seconds, 3600)
        minutes_remaining, seconds_remaining = divmod(remainder, 60)
        
        print("  {:02d}:{:02d}:{:02d}".format(hours_remaining,minutes_remaining,seconds_remaining))
        
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!!")

# Input for hours, minutes, and seconds in the format h:m:s
time_input = input("Enter time in the format h:m:s (e.g., 0:0:0): ")

# Split the input string into hours, minutes, and seconds
hours, minutes, seconds = map(int, time_input.split(':'))

# Start the countdown timer
countdown_timer(hours, minutes, seconds)