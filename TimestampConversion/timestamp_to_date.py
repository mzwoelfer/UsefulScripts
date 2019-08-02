"""Paste your timestamp and get the date as a return"""
import datetime
TIMESTAMP_INPUT = input("Paste yor Timestamp: ")[:10]
INT_TIME_SEC = int(TIMESTAMP_INPUT)

print(
    datetime.datetime.fromtimestamp(INT_TIME_SEC).strftime('%d %m %Y %H:%M:%S')
)
