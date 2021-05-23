knapsack problem

# 0-1 knapsack problem: each item has value and weights, pick 0 or 1 of each item, total weight should be smaller than W, what is the maxium value you could get?


def knapsack(values, weights, W):
    if len(values) == 1:
        if weights[0] <= W:
            return values[0]
        else:
            return 0
        
    if weights[0] <= W:
        return max(knapsack(values[1:], weights[1:], W), values[0] + knapsack(values[1:], weights[1:], W-weights[0]))
    else:
        return knapsack(values[1:], weights[1:], W)
    
print(knapsack([60, 100, 120], [10,20,30], 50)) #220
print(knapsack([4, 5, 3, 7], [2, 3, 1, 4 ], 5)) #10    

def knapsack(W, wt, val, n):
 
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (wt[n-1] > W):
        return knapsack(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            val[n-1] + knapsack(
                W-wt[n-1], wt, val, n-1),
            knapsack(W, wt, val, n-1))
    
print(knapsack(50, [10,20,30], [60, 100, 120], 3)) #220
print(knapsack(5, [2, 3, 1, 4 ], [4, 5, 3, 7], 4)) #10 



# dp solution

def knapsack(weights, values,  W):
    dp = [[0]*(W+1) for x in range(len(values) + 1)]
    
    for i in range(1, len(values)+1):
        for j in range(1, W+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
                
    return dp[len(values)][W]

    
print(knapsack([10,20,30], [60, 100, 120], 50)) #220
print(knapsack([2, 3, 1, 4 ], [4, 5, 3, 7], 5)) #10 