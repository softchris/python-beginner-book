# run pip install schedule
# run python solution.py "Deck 1" "12:00"

import sys
import schedule
import time

def clean(location):
  print(f"Cleaning in progress at {location}...")

args = sys.argv

if len(args) < 2:
  location = "Default Location"
  time_to_clean = "12:00"
elif len(args) == 3:
  location = args[1]
  time_to_clean = args[2]

print(f"Usage: python cleaning-ship.py [{location}] [{time_to_clean}]")
  sys.exit(1)

# Schedule cleaning at specified intervals
schedule.every().day.at(time_to_clean).do(clean, location=location)

print("Cleaning schedule initialized. Waiting for the next task...")

while True:
  schedule.run_pending()
  time.sleep(1)
