xs = raw_input("Enter amount to withdraw: ")
ys = raw_input("Enter total balance: ")
x = float(xs)
y = float(ys)

if x%5 == 0 and x < y:
    print (y-x)-0.50
elif x>y:
    print "Insufficient funds"
elif x%5 != 0:
    print "Enter amount to withdraw in multiple of 5"