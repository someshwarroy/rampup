#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it


# print today's date
uNow = datetime.now()
print("Date today: "+ str(uNow))

# print today's date one year from now
print("Date 1y: " + str(uNow + timedelta(days=365)))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  


