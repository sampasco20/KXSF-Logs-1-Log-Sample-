# shoutcast2soundexchange
A Python script to convert shoutcast sc_w3c* logs to what SoundExchange needs

This is based on what is described at:
https://digitalservices.npr.org/post/soundexchange-streaming-file-format-standard-announced

It assumes that the shoutcast fields are in this order:
c-ip c-dns date time cs-uri-stem c-status cs(User-Agent) sc-bytes x-duration avgbandwidth

The mapping looks like this for the Soundexchange required columns:
* "IP address" (#.#.#.#; Do NOT include port numbers (127.0.0.1:3600))
  Shoutcast: c-ip
* "Date" listener tuned in (YYYY-MM-DD)
  Shoutcast: date (but must be converted to UTC)
* "Time" listener tuned in (HH:MM:SS; 24-hour military time; UTC time zone)
  Shoutcast: time (but must be converted to UTC)
* "Stream" ID (No spaces)
  Station Call Letters
* "Duration" of listening (Seconds)
  Shoutcast: x-duration
* HTTP "Status" Code
  Shoutcast: c-status
* "Referrer"/Client Player  
  Shoutcast: cs(User-Agent)
  
You will need to update the timezone and the station call letters in the script.  The output is tab delimited format that SoundExchange requires.

Typically you would run it as:

shout2se.py sc_w3c-kxxx.log	> soundexchange.log

You will need to install the pytz module.  This is typically done by running "pip install pytz".  pytz does the conversion from localtime to UTC that SoundExchange needs.

This should run on Unix variants and Mac from a terminal window.  If you are using Windows, follow these instructions... https://edu.google.com/openonline/course-builder/docs/1.10/set-up-course-builder/check-for-python.html#windows

