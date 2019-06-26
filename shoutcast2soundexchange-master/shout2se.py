#!/usr/bin/python

import datetime
import pytz
import sys

callsign = 'KXXX'
localtz = 'America/Los_Angeles'
# Shoutcast logs look like:
# Fields: c-ip c-dns date time cs-uri-stem c-status cs(User-Agent) sc-bytes x-duration avgbandwidth
# 
# Soundexchange Required Columns:
# * "IP address" (#.#.#.#; Do NOT include port numbers (127.0.0.1:3600))
#   Shoutcast: c-ip
# * "Date" listener tuned in (YYYY-MM-DD)
#   Shoutcast: date (but must be converted to UTC)
# * "Time" listener tuned in (HH:MM:SS; 24-hour military time; UTC time zone)
#   Shoutcast: time (but must be converted to UTC)
# * "Stream" ID (No spaces)
#   Station Call Letters
# * "Duration" of listening (Seconds)
#   Shoutcast: x-duration
# * HTTP "Status" Code
#   Shoutcast: c-status
# * "Referrer"/Client Player  
#   Shoutcast: cs(User-Agent)

total = len(sys.argv)
if total < 2:
    print("I need a file name on the command line")
    quit()

print("IP Address\tDate\tTime\tStream\tDuration\tStatus\tReferrer")
with open(sys.argv[1], "r") as infile:
    for line in infile:
        li=line.strip()
        if not li.startswith("#"):
            foo = li.split(" ")
            ipaddr = foo[0]
            date = foo[2]
            time = foo[3]
            status = foo[5]
            referrer = foo[6]
            duration = foo[8]
            timestring = date + 'T' + time + 'Z'
            # Create datetime object
            d = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M:%SZ")
            # Set the time zone 
            d = pytz.timezone(localtz).localize(d)
            # Transform the time to UTC
            d = d.astimezone(pytz.utc)
            print(ipaddr + '\t' + d.strftime("%Y-%m-%d\t%H:%M:%S") + '\t' + callsign + '\t' + duration + '\t' + status + '\t' + referrer)

