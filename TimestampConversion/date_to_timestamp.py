"""Execute the script, paste your date as "Mon, 20 Nov 1995 19:12:08 -0500"
and get the tiemstamp"""
from email.utils import parsedate
import time
DATE_INPUT = input("Type in your Date:")
print("The timestamp is: ", int(time.mktime(parsedate(DATE_INPUT))))
