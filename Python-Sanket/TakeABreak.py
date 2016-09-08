import time
import webbrowser

count = 0
while count < 4:
    print time.ctime()
    time.sleep(10)
    webbrowser.open("xkcd.com")
    count =+ 1