J, K, L = raw_input().split()
J = int(J)
K = int(K)
L = int(L)

count = 0

for i in range(J, K+1):
    if i % L == 0:
        count = count + 1
    else:
        continue

print count