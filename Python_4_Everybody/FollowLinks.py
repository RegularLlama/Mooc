# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

ursite = raw_input("Enter URL: ")

html = urllib.urlopen(ursite).read()
soup = BeautifulSoup(html)

tags = soup('a')
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))


for i in range(0, count):
    print tags[position-1].get("href", None)
    html = urllib.urlopen(tags[position-1].get("href", None)).read()
    soup = BeautifulSoup(html)
    tags = soup('a')