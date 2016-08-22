import urllib2
import sys
import lxml.html

# returns string
def get_page():
    if len(sys.argv) != 2:
        print "Usage: python page-scraper.py <url>"
        exit()
    else:
        try:
            response = urllib2.urlopen(sys.argv[1])
            return response.read()
        except:
            print "Invalid url."
            exit()

dom =  lxml.html.fromstring(get_page())
for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    print link