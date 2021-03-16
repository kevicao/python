#!/usr/bin/env python
# coding: utf-8

# In[5]:


#min number of coins to make amount
#https://leetcode.com/problems/coin-change/solution/

#F(S)=F(S−C)+1, we do not now which coint (C) so that we need loop and take min

def coinChange(coins, amount):
    dp = [amount+1]*(amount+1)
    dp[0] = 0
    
    for i in range(amount+1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]
    
print(coinChange([1, 2, 5], 11)) #3
print(coinChange([2], 3))  # -1


# In[9]:


# number of ways to make that number
# Let us use dp[i] to denote the number of ways to sum up to amount i.
# dp[i + coin] += dp[i]
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-518-coin-change-2/
# https://www.cnblogs.com/python27/archive/2013/09/05/3303721.html

def change(coins, amount):
    dp = [1] + [0] * amount   
    for coin in coins:
        for i in range(amount - coin + 1):
            if dp[i]:
                dp[i + coin] += dp[i]
                
    return dp[amount]

print(change([2],3)) #0
print(change([5, 1, 2], 5))  #4
print(change([10],10)) #1


# In[ ]:




