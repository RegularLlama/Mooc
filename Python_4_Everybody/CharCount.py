counts = dict()
str = raw_input("Enter: ")
for i in str:
    counts[i] = counts.get(i,0) + 1
print counts

for name,occurrence in counts.items():
    if occurrence>1:
        print name, occurrence