#Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list. Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.

#usage: python page-scraper.py <valid url>
#required: Python 2.7

import urllib2
import sys
import lxml.html

url_input = ""
# returns html as string
def get_page():
    if len(sys.argv) != 2:
        print "Usage: python page-scraper.py <url>"
        exit()
    else:
        try:
            global url_input
            url_input = sys.argv[1]
            response = urllib2.urlopen(sys.argv[1])
            return response.read()
        except:
            print "Invalid url."
            exit()

dom =  lxml.html.fromstring(get_page())
links = set(dom.xpath('//a/@href'))

#add url to relative page links

try:
    f = open('list-of-links.txt', 'w')
    f.write('url: ' + url_input + '\n')
    f.write('--------------------------------\n')
    for link in links:
        f.write(link + '\n')
except:
    print "Could not create or write to file."    
