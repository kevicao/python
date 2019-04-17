# https://www.hackerrank.com/contests/amazon/challenges/meeting-schedules#!
# amazon schedule problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

M, K  = map(int, raw_input().split(' '))

all = [0]*24*60
for i in range(M):
    busy = map(int, raw_input().split(" "))
    slot = [busy[0]*60 + busy[1], busy[2]*60 + busy[3]]
    all[slot[0]:slot[1]] = [1]*(slot[1] - slot[0])
    
i = 0
while i <  len(all):
    if all[i] == 0:
        j = i
        while j< len(all) and all[j] == 0 :
            j += 1
        if j-i > K:
            print str(i/60).zfill(2), str(i%60).zfill(2), str(j/60 if j/60 != 24 else 0 ).zfill(2), str(j%60).zfill(2)
        i = j
    else:
        i += 1
