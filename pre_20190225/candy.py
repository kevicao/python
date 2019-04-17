'''
the minimum number of candies to give a line of children with ratting
http://www.programcreek.com/2014/03/leetcode-candy-java/
'''

def candy(ratings):
    if len(ratings) == 0:
        return 0
    
    candies = [1]*len(ratings)
    
    #from left
    for i in range(1,len(ratings)):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
        else:
            candies[i] = 1
            
    result = candies[-1]
    #from right
    for i in range(len(ratings)-2, -1, -1):
        cur = 1
        if ratings[i] > ratings[i+1]:
            cur = candies[i+1] + 1
            
        candies[i] = max(cur, candies[i])
        result += candies[i]
       
    return result
        
ratings = [6, 10, 9, 5, 3, 1] #16
print candy(ratings)  

