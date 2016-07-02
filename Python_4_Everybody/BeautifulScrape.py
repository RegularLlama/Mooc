# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *


html = urllib.urlopen("http://python-data.dr-chuck.net/comments_280480.html").read()

soup = BeautifulSoup(html)
sum = 0

tags = soup('span')
for tag in tags:
    sum = sum + int(tag.contents[0])
print sum