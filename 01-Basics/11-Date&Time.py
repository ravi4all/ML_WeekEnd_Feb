import time;    # This is required to include time module.
from email.utils import localtime
import calendar     # This is required to include calendar module
from _datetime import datetime
import datetime

# The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).
"""
ticks = time.time()
print(ticks)        """

# Get current time
"""
cur_time = time.localtime(time.time())
print("Current time is ",cur_time)    """

# Time and date with format
"""
format_time = time.asctime(time.localtime(time.time()))
print("Formatted time ",format_time)    """

# Getting calendar of a month
"""
cal = calendar.month(2016,7)
print(cal)  """

cal = calendar.isleap(2017)
print(cal)