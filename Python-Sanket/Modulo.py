lst = []
arrSize = int(raw_input())

answer = 1

line = raw_input()
x = line.split()
if len(x) == arrSize:
    for i in x:
        i = int(i)
        answer = (answer*i) % (10**9 + 7)

    print answer

else:
    exit()

