import time
import json
import urllib
import socket
 
from Adafruit_LED_Backpack import SevenSegment
 
 
# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment()
colon = False

channel_id = "put your channel id here" # channel id
api_key = "put your api key here"
lookup_url = "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_id + "&key=" + api_key

def is_connected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        return True
    except:
        pass
    return False
 
def main():
    display.begin()
    display.clear()
    while 1:
        try:
            # Catches the webpage from google
            soup = urllib.urlopen(lookup_url)
            markup = soup.read()
            # Access the part of the JSON object that we care about
            feed_json = json.loads(markup)
            sub_count = feed_json["items"][0]["statistics"]["subscriberCount"]
            sub_count = float(sub_count)
            # Tells us how great we are (writes to display
            print(sub_count)
            display.clear()
            display.print_float(sub_count, 0)
            display.write_display()
 
        except:
            # If can't get new number, screen goes blank
            display.clear()
        time.sleep(1)
 
 
 
if __name__ == '__main__':
    main()
