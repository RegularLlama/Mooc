largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" :
        break
        exit()
    try:
        n = float(num)
    except:
        print ""
        continue
    if smallest is None and largest is None:
        smallest = largest = n
    elif n < smallest:
        smallest = n
    elif n > largest :
        largest = n
if smallest is not None and largest is not None:
    print "Minimum", int(smallest)
    print "Maximum", int(largest)
else:
    print "you're done dude"
