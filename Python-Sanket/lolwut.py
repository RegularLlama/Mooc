lst = list()
while True:
    thing = raw_input()
    if len(thing) < 1 : break
    lst.append(thing)

lst.sort()
for item in lst:
    print item