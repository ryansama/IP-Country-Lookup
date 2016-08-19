# Commandline program that uses ip-api API to obtain the country of a given IP
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

