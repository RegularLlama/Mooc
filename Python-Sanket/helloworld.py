L = int(raw_input())
N = int(raw_input())

for i in range(0,N):
    W,H = raw_input().split()
    W = int(W)
    H = int(H)
    if W < L or H < L:
        print 'UPLOAD ANOTHER'
    else:
        if W == H:
            print 'ACCEPTED'
        else:
            print 'CROP IT'