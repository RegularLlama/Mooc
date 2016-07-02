import urllib
import xml.etree.ElementTree as ET

ursite = raw_input("Enter location: ")
print "Retrieving", ursite

print "length site", len(ursite)

stuff = urllib.urlopen(ursite).read()

print "length stuff", len(stuff)
tree = ET.fromstring(stuff)

print "length tree", len(tree)
sum = 0
lst = tree.findall(".//count")

print "Count: ", len(lst)

for item in lst:
    sum = int(item.text) + sum

print "Sum:", sum