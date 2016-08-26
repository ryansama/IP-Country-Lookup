#Fetch Current Weather - Get the current weather for a given zip/postal code. Optional: Try locating the user automatically.
#requried: -Python 2.7
#          -pyowm module (https://github.com/csparpa/pyowm)

#usage: python current-weather.py <zip/postal code>

import pyowm
import re

input_zip = ""
def getInput():
    if len(sys.argv) != 2:
        print "Usage: python current-weather.py <zip/postal code>"
        exit()
    else:
        global input_zip
        input_zip = sys.argv[1]
