"""
gas station i has gas(i), you car need cost(i) to reach next station
find the starting station if you can travel the circle, -1 if not
Solution:from qunt interview
put a car with enough gas randomly in a station, mark gas level before you add
gas, the lowest measurement gives the starting gas station

http://stackoverflow.com/questions/2286849/algorithm-for-truck-moving-around-a-circle-of-gas-stations

{4, 6}, {6, 5}, {7, 3} and {4, 5} gas and distance 2nd
"""

def gas_station(gas, cost):
    min_s = float('inf')
    s = 0
    position = 0
    
    for i in range(len(gas)):
        s += gas[i] - cost[i]
        if s < min_s:
            min_s = s
            position = (i+1)%len(gas)
            
    if s >= 0:
        return position
    else:
        return -1
    
gas = [4,6,7,4]
cost = [6,5,3,5]  

print gas_station(gas, cost)

