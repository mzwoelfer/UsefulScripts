# Timestamp conversion

These scripts convert Timestampt, epoch, to human readable dates and vice versa.

# Issue
The `date_to_timestamp.py` module only accepts dates according to the [RFC 2822](https://tools.ietf.org/html/rfc2822.html) standard, which is `"Mon, 20 Nov 1995 19:12:08 -0500"`. For further information look [here](https://docs.python.org/3/library/email.utils.html#email.utils.parsedate)