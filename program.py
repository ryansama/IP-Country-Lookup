#Title
#   IP Country Lookup
#Author(s)
#   Ryan Samarajeewa
#Description
#   A web app / program that offers a quick way to map a given IP address to a country.

import sqlite3
import urllib2

def main():
    response = urllib2.urlopen("http://www.ip2nation.com/ip2nation/Download")
    '''
    db_connection = sqlite3.connect('test.db')
    createTable(db_connection)
    db_connection.close()
    '''

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
