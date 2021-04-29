Magical Candy Bags

# You have N bags of candy. The ith bag contains arr[i] pieces of candy, and each of the bags is magical!
# It takes you 1 minute to eat all of the pieces of candy in a bag (irrespective of how many pieces of candy are inside), and as soon as you finish, the bag mysteriously refills. If there were x pieces of candy in the bag at the beginning of the minute, then after you've finished you'll find that floor(x/2) pieces are now inside.
# You have k minutes to eat as much candy as possible. How many pieces of candy can you eat?

def maxCandies(arr, k):
  # Write your code here
    import heapq
    heapq._heapify_max(arr)
    ans = 0
    for i in range(k):
        ans += arr[0]        
        heapq._heapreplace_max(arr, arr[0]//2)
    return ans  