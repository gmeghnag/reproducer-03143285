import time
import sys
import os

bytes = os.getenv("BYTES", 20972802)
bytes = int(bytes)

sleep = os.getenv("SLEEP", 30)
sleep = int(sleep)

exit = os.getenv("EXIT", False)
if exit != False:
  if exit.lower() == 'true':
    exit = True
  if exit.lower() == 'false':
    exit = False

while True:
  print("s" * bytes)
  time.sleep(sleep)
  if exit:
    sys.exit(0)
