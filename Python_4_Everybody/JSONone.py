import urllib
import json

address = raw_input('Enter location: ')
print "Retrieving", address
data = urllib.urlopen(address).read()
print 'Retrieved',len(data),'characters'
info = json.loads(data)
sum = 0
count = 0
for i in info['comments']:
    sum = sum + i['count']
    count = count + 1
print "Count:",count
print "Sum:",sum
