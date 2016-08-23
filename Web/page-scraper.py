import urllib2
import sys
import lxml.html

# returns html as string
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
links = set(dom.xpath('//a/@href'))

#add url to relative page links
f = open('list-of-links.txt', 'w')
for link in links:
    f.write(link + '\n')    
