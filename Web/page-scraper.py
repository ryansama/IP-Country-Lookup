import urllib2
import sys

if len(sys.argv) != 2:
    print "Usage: python page-scraper.py <url>"
else:
    try:
        response = urllib2.urlopen(sys.argv[1])
        html = response.read()
        print html
    except:
        print "Invalid url."
