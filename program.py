#Title
#   IP Country Lookup
#Author(s)
#   Ryan Samarajeewa
#Description
#   A web app / program that offers a quick way to map a given IP address to a country.

from program import urllib2
from program import zipfile
from program import sqlite3

def main():
    print 'Please enter an IP:'

#Updates the database by downloading latest content
#from ip2nation
def updateDB():
    #Download zip file
    url = "http://www.ip2nation.com/ip2nation.zip"
    dlfile(url)

    #Extract zip file
    file = zipfile.ZipFile("ip2nation.zip")
    file.extractall()
    '''
    db_connection = sqlite3.connect('test.db')
    createTable(db_connection)
    db_connection.close()
    '''

def dlfile(url):
    # Open the url
    try:
        f = urllib2.urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(urllib2.os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())

    #Handle errors
    except urllib2.HTTPError, e:
        print "HTTP Error:", e.code, url
    except urllib2.URLError, e:
        print "URL Error:", e.reason, url

def createTable(conn):
    conn = sqlite3.connect('test.db')
    print "Opened database successfully"

    conn.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
           NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    print "Table created successfully"

main()
