import urllib

def read_text():
    quotes = open("C:/Users/neela/Documents/profane.txt")
    contents = quotes.read()
    checky(contents)

def checky(texty):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + texty)
    output = connection.read()
    connection.close()
    if "false" in output:
        print "It's all good, man"
    else:
        print "somethings afoot"


read_text()