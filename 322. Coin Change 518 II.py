#!/usr/bin/env python
# coding: utf-8

# In[5]:


#min number of coins to make amount
#https://leetcode.com/problems/coin-change/solution/

#F(S)=F(S−C)+1, we do not know which coint (C) so that we need loop and take min

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

#################################################
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        mem = [0]*(amount+1)
        
        for i in range(1,amount+1):
            min_number = float('inf')
            for coin in coins:
                if i - coin >= 0 and mem[i-coin] + 1 < min_number:
                    min_number = mem[i-coin] + 1
            
            mem[i] = min_number
            
        return mem[amount] if mem[amount] != float('inf') else -1
        

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


# In[ ]: facebook: whehter it is possible to make the amount
def canGetExactChange(targetMoney, denominations):
  # Write your code here
    arr = [False]*(targetMoney+1)
    arr[0] = True
    for x in range(1,targetMoney+1):
        for denom in denominations:
            if (x - denom >= 0) and (arr[x-denom] == True):
                arr[x] = True
                
    return arr[-1]  



