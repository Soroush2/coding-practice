"""
This script shows the current date and time
"""
import datetime

def shows_current_time():
    time = datetime.datetime.now()
    print(time)

if __name__ == "__main__":
    shows_current_time()