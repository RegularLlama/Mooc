import re
hand = open('sumregex.txt')
shand = hand.read()

y = re.findall ('[0-9]+' ,shand)
sum = 0
for word in y :
    sum = sum + int(word)

print sum

