import copy
import random

sudoko = [[int(random.random()*10) for i in range(9)] for i in range(9)]

a = range(1,10)
check= dict()

for i in range(27):
    check[i] = copy.deepcopy(a)
    
for i in range(9):
    for j in range(9):
        b = sudoko[i][j]
        if b in check[i]:
            check[i].remove(b)
        if b in check[i+9]:
            check[i+9].remove(b)
        if b in check[i+18]:
            check[i+18].remove(b)
            
for i in range(27):
    if len(check[i]) > 0:
        print i, check[i]
        
for i in sudoko:
    print i

