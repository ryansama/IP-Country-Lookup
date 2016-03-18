#IP Country Lookup
#
from twill.commands import *

def main():
    go("http://www.ip2nation.com/ip2nation")
    showforms()

main()