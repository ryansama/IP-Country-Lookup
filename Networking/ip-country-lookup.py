#Country from IP Lookup - Enter an IP address and find the country that IP is registered in. Optional: Find the Ip automatically.
# Usage: python ip-country-lookup.py <country>
# Outputs user's current country by default

import urllib2
import json
import sys

if len(sys.argv) > 1:
    response = urllib2.urlopen("http://ip-api.com/json/" + sys.argv[1]).read()
    response_json = json.loads(response)

    if response_json["status"] == "success":
        print response_json["country"]
    else:
        print "Invalid input."
else:
    response = urllib2.urlopen("http://ip-api.com/json/").read()
    response_json = json.loads(response)

    if response_json["status"] == "success":
        print response_json["country"]
    else:
        print "Failed to obtain country."

