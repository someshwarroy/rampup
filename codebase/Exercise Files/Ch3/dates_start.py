#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  oToday = date.today()
  daynames = ["mon","tue","wed","thu","fri", "sat", "sun"]
  print(oToday, daynames[oToday.weekday()], oToday.day, oToday.year, oToday.month)

  # print out the date's individual components

  
  # retrieve today's weekday (0=Monday, 6=Sunday)

  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  oToday = None
  oToday = datetime.now()
  print(oToday, oToday.weekday(),oToday.year)
  # Get the current time


  
if __name__ == "__main__":
  main();
  